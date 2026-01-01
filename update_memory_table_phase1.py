# update_memory_table_phase1.py
# Phase 1対応: image_path と post_type カラムを追加

import sqlite3
import os

# データベースパス
DB_PATH = 'SemanticGrove.db'

def update_memory_posts_table():
    """memory_postsテーブルを更新（Phase 1対応）"""
    
    if not os.path.exists(DB_PATH):
        print(f"❌ データベースが見つかりません: {DB_PATH}")
        return False
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 既存のカラムを確認
        cursor.execute("PRAGMA table_info(memory_posts)")
        columns = [row[1] for row in cursor.fetchall()]
        
        print("現在のカラム:", columns)
        
        # post_type カラムを追加（存在しない場合）
        if 'post_type' not in columns:
            cursor.execute("""
                ALTER TABLE memory_posts
                ADD COLUMN post_type TEXT DEFAULT 'text'
            """)
            print("✅ post_type カラムを追加しました")
        else:
            print("ℹ️  post_type カラムは既に存在します")
        
        # image_path カラムを追加（存在しない場合）
        if 'image_path' not in columns:
            cursor.execute("""
                ALTER TABLE memory_posts
                ADD COLUMN image_path TEXT
            """)
            print("✅ image_path カラムを追加しました")
        else:
            print("ℹ️  image_path カラムは既に存在します")
        
        conn.commit()
        
        # 更新後のテーブル構造を確認
        cursor.execute("PRAGMA table_info(memory_posts)")
        updated_columns = cursor.fetchall()
        
        conn.close()
        
        print("\n更新後のテーブル構造:")
        for col in updated_columns:
            print(f"  - {col[1]}: {col[2]}")
        
        return True
            
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("記憶の巨大樹 - Phase 1 データベース更新")
    print("=" * 60)
    print()
    
    success = update_memory_posts_table()
    
    print()
    if success:
        print("🎉 Phase 1 アップデート完了！")
        print()
        print("追加された機能:")
        print("  ✅ 画像アップロード対応")
        print("  ✅ 投稿タイプ (text/image/both)")
        print("  ✅ カテゴリー拡張 (10種類)")
        print()
        print("次のステップ:")
        print("1. app_main.py のAPIを更新")
        print("2. Pillowをインストール: pip install Pillow")
        print("3. サーバーを起動: python app/app_main.py")
        print("4. ブラウザで http://localhost:5000/memory-tree にアクセス")
    else:
        print("❌ アップデート失敗")
        print()
        print("確認事項:")
        print("1. SemanticGrove.db が存在するか")
        print("2. データベースファイルの権限")
        print("3. memory_posts テーブルが既に存在するか")
    
    print("=" * 60)