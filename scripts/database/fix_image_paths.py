import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def fix_image_paths():
    """Windowsパス（\\）をWebパス（/）に変換"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("画像パス修正スクリプト")
    print("=" * 60)
    
    # IQ問題で画像を持つものを取得
    cursor.execute("""
        SELECT id, question_json 
        FROM questions 
        WHERE language = 'IQ'
    """)
    
    rows = cursor.fetchall()
    fixed_count = 0
    
    for row in rows:
        question_id = row[0]
        question_json = json.loads(row[1])
        
        # imageフィールドがあるかチェック
        if 'image' in question_json and question_json['image']:
            old_path = question_json['image']
            
            # バックスラッシュをスラッシュに変換
            new_path = old_path.replace('\\', '/')
            
            if old_path != new_path:
                print(f"\n問題ID {question_id}:")
                print(f"  修正前: {old_path}")
                print(f"  修正後: {new_path}")
                
                # パスを更新
                question_json['image'] = new_path
                
                # データベースを更新
                cursor.execute("""
                    UPDATE questions 
                    SET question_json = ? 
                    WHERE id = ?
                """, (json.dumps(question_json, ensure_ascii=False), question_id))
                
                fixed_count += 1
    
    conn.commit()
    conn.close()
    
    print("\n" + "=" * 60)
    print(f"✓ 修正完了: {fixed_count}件の画像パスを修正しました")
    print("=" * 60)

def verify_fix():
    """修正結果を確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n【修正後の確認】")
    cursor.execute("""
        SELECT id, question_json 
        FROM questions 
        WHERE language = 'IQ' 
        AND question_json LIKE '%image%'
    """)
    
    rows = cursor.fetchall()
    
    for row in rows:
        question_json = json.loads(row[1])
        if 'image' in question_json:
            print(f"問題ID {row[0]}: {question_json['image']}")
    
    conn.close()

if __name__ == "__main__":
    fix_image_paths()
    verify_fix()