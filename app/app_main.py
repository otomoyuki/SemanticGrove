import markdown
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import json
import os
import sys
import traceback
from datetime import datetime
import random
import uuid
from werkzeug.utils import secure_filename
from PIL import Image

# 親ディレクトリをパスに追加
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, PARENT_DIR)

# 新しいPostgreSQL用のインポート
from app_config import config
from models import db, User as PostgresUser, QuestionHistory, UserStats, PointHistory, Feedback

# パス設定
TEMPLATE_DIR = os.path.join(PARENT_DIR, "templates")
STATIC_DIR = os.path.join(PARENT_DIR, "static")
DB_PATH = os.path.join(PARENT_DIR, "SemanticGrove.db")

print("=" * 60)
print("Flask Application Starting...")
print(f"BASE_DIR: {BASE_DIR}")
print(f"PARENT_DIR: {PARENT_DIR}")
print(f"TEMPLATE_DIR: {TEMPLATE_DIR}")
print(f"STATIC_DIR: {STATIC_DIR}")
print(f"DB_PATH: {DB_PATH}")
print(f"DB Exists: {os.path.exists(DB_PATH)}")
print("=" * 60)

# Flaskアプリの初期化
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# 環境に応じた設定を読み込み
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Flask-Login設定（既存のログイン機能用）
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'このページにアクセスするにはログインが必要です'

# PostgreSQLデータベースの初期化（新機能用）
db.init_app(app)

# データベーステーブルの作成
with app.app_context():
    db.create_all()
    print("✅ PostgreSQLテーブルを作成しました")

# ==================== ユーザー管理（既存のSQLite用） ====================

class User(UserMixin):
    """Flask-Login用のユーザークラス（既存機能）"""
    def __init__(self, id, username, email, display_name):
        self.id = id
        self.username = username
        self.email = email
        self.display_name = display_name

