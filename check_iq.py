import sqlite3
import json

conn = sqlite3.connect('SemanticGrove.db')
cursor = conn.cursor()

# ID 620-630あたりのIQ問題を確認
cursor.execute("""
    SELECT id, question_json 
    FROM questions 
    WHERE language = 'IQ' 
    AND id BETWEEN 620 AND 630
    ORDER BY id
""")

for row in cursor.fetchall():
    question_id = row[0]
    data = json.loads(row[1])
    
    print(f"\n{'='*60}")
    print(f"問題ID: {question_id}")
    print(f"問題文: {data.get('question', 'なし')}")
    print(f"画像: {data.get('image', 'なし')}")
    print(f"選択肢:")
    for i, opt in enumerate(data.get('options', [])):
        print(f"  {i}: {opt}")
    print(f"正解インデックス: {data.get('answer', 'なし')}")

conn.close()