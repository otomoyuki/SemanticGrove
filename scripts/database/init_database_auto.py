import sqlite3
import json
from werkzeug.security import generate_password_hash
from datetime import datetime
import os

# データベースファイル名
DB_NAME = "SemanticGrove.db"

def init_database():
    """データベースを初期化"""
    print("=" * 60)
    print("SemanticGrove データベース初期化")
    print("=" * 60)
    
    # 既存のDBがあれば削除（確認なし）
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"✓ 既存の {DB_NAME} を削除しました")
    
    # データベース接続
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n[1/4] テーブルを作成中...")
    
    # questionsテーブル
    cursor.execute("""
        CREATE TABLE questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT NOT NULL,
            question_json TEXT NOT NULL,
            category TEXT,
            difficulty TEXT NOT NULL,
            score INTEGER DEFAULT 5,
            meaning TEXT,
            usage TEXT
        )
    """)
    
    # usersテーブル
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            display_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    """)
    
    # scoresテーブル
    cursor.execute("""
        CREATE TABLE scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            mode TEXT NOT NULL,
            language TEXT,
            total_questions INTEGER,
            correct_answers INTEGER,
            time_seconds INTEGER,
            score_points INTEGER,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    
    # インデックス作成
    cursor.execute("CREATE INDEX idx_questions_language ON questions(language)")
    cursor.execute("CREATE INDEX idx_questions_difficulty ON questions(difficulty)")
    cursor.execute("CREATE INDEX idx_scores_user ON scores(user_id)")
    cursor.execute("CREATE INDEX idx_scores_mode ON scores(mode)")
    
    print("✓ テーブル作成完了")
    
    print("\n[2/4] テストユーザーを作成中...")
    
    # テストユーザー
    test_users = [
        ('testuser', 'test@example.com', 'password123', 'テストユーザー'),
        ('demo', 'demo@example.com', 'demo123', 'デモユーザー'),
        ('admin', 'admin@example.com', 'admin123', '管理者')
    ]
    
    for username, email, password, display_name in test_users:
        password_hash = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO users (username, email, password_hash, display_name)
            VALUES (?, ?, ?, ?)
        """, (username, email, password_hash, display_name))
        print(f"✓ ユーザー作成: {username} (パスワード: {password})")
    
    print("\n[3/4] サンプル問題を追加中...")
    
    # サンプル問題を追加
    sample_questions = [
        ('JavaScript', '{"question":"JavaScriptで変数を宣言するキーワードはどれですか？","options":[{"id":"A","text":"let"},{"id":"B","text":"var"},{"id":"C","text":"const"},{"id":"D","text":"すべて"}],"answer":[3]}', '基本文法', '1', 5, 'let, var, constはすべて変数宣言に使える', 'スコープや再代入の違いに注意'),
        ('Python', '{"question":"Pythonで整数型を表すデータ型はどれですか？","options":[{"id":"A","text":"int"},{"id":"B","text":"float"},{"id":"C","text":"str"},{"id":"D","text":"bool"}],"answer":[0]}', 'データ型', '1', 5, 'intは整数を表すデータ型', '数値計算やループ制御に使用'),
        ('PHP', '{"question":"PHPで変数を宣言する正しい方法はどれですか？","options":[{"id":"A","text":"$name = \\"PHP\\";"},{"id":"B","text":"var name = \\"PHP\\";"},{"id":"C","text":"let name = \\"PHP\\";"},{"id":"D","text":"name = \\"PHP\\";"}],"answer":[0]}', '基本文法', '1', 5, 'PHPでは変数名の前に$を付けて宣言する', 'PHP開発の基本'),
    ]
    
    for lang, qjson, cat, diff, score, meaning, usage in sample_questions:
        cursor.execute("""
            INSERT INTO questions (language, question_json, category, difficulty, score, meaning, usage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (lang, qjson, cat, diff, score, meaning, usage))
    
    print(f"✓ {len(sample_questions)}問のサンプル問題を追加しました")
    
    print("\n[4/4] 完了")
    
    conn.commit()
    conn.close()
    
    print("\n" + "=" * 60)
    print("✓ データベース初期化完了！")
    print("=" * 60)
    print(f"\nテストアカウント:")
    print("  ユーザー名: testuser / パスワード: password123")
    print("=" * 60)

if __name__ == "__main__":
    init_database()