@login_manager.user_loader
def load_user(user_id):
    """ユーザーIDからユーザー情報を取得（既存のSQLiteから）"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, display_name FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return User(row['id'], row['username'], row['email'], row['display_name'])
    return None

def get_db_connection():
    """問題データベース接続を取得（SQLite）"""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ==================== 新機能：統計管理（PostgreSQL） ====================

def get_or_create_stats_user():
    """統計用ユーザーを取得または作成（PostgreSQL）"""
    if 'stats_user_id' not in session:
        # 新しいセッションIDを生成
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        
        # PostgreSQLに統計用ユーザーを作成
        stats_user = PostgresUser(
            username=f"guest_{session_id[:8]}",
            session_id=session_id
        )
        db.session.add(stats_user)
        db.session.commit()
        
        session['stats_user_id'] = stats_user.id
        print(f"✅ 統計用ユーザーを作成: {stats_user.username}")
    else:
        stats_user = PostgresUser.query.get(session['stats_user_id'])
        if not stats_user:
            session.pop('stats_user_id', None)
            return get_or_create_stats_user()
    
    return stats_user

# ==================== 重み付き出題システム ====================

@app.route("/api/practice/<mode>")
def api_practice_weighted(mode):
    """重み付き問題出題（学習・初級・中級）"""
    try:
        language = request.args.get("lang", "すべて")
        limit = int(request.args.get("limit", 10))
        
        # ユーザーIDを取得
        stats_user = get_or_create_stats_user()
        user_id = stats_user.id
        
        # モードマッピング
        mode_map = {
            'practice': 'practice',
            'low': 'beginner',
            'middle': 'intermediate'
        }
        db_mode = mode_map.get(mode, 'practice')
        
        # 重み付き出題
        questions = get_weighted_questions(user_id, language, db_mode, limit)
        
        if not questions:
            return jsonify({"error": "No questions available"}), 404
        
        return jsonify(questions)
        
    except Exception as e:
        print(f"Error in weighted practice: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/api/practice/high")
def api_high_weighted():
    """重み付き問題出題（上級）"""
    try:
        language = request.args.get("lang", "すべて")
        limit = int(request.args.get("limit", 10))
        
        stats_user = get_or_create_stats_user()
        user_id = stats_user.id
        
        # 重み付き出題
        questions = get_weighted_questions(user_id, language, 'advanced', limit)
        
        if not questions:
            return jsonify({"error": "No questions available"}), 404
        
        return jsonify(questions)
        
    except Exception as e:
        print(f"Error in high practice: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500    

def get_weighted_questions(user_id, language, mode, limit=10):
    """正答率に基づいて重み付けした問題を取得"""
    conn = get_db_connection()
    # limitを整数に変換（文字列で渡される場合に備えて）
    limit = int(limit)

    cursor = conn.cursor()
    
    # 難易度マッピング
    difficulty_map = {
        'beginner': ['1', '2'],
        'intermediate': ['3', '4'],
        'advanced': ['5', '6', '7', '8', '9', '10']
    }
    
    difficulties = difficulty_map.get(mode, ['1'])
    placeholders = ','.join('?' * len(difficulties))
    
    query = f"""
        SELECT id, question_json, category, difficulty, score, meaning, usage
        FROM questions
        WHERE language = ? AND difficulty IN ({placeholders})
    """
    
    cursor.execute(query, [language] + difficulties)
    all_questions = cursor.fetchall()
    conn.close()
    
    if not all_questions:
        return []
    
    # 各問題の履歴を取得
    question_weights = []
    for q in all_questions:
        question_id = q['id']
        
        history = QuestionHistory.query.filter_by(
            user_id=user_id,
            question_id=question_id,
            mode=mode
        ).first()
        
        if history is None:
            weight = 100.0  # 未回答の問題
        else:
            accuracy = history.accuracy_rate
            if accuracy == 0:
                weight = 25.0
            elif accuracy < 30:
                weight = 8.0
            elif accuracy < 50:
                weight = 6.0
            elif accuracy < 70:
                weight = 4.0
            elif accuracy < 90:
                weight = 2.0
            else:
                weight = 1.0
        
        question_weights.append((q, weight))
    
    questions = [q[0] for q in question_weights]
    weights = [q[1] for q in question_weights]
    
    sample_size = min(limit, len(questions))
    selected = random.choices(questions, weights=weights, k=sample_size)
    
    # RowオブジェクトをJSON化可能な辞書に変換し、question_jsonをパース
    result = []
    for row in selected:
        # question_jsonをパースしてJSONオブジェクトに変換
        question_data = json.loads(row['question_json'])
        
        # JavaScriptが期待する形式に整形
        result.append({
            'id': row['id'],
            'question': question_data.get('question', ''),
            'options': question_data.get('options', []),
            'answer': question_data.get('answer', []),
            'category': row['category'],
            'difficulty': row['difficulty'],
            'score': row['score'],
            'explanation': row['meaning'], 
            'learning_point': row['usage']
        })
    
    return result

def record_answer(user_id, question_id, language, category, difficulty, mode, is_correct):
    """回答を記録し、統計を更新"""
    history = QuestionHistory.query.filter_by(
        user_id=user_id,
        question_id=question_id,
        mode=mode
    ).first()
    
    if history is None:
        history = QuestionHistory(
            user_id=user_id,
            question_id=question_id,
            language=language,
            category=category,
            difficulty=difficulty,
            mode=mode
        )
        db.session.add(history)
    
    # Noneチェック付きでカウント更新
    history.total_count = (history.total_count or 0) + 1
    if is_correct:
        history.correct_count = (history.correct_count or 0) + 1
        # ✨ モード別ポイント付与
        point_map = {
            'practice': 0,      # 学習モード
            'beginner': 1,      # 初級モード
            'intermediate': 2,  # 中級モード
            'advanced': 3       # 上級モード
        }
        points = point_map.get(mode, 0)
        if points > 0:
            add_sg_points(user_id, points, f'correct_{mode}_{language}')
    else:
        history.wrong_count = (history.wrong_count or 0) + 1
    history.last_attempted = datetime.utcnow()
    
    # UserStats の更新
    stats = UserStats.query.filter_by(
        user_id=user_id,
        language=language,
        mode=mode
    ).first()
    
    if stats is None:
        stats = UserStats(
            user_id=user_id,
            language=language,
            mode=mode
        )
        db.session.add(stats)
    
    # Noneチェック付きでカウント更新
    stats.total_questions_attempted = (stats.total_questions_attempted or 0) + 1
    if is_correct:
        stats.total_correct = (stats.total_correct or 0) + 1
    else:
        stats.total_wrong = (stats.total_wrong or 0) + 1
    stats.update_stats()
    
    db.session.commit()

# ==================== SGポイントシステム ====================

def add_sg_points(user_id, points, reason):
    """SGポイントを付与"""
    try:
        user = PostgresUser.query.get(user_id)
        if not user:
            return False
        
        # ポイント追加
        user.sg_points += points
        
        # 履歴記録
        history = PointHistory(
            user_id=user_id,
            points=points,
            reason=reason
        )
        db.session.add(history)
        db.session.commit()
        
        print(f"✅ {user.username} に {points} SG を付与: {reason}")
        return True
        
    except Exception as e:
        print(f"❌ ポイント付与エラー: {e}")
        db.session.rollback()
        return False

def check_login_bonus(user_id):
    """ログインボーナスをチェック"""
    try:
        user = PostgresUser.query.get(user_id)
        if not user:
            return 0
        
        today = datetime.utcnow().date()
        
        # 初回ログイン
        if user.total_logins == 0:
            add_sg_points(user_id, 10, 'first_login')
            user.total_logins = 1
            user.last_login_date = today
            db.session.commit()
            return 10
        
        # 連続ログイン
        if user.last_login_date != today:
            add_sg_points(user_id, 5, 'daily_login')
            user.total_logins += 1
            user.last_login_date = today
            db.session.commit()
            return 5
        
        return 0
        
    except Exception as e:
        print(f"❌ ログインボーナスエラー: {e}")
        return 0

# ==================== ルーティング ====================

# 🌿 SemanticField トップページ
@app.route("/")
def field_top():
    """SemanticField トップページ（2D/3D切り替え可能）"""
    return render_template('field-top.html')

# 🌲 SemanticGrove（学習エリア）
@app.route("/main")
def main():
    """ホームページ"""
    return render_template("main.html")

@app.route("/learn")
def learn():
    """学習モード"""
    return render_template("learn.html")

@app.route("/practice/low")
def practice_low():
    """初級モード"""
    return render_template("practice-low.html")

@app.route("/practice/middle")
def practice_middle():
    """中級モード"""
    return render_template("practice-middle.html")

@app.route("/practice/high")
def practice_high():
    """上級モード"""
    return render_template("practice-high.html")

# 🎮 ゲーム広場
@app.route("/games")
def games():
    """ゲーム広場ページ"""
    return render_template("game-hub.html")

# 📝 フィードバック
@app.route("/feedback")
def feedback():
    """フィードバックページ"""
    return render_template("feedback.html")

# 🌳 記憶の巨大樹（実装済み）
@app.route('/memory-tree')
def memory_tree():
    """記憶の巨大樹メインページ"""
    return render_template('memory-tree.html')

@app.route('/dino-race')
def dino_race():
    """競恐竜場（Coming Soon）"""
    return render_template('coming-soon.html', 
                         title='競恐竜場',
                         icon='🦖',
                         description='恐竜レースバトル。開発中です。')

@app.route('/wildlife')
def wildlife():
    """ワイルドライフ（Coming Soon）"""
    return render_template('coming-soon.html', 
                         title='ワイルドライフ',
                         icon='🦁',
                         description='動物の一生を体験。準備中です。')

@app.route('/shop-sim')
def shop_sim():
    """店舗シミュレーター（Coming Soon）"""
    return render_template('coming-soon.html', 
                         title='店舗経営シミュレーター',
                         icon='🏪',
                         description='お店を育てるシミュレーション。開発予定です。')

# ==================== ユーザー認証 ====================

@app.route("/login", methods=['GET', 'POST'])
def login():
    """ログイン"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        
        if user_data and check_password_hash(user_data['password_hash'], password):
            user = User(user_data['id'], user_data['username'], user_data['email'], user_data['display_name'])
            login_user(user)
            
            cursor.execute("UPDATE users SET last_login = ? WHERE id = ?", (datetime.now(), user.id))
            conn.commit()
            conn.close()
            
            flash('ログインしました！', 'success')
            return redirect(url_for('main'))
        else:
            conn.close()
            flash('ユーザー名またはパスワードが間違っています', 'error')
    
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    """ユーザー登録"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        display_name = request.form.get('display_name') or username
        
        if not username or not email or not password:
            flash('すべての項目を入力してください', 'error')
            return render_template("register.html")
        
        if len(password) < 6:
            flash('パスワードは6文字以上にしてください', 'error')
            return render_template("register.html")
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            password_hash = generate_password_hash(password)
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, display_name)
                VALUES (?, ?, ?, ?)
            """, (username, email, password_hash, display_name))
            
            conn.commit()
            conn.close()
            
            flash('登録が完了しました！ログインしてください', 'success')
            return redirect(url_for('login'))
            
        except sqlite3.IntegrityError:
            flash('そのユーザー名またはメールアドレスは既に使用されています', 'error')
            return render_template("register.html")
    
    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    """ログアウト"""
    logout_user()
    flash('ログアウトしました', 'success')
    return redirect(url_for('field_top'))


