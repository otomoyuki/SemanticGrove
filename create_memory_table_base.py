# create_memory_table_base.py
import sqlite3
import os

DB_PATH = 'SemanticGrove.db'

def create_memory_posts_table():
    """memory_postsテーブルを作成（基本版）"""
    
    if not os.path.exists(DB_PATH):
        print(f"❌ データベースが見つかりません: {DB_PATH}")
        return False
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # テーブル作成
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory_posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                content TEXT,
                category TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                likes INTEGER DEFAULT 0,
                status TEXT DEFAULT 'approved',
                post_type TEXT DEFAULT 'text',
                image_path TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # インデックス作成
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_memory_posts_user_id 
            ON memory_posts(user_id)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_memory_posts_status 
            ON memory_posts(status)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_memory_posts_created_at 
            ON memory_posts(created_at DESC)
        """)
        
        conn.commit()
        
        # 確認
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='memory_posts'")
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            print("✅ memory_postsテーブルを作成しました（Phase 1対応版）")
            print("\nテーブル構造:")
            print("  - id: INTEGER PRIMARY KEY")
            print("  - user_id: INTEGER")
            print("  - title: TEXT")
            print("  - content: TEXT")
            print("  - category: TEXT")
            print("  - created_at: TIMESTAMP")
            print("  - likes: INTEGER")
            print("  - status: TEXT")
            print("  - post_type: TEXT (Phase 1)")
            print("  - image_path: TEXT (Phase 1)")
            return True
        else:
            print("❌ テーブル作成に失敗しました")
            return False
            
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("記憶の巨大樹 - テーブル作成（Phase 1対応版）")
    print("=" * 60)
    print()
    
    success = create_memory_posts_table()
    
    print()
    if success:
        print("🎉 セットアップ完了！")
        print()
        print("次のステップ:")
        print("1. サーバーを起動: python app/app_main.py")
        print("2. ブラウザで http://localhost:5000/memory-tree にアクセス")
    else:
        print("❌ セットアップ失敗")
        print()
        print("確認事項:")
        print("1. SemanticGrove.db が存在するか")
        print("2. データベースファイルの権限")
    
    print("=" * 60)