import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def verify_iq_problems():
    """IQ問題の詳細確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 70)
    print("IQ問題数の詳細確認")
    print("=" * 70)
    
    # 総数確認
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
    total = cursor.fetchone()[0]
    print(f"\n✓ IQ問題総数: {total}問")
    
    # 難易度別
    print("\n【難易度別】")
    cursor.execute("""
        SELECT difficulty, COUNT(*) as count 
        FROM questions 
        WHERE language = 'IQ' 
        GROUP BY difficulty 
        ORDER BY CAST(difficulty AS INTEGER)
    """)
    for row in cursor.fetchall():
        print(f"  難易度{row[0]}: {row[1]}問")
    
    # カテゴリ別
    print("\n【カテゴリ別】")
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'IQ' 
        GROUP BY category 
        ORDER BY count DESC
        LIMIT 20
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}問")
    
    # 画像付き問題数
    cursor.execute("""
        SELECT COUNT(*) 
        FROM questions 
        WHERE language = 'IQ' 
        AND question_json LIKE '%image%'
    """)
    image_count = cursor.fetchone()[0]
    print(f"\n✓ 画像付き問題: {image_count}問")
    
    # 最新10問
    print("\n【最新追加された10問】")
    cursor.execute("""
        SELECT id, category, difficulty, question_json
        FROM questions 
        WHERE language = 'IQ' 
        ORDER BY id DESC 
        LIMIT 10
    """)
    for row in cursor.fetchall():
        q_data = json.loads(row[3])
        q_text = q_data.get('question', '')[:50]
        print(f"  ID:{row[0]} | {row[1]} | 難度{row[2]} | {q_text}...")
    
    # ID範囲確認
    cursor.execute("""
        SELECT MIN(id), MAX(id) 
        FROM questions 
        WHERE language = 'IQ'
    """)
    min_id, max_id = cursor.fetchone()
    print(f"\n✓ ID範囲: {min_id} ～ {max_id}")
    
    conn.close()
    
    print("\n" + "=" * 70)
    if total >= 500:
        print("🎉 目標達成！500問以上あります！")
    else:
        print(f"⚠️  不足: あと{500-total}問必要です")
    print("=" * 70)
    
    return total

def check_api_compatibility():
    """APIが正しく問題を取得できるか確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n" + "=" * 70)
    print("API互換性チェック")
    print("=" * 70)
    
    # /api/learn と同じクエリ
    query = """
        SELECT id, language, question_json, category, difficulty, score, meaning, usage
        FROM questions
        WHERE language = 'IQ' AND difficulty IN ('1', '2', '3')
        ORDER BY CAST(difficulty AS INTEGER) ASC, id ASC
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print(f"\n✓ APIが返す問題数（難易度1-3）: {len(rows)}問")
    
    # 画像付き問題が含まれているか
    image_questions = 0
    for row in rows:
        q_data = json.loads(row[2])
        if 'image' in q_data and q_data['image']:
            image_questions += 1
    
    print(f"✓ うち画像付き: {image_questions}問")
    
    conn.close()

if __name__ == "__main__":
    total = verify_iq_problems()
    check_api_compatibility()