# ==================== Phase 1.5: 利用規約 ====================

@app.route('/terms')
def terms():
    """利用規約ページ"""
    return render_template('terms.html')

# ==================== API ====================

@app.route("/api/learn")
def get_learning_content():
    """学習モード用API"""
    lang = request.args.get("lang", "JavaScript")
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            SELECT id, language, question_json, category, difficulty, score, meaning, usage
            FROM questions
            WHERE language = ?
            ORDER BY CAST(difficulty AS INTEGER) ASC, id ASC
        """
        
        cursor.execute(query, (lang,))
        rows = cursor.fetchall()
        conn.close()
        
        result = []
        for row in rows:
            try:
                question_data = json.loads(row['question_json'])
                
                item = {
                    "id": row['id'],
                    "question": question_data.get('question', ''),
                    "options": question_data.get('options', []),
                    "answer": question_data.get('answer', [0]),
                    "explanation": row['meaning'] or '',
                    "learning_point": row['usage'] or '',
                    "difficulty": row['difficulty'],
                    "score": row['score']
                }
                
                if 'image' in question_data and question_data['image']:
                    item['image'] = question_data['image']
                
                result.append(item)
                
            except Exception as e:
                print(f"Error processing row {row['id']}: {e}")
                continue
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/api/save-score", methods=['POST'])
@login_required
def save_score():
    """スコアを保存"""
    data = request.json
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO scores (user_id, mode, language, total_questions, correct_answers, time_seconds, score_points)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            current_user.id,
            data.get('mode'),
            data.get('language'),
            data.get('total'),
            data.get('correct'),
            data.get('time'),
            data.get('score')
        ))
        
        conn.commit()
        conn.close()
        
        # ✨ 上級モードの終了時ボーナス計算
        if data.get('mode') == 'high':
            try:
                stats_user = get_or_create_stats_user()
                correct = data.get('correct', 0)
                total = data.get('total', 1)
                
                # (正解数²/問題数²)×20 を計算して四捨五入
                bonus = round((correct ** 2 / total ** 2) * 20)
                
                if bonus > 0:
                    add_sg_points(stats_user.id, bonus, f'advanced_completion_bonus_{correct}/{total}')
                    print(f"✅ 上級モード完了ボーナス: {bonus} SG ({correct}/{total}問正解)")
            except Exception as e:
                print(f"⚠️ ボーナス計算エラー: {e}")
        
        return jsonify({"success": True, "message": "スコアを保存しました"})
        
    except Exception as e:
        print(f"Error saving score: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/ranking")
def get_ranking():
    """ランキングを取得"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                u.display_name,
                u.username,
                MAX(s.score_points) as best_score,
                s.time_seconds,
                s.correct_answers,
                s.total_questions,
                ROUND(s.correct_answers * 100.0 / s.total_questions, 1) as accuracy,
                s.completed_at
            FROM scores s
            JOIN users u ON s.user_id = u.id
            WHERE s.mode = 'high'
            GROUP BY u.id
            ORDER BY best_score DESC, s.time_seconds ASC
            LIMIT 100
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        rankings = []
        for idx, row in enumerate(rows):
            minutes = row['time_seconds'] // 60
            seconds = row['time_seconds'] % 60
            
            rankings.append({
                "rank": idx + 1,
                "username": row['display_name'] or row['username'],
                "score": row['best_score'],
                "time": f"{minutes:02d}:{seconds:02d}",
                "accuracy": row['accuracy'],
                "completed_at": row['completed_at']
            })
        
        return jsonify(rankings)
        
    except Exception as e:
        print(f"Error getting ranking: {e}")
        return jsonify([]), 500

