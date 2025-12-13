import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def check_question_581():
    """問題581の詳細を確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("問題581の詳細確認")
    print("=" * 60)
    
    # 問題581を取得
    cursor.execute("SELECT * FROM questions WHERE id = 581")
    row = cursor.fetchone()
    
    if not row:
        print("❌ 問題581が見つかりません")
        return
    
    print(f"\n【基本情報】")
    print(f"ID: {row[0]}")
    print(f"Language: {row[1]}")
    print(f"Category: {row[3]}")
    print(f"Difficulty: {row[4]}")
    print(f"Score: {row[5]}")
    
    # JSONデータを解析
    question_json = json.loads(row[2])
    
    print(f"\n【問題内容】")
    print(f"問題文: {question_json.get('question', 'なし')}")
    print(f"画像パス: {question_json.get('image', 'なし')}")
    
    print(f"\n【選択肢】")
    for opt in question_json.get('options', []):
        print(f"  {opt['id']}. {opt['text']}")
    
    print(f"\n【正解】")
    answer_indices = question_json.get('answer', [])
    if answer_indices:
        correct_opt = question_json['options'][answer_indices[0]]
        print(f"  {correct_opt['id']}. {correct_opt['text']}")
    
    print(f"\n【解説】")
    print(f"  {row[6]}")  # meaning
    
    print(f"\n【学習ポイント】")
    print(f"  {row[7]}")  # usage
    
    # IQ問題を全件取得（最新10件）
    print("\n" + "=" * 60)
    print("IQ問題の最新10件")
    print("=" * 60)
    
    cursor.execute("""
        SELECT id, category, difficulty 
        FROM questions 
        WHERE language = 'IQ' 
        ORDER BY id DESC 
        LIMIT 10
    """)
    
    rows = cursor.fetchall()
    for r in rows:
        marker = "★" if r[0] == 581 else " "
        print(f"{marker} ID:{r[0]:4d} | カテゴリ:{r[1]:15s} | 難易度:{r[2]}")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("✓ 確認完了")
    print("=" * 60)

def export_question_581_json():
    """問題581をJSON形式でエクスポート（APIの返却値を確認）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT question_json, category, difficulty, score, meaning, usage 
        FROM questions 
        WHERE id = 581
    """)
    
    row = cursor.fetchone()
    if not row:
        print("問題581が見つかりません")
        return
    
    # APIが返すであろう形式
    question_data = json.loads(row[0])
    api_response = {
        "id": 581,
        "question": question_data.get("question"),
        "image": question_data.get("image"),
        "options": question_data.get("options"),
        "answer": question_data.get("answer"),
        "category": row[1],
        "difficulty": row[2],
        "score": row[3],
        "explanation": row[4],
        "learning_point": row[5]
    }
    
    print("\n【APIレスポンス形式（予想）】")
    print(json.dumps(api_response, ensure_ascii=False, indent=2))
    
    conn.close()

if __name__ == "__main__":
    check_question_581()
    export_question_581_json()