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

# 親ディレクトリをパスに追加
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, PARENT_DIR)

# 新しいPostgreSQL用のインポート
from app_config import config
from models import db, User as PostgresUser, QuestionHistory, UserStats

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

def get_weighted_questions(user_id, language, mode, limit=10):
    """正答率に基づいて重み付けした問題を取得"""
    conn = get_db_connection()
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
            weight = 10.0  # 未回答の問題
        else:
            accuracy = history.accuracy_rate
            if accuracy == 0:
                weight = 10.0
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
    
    return selected

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
    
    history.total_count += 1
    if is_correct:
        history.correct_count += 1
    else:
        history.wrong_count += 1
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
    
    stats.total_questions_attempted += 1
    if is_correct:
        stats.total_correct += 1
    else:
        stats.total_wrong += 1
    stats.update_stats()
    
    db.session.commit()

# ==================== ルーティング（既存） ====================

@app.route("/")
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

# ==================== 新規追加：ゲームとフィードバックページ ====================

@app.route("/games")
def games():
    """ゲームページ（Coming Soon）"""
    return render_template("coming-soon.html", page_title="ゲーム")

@app.route("/feedback")
def feedback():
    """フィードバックページ（Coming Soon）"""
    return render_template("coming-soon.html", page_title="ご意見")

# ====================================================================================

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
    return redirect(url_for('main'))

@app.route("/readme")
def readme():
    """README"""
    return render_template("readme.html")

# ==================== API（既存） ====================

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
    limit = request.args.get("limit", "10")  # デフォルト10問
    
    try:
        limit = int(limit)
        if limit not in [10, 20, 30, 50]:
            limit = 10
    except ValueError:
        limit = 10
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 難易度1-2の問題を取得
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
        
        # 難易度3-4の問題を取得
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
        
        # 難易度5以上の問題を取得
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

# ==================== 新API（統計機能） ====================

@app.route('/api/answer', methods=['POST'])
def api_answer():
    """回答を記録（新機能）"""
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
    """ユーザーの統計を取得（新機能）"""
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

# ==================== エラーハンドラ ====================

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    print(f"500 Error: {e}")
    traceback.print_exc()
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    print("\nStarting Flask development server...")
    print("Access the app at: http://localhost:5000")
    print("=" * 60 + "\n")
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=(env == 'development'))
    @app.route('/readme')
def readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        html = markdown.markdown(content, extensions=['fenced_code', 'tables'])
        return render_template('readme.html', readme_html=html)
    except:
        return "README not found", 404