@app.route("/api/practice/low")
def get_practice_low():
    """初級モード用API - 問題数をカスタマイズ可能"""
    lang = request.args.get("lang", "JavaScript")
    limit = request.args.get("limit", "10")
    
    try:
        limit = int(limit)
        if limit not in [10, 20, 30, 50]:
            limit = 10
    except ValueError:
        limit = 10
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = f"""
            SELECT id, language, question_json, category, difficulty, score, meaning, usage
            FROM questions
            WHERE language = ? AND difficulty IN ('1', '2')
            ORDER BY RANDOM()
            LIMIT {limit}
        """
        
        cursor.execute(query, (lang,))
        rows = cursor.fetchall()
        conn.close()
        
        result = []
        for row in rows:
            try:
                question_data = json.loads(row['question_json'])
                
                item = {
                    "id": row['id'],
                    "question": question_data.get('question', ''),
                    "options": question_data.get('options', []),
                    "answer": question_data.get('answer', [0]),
                    "explanation": row['meaning'] or '',
                    "learning_point": row['usage'] or '',
                    "difficulty": row['difficulty'],
                    "score": row['score']
                }
                
                if 'image' in question_data and question_data['image']:
                    item['image'] = question_data['image']
                
                result.append(item)
                
            except Exception as e:
                print(f"Error processing row {row['id']}: {e}")
                continue
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/api/practice/middle")
def get_practice_middle():
    """中級モード用API - 問題数をカスタマイズ可能"""
    lang = request.args.get("lang", "JavaScript")
    limit = request.args.get("limit", "10")
    
    try:
        limit = int(limit)
        if limit not in [10, 20, 30, 50]:
            limit = 10
    except ValueError:
        limit = 10
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = f"""
            SELECT id, language, question_json, category, difficulty, score, meaning, usage
            FROM questions
            WHERE language = ? AND difficulty IN ('3', '4')
            ORDER BY RANDOM()
            LIMIT {limit}
        """
        
        cursor.execute(query, (lang,))
        rows = cursor.fetchall()
        conn.close()
        
        result = []
        for row in rows:
            try:
                question_data = json.loads(row['question_json'])
                
                item = {
                    "id": row['id'],
                    "question": question_data.get('question', ''),
                    "options": question_data.get('options', []),
                    "answer": question_data.get('answer', [0]),
                    "explanation": row['meaning'] or '',
                    "learning_point": row['usage'] or '',
                    "difficulty": row['difficulty'],
                    "score": row['score']
                }
                
                if 'image' in question_data and question_data['image']:
                    item['image'] = question_data['image']
                
                result.append(item)
                
            except Exception as e:
                print(f"Error processing row {row['id']}: {e}")
                continue
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/api/practice/high")
def get_practice_high():
    """上級モード用API - 問題数をカスタマイズ可能"""
    lang = request.args.get("lang", "JavaScript")
    limit = request.args.get("limit", "10")
    
    try:
        limit = int(limit)
        if limit not in [10, 20, 30, 50]:
            limit = 10
    except ValueError:
        limit = 10
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = f"""
            SELECT id, language, question_json, category, difficulty, score, meaning, usage
            FROM questions
            WHERE language = ? AND CAST(difficulty AS INTEGER) >= 5
            ORDER BY RANDOM()
            LIMIT {limit}
        """
        
        cursor.execute(query, (lang,))
        rows = cursor.fetchall()
        conn.close()
        
        result = []
        for row in rows:
            try:
                question_data = json.loads(row['question_json'])
                
                item = {
                    "id": row['id'],
                    "question": question_data.get('question', ''),
                    "options": question_data.get('options', []),
                    "answer": question_data.get('answer', [0]),
                    "explanation": row['meaning'] or '',
                    "learning_point": row['usage'] or '',
                    "difficulty": row['difficulty'],
                    "score": row['score']
                }
                
                if 'image' in question_data and question_data['image']:
                    item['image'] = question_data['image']
                
                result.append(item)
                
            except Exception as e:
                print(f"Error processing row {row['id']}: {e}")
                continue
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ==================== 統計API ====================

