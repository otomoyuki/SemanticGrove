import sqlite3
import json

conn = sqlite3.connect("SemanticGrove.db")
cursor = conn.cursor()

cursor.execute("SELECT id, language, question_json FROM questions WHERE language = 'HTML' LIMIT 3")
rows = cursor.fetchall()

print("HTML問題のサンプル:")
print("=" * 60)

for row in rows:
    print(f"\n問題ID: {row[0]}")
    print(f"言語: {row[1]}")
    print(f"JSON: {row[2][:200]}...")  # 最初の200文字
    
    try:
        data = json.loads(row[2])
        print(f"質問: {data['question']}")
        print(f"選択肢数: {len(data['options'])}")
        for opt in data['options']:
            print(f"  {opt['id']}: {opt['text']}")
    except Exception as e:
        print(f"エラー: {e}")

conn.close()