@app.route('/api/answer', methods=['POST'])
def api_answer():
    """回答を記録"""
    stats_user = get_or_create_stats_user()
    data = request.json
    
    record_answer(
        user_id=stats_user.id,
        question_id=data['question_id'],
        language=data['language'],
        category=data.get('category', ''),
        difficulty=data.get('difficulty', '1'),
        mode=data['mode'],
        is_correct=data['is_correct']
    )
    
    return jsonify({'status': 'success'})

@app.route('/api/stats/<language>/<mode>')
def api_stats(language, mode):
    """ユーザーの統計を取得"""
    stats_user = get_or_create_stats_user()
    
    stats = UserStats.query.filter_by(
        user_id=stats_user.id,
        language=language,
        mode=mode
    ).first()
    
    if stats is None:
        return jsonify({
            'total_questions': 0,
            'correct': 0,
            'wrong': 0,
            'accuracy': 0.0
        })
    
    return jsonify({
        'total_questions': stats.total_questions_attempted,
        'correct': stats.total_correct,
        'wrong': stats.total_wrong,
        'accuracy': stats.accuracy_rate
    })

@app.route('/api/feedback', methods=['POST'])
def api_feedback():
    """フィードバックを保存"""
    try:
        data = request.json
        
        feedback = Feedback(
            category=data['category'],
            message=data['message']
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        # フィードバック投稿で1 SG付与
        stats_user = get_or_create_stats_user()
        add_sg_points(stats_user.id, 1, 'feedback')

        return jsonify({
            'success': True, 
            'message': 'フィードバックを受け付けました',
            'sg_bonus': 1
        })
        
    except Exception as e:
        print(f"Feedback error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/sg/balance', methods=['GET'])
def api_sg_balance():
    """SGポイント残高を取得"""
    try:
        stats_user = get_or_create_stats_user()
        
        # ログインボーナスチェック
        bonus = check_login_bonus(stats_user.id)
        
        db.session.refresh(stats_user)
        
        return jsonify({
            'success': True,
            'balance': stats_user.sg_points,
            'bonus': bonus
        })
        
    except Exception as e:
        print(f"SG balance error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== 🆕 ゲーム統合用 SG API ====================

@app.route('/api/sg/add', methods=['POST'])
def api_sg_add():
    """SGポイントを追加（ゲーム報酬用）"""
    try:
        data = request.json
        amount = data.get('amount', 0)
        reason = data.get('reason', 'game_reward')
        
        if amount <= 0:
            return jsonify({
                'success': False,
                'error': '無効な金額です'
            }), 400
        
        stats_user = get_or_create_stats_user()
        add_sg_points(stats_user.id, amount, reason)
        
        db.session.refresh(stats_user)
        
        print(f"✅ SG追加: {amount} SG ({reason})")
        
        return jsonify({
            'success': True,
            'added': amount,
            'new_balance': stats_user.sg_points,
            'reason': reason
        })
        
    except Exception as e:
        print(f"SG add error: {e}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/sg/spend', methods=['POST'])
def api_sg_spend():
    """SGポイントを消費（ガチャ・購入用）"""
    try:
        data = request.json
        amount = data.get('amount', 0)
        reason = data.get('reason', 'game_purchase')
        
        if amount <= 0:
            return jsonify({
                'success': False,
                'error': '無効な金額です'
            }), 400
        
        stats_user = get_or_create_stats_user()
        
        # 残高チェック
        if stats_user.sg_points < amount:
            return jsonify({
                'success': False,
                'error': 'SG不足',
                'current_balance': stats_user.sg_points,
                'required': amount
            }), 400
        
        # SG消費（負の値で追加）
        add_sg_points(stats_user.id, -amount, reason)
        
        db.session.refresh(stats_user)
        
        print(f"✅ SG消費: {amount} SG ({reason})")
        
        return jsonify({
            'success': True,
            'spent': amount,
            'new_balance': stats_user.sg_points,
            'reason': reason
        })
        
    except Exception as e:
        print(f"SG spend error: {e}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500
# ==================== 管理画面 ====================

# ==================== 記憶の巨大樹 API ====================
# app_main.py に追加するコード（Phase 1対応）
# 既存の記憶の巨大樹APIを以下に置き換えてください

# 画像アップロード設定
UPLOAD_FOLDER = os.path.join(STATIC_DIR, 'uploads', 'memory-tree')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# アップロードフォルダを作成
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """許可されたファイル拡張子かチェック"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_thumbnail(image_path, thumbnail_path, size=(800, 800)):
    """サムネイル画像を作成"""
    try:
        with Image.open(image_path) as img:
            # EXIF情報を保持しつつリサイズ
            img.thumbnail(size, Image.Resampling.LANCZOS)
            # RGBに変換（PNG透過対応）
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            img.save(thumbnail_path, 'JPEG', quality=85, optimize=True)
        return True
    except Exception as e:
        print(f"サムネイル作成エラー: {e}")
        return False

# ==================== 記憶の巨大樹 API (Phase 1対応) ====================

@app.route('/api/memory-tree/posts', methods=['GET'])
def api_memory_posts():
    """投稿一覧を取得"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, user_id, title, content, category, post_type, image_path, 
                   created_at, likes, status
            FROM memory_posts
            WHERE status = 'approved'
            ORDER BY created_at DESC
            LIMIT 100
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        posts = []
        for row in rows:
            posts.append({
                'id': row['id'],
                'user_id': row['user_id'],
                'title': row['title'],
                'content': row['content'] or '',
                'category': row['category'],
                'post_type': row['post_type'],
                'image_path': row['image_path'],
                'created_at': row['created_at'],
                'likes': row['likes'],
                'status': row['status']
            })
        
        return jsonify({
            'success': True,
            'posts': posts
        })
        
    except Exception as e:
        print(f"投稿一覧取得エラー: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/memory-tree/posts/<int:post_id>', methods=['GET'])
def api_memory_post_detail(post_id):
    """投稿詳細を取得"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, user_id, title, content, category, post_type, image_path,
                   created_at, likes, status
            FROM memory_posts
            WHERE id = ? AND status = 'approved'
        """, (post_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            post = {
                'id': row['id'],
                'user_id': row['user_id'],
                'title': row['title'],
                'content': row['content'] or '',
                'category': row['category'],
                'post_type': row['post_type'],
                'image_path': row['image_path'],
                'created_at': row['created_at'],
                'likes': row['likes'],
                'status': row['status']
            }
            
            return jsonify({
                'success': True,
                'post': post
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Post not found'
            }), 404
        
    except Exception as e:
        print(f"投稿詳細取得エラー: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/memory-tree/post', methods=['POST'])
def api_memory_post_create():
    """新しい投稿を作成（画像対応）"""
    try:
        # フォームデータ取得
        title = request.form.get('title')
        category = request.form.get('category')
        post_type = request.form.get('postType')
        content = request.form.get('content', '')
        image_description = request.form.get('imageDescription', '')
        
        # バリデーション
        if not title or not category or not post_type:
            return jsonify({
                'success': False,
                'error': 'タイトル、カテゴリー、投稿タイプは必須です'
            }), 400
        
        if len(title) > 100:
            return jsonify({
                'success': False,
                'error': 'タイトルは100文字以内にしてください'
            }), 400
        
        # テキストのみ・両方の場合は本文必須
        if post_type in ['text', 'both'] and not content:
            return jsonify({
                'success': False,
                'error': '本文を入力してください'
            }), 400
        
        if len(content) > 2000:
            return jsonify({
                'success': False,
                'error': '本文は2000文字以内にしてください'
            }), 400
        
        # 画像処理
        image_path = None
        if post_type in ['image', 'both']:
            if 'image' not in request.files:
                return jsonify({
                    'success': False,
                    'error': '画像をアップロードしてください'
                }), 400
            
            file = request.files['image']
            
            if file.filename == '':
                return jsonify({
                    'success': False,
                    'error': '画像をアップロードしてください'
                }), 400
            
            if not allowed_file(file.filename):
                return jsonify({
                    'success': False,
                    'error': 'PNG, JPG形式のみ対応しています。CADデータをお持ちの方は、レンダリング画像やスクリーンショットに変換してから投稿してください。'
                }), 400
            
            # ファイルサイズチェック
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)
            
            if file_size > MAX_FILE_SIZE:
                return jsonify({
                    'success': False,
                    'error': '画像サイズは5MB以内にしてください'
                }), 400
            
            # ファイル名を生成（タイムスタンプ + ユーザーID）
            import time
            timestamp = int(time.time() * 1000)
            stats_user = get_or_create_stats_user()
            filename = secure_filename(f"{stats_user.id}_{timestamp}_{file.filename}")
            
            # 保存
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            
            # サムネイル作成
            thumbnail_filename = f"thumb_{filename}"
            thumbnail_path = os.path.join(UPLOAD_FOLDER, thumbnail_filename)
            
            if create_thumbnail(filepath, thumbnail_path):
                # サムネイルをメインとして使用
                os.remove(filepath)
                os.rename(thumbnail_path, filepath)
            
            # 相対パスを保存
            image_path = f"/static/uploads/memory-tree/{filename}"
        
        # 画像のみの場合は説明文を本文として保存
        if post_type == 'image' and image_description:
            content = image_description
        
        # ユーザーIDを取得
        stats_user = get_or_create_stats_user()
        user_id = stats_user.id
        
        # データベースに保存
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO memory_posts 
            (user_id, title, content, category, post_type, image_path, created_at, likes, status)
            VALUES (?, ?, ?, ?, ?, ?, datetime('now'), 0, 'approved')
        """, (user_id, title, content, category, post_type, image_path))
        
        post_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # SGポイント付与
        sg_bonus = 1  # Phase 1: スパム防止
        add_sg_points(user_id, sg_bonus, 'memory_tree_post')
        
        print(f"✅ 記憶の巨大樹投稿: {title} (タイプ: {post_type}) (+{sg_bonus} SG)")
        
        return jsonify({
            'success': True,
            'post_id': post_id,
            'sg_bonus': sg_bonus,
            'message': '投稿が完了しました！'
        })
        
    except Exception as e:
        print(f"投稿作成エラー: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/memory-tree/like/<int:post_id>', methods=['POST'])
def api_memory_post_like(post_id):
    """投稿にいいねする"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE memory_posts
            SET likes = likes + 1
            WHERE id = ?
        """, (post_id,))
        
        cursor.execute("SELECT likes FROM memory_posts WHERE id = ?", (post_id,))
        row = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        if row:
            return jsonify({
                'success': True,
                'likes': row['likes']
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Post not found'
            }), 404
        
    except Exception as e:
        print(f"いいねエラー: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
# ==================== 管理画面 ====================

@app.route('/admin/feedback')
def admin_feedback():
    """フィードバック管理画面（パスワード保護）"""
    if not session.get('admin_authenticated'):
        return redirect(url_for('admin_login'))
    return render_template('feedback-admin.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """管理画面ログイン"""
    if request.method == 'POST':
        password = request.form.get('password')
        ADMIN_PASSWORD = 'semantic2024'
        
        if password == ADMIN_PASSWORD:
            session['admin_authenticated'] = True
            return redirect(url_for('admin_feedback'))
        else:
            flash('パスワードが正しくありません', 'error')
    
    return render_template('admin-login.html')

@app.route('/admin/logout')
def admin_logout():
    """管理画面ログアウト"""
    session.pop('admin_authenticated', None)
    flash('ログアウトしました', 'success')
    return redirect(url_for('admin_login'))

@app.route('/api/admin/feedback', methods=['GET'])
def api_admin_feedback():
    """フィードバック一覧を取得（認証必須）"""
    if not session.get('admin_authenticated'):
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'feedbacks': [{
                'id': f.id,
                'category': f.category,
                'message': f.message,
                'created_at': f.created_at.isoformat(),
                'status': f.status
            } for f in feedbacks]
        })
    except Exception as e:
        print(f"Admin feedback error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/admin/feedback/update', methods=['POST'])
def api_admin_feedback_update():
    """フィードバックのステータスを更新（認証必須）"""
    if not session.get('admin_authenticated'):
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        data = request.json
        feedback = Feedback.query.get(data['id'])
        
        if not feedback:
            return jsonify({'success': False, 'error': 'Feedback not found'}), 404
        
        feedback.status = data['status']
        db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        print(f"Update feedback error: {e}")
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== README ====================

@app.route('/readme')
def readme():
    import os
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        readme_path = os.path.join(base_dir, 'README.md')
          
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        html = markdown.markdown(content, extensions=['fenced_code', 'tables'])
        
        return render_template('readme.html', readme_html=html)
    except Exception as e:
        return f"Error: {str(e)}", 500

# ==================== エラーハンドラ ====================

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    print(f"500 Error: {e}")
    traceback.print_exc()
    return jsonify({"error": "Internal server error"}), 500

# ==================== アプリ起動 ====================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🌿 SemanticField Starting...")
    print("=" * 60)
    print("📍 Access URLs:")
    print("   - トップページ:     http://localhost:5000/")
    print("   - SemanticGrove:   http://localhost:5000/main")
    print("   - ゲーム広場:       http://localhost:5000/games")
    print("   - フィードバック:   http://localhost:5000/feedback")
    print("=" * 60 + "\n")
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=(env == 'development'))