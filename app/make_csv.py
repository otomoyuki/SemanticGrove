import sqlite3
import csv
import os

# 正しいパスを指定
db_path = os.path.join(os.path.dirname(__file__), '..', 'SemanticGrove.db')
print(f"データベースパス: {db_path}")
print(f"存在確認: {os.path.exists(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    SELECT id, language, question_json
    FROM questions
    ORDER BY id
""")

output_path = os.path.join(os.path.dirname(__file__), '..', 'questions_export_utf8.csv')

with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'language', 'question'])
    
    count = 0
    for row in cursor.fetchall():
        import json
        try:
            q_data = json.loads(row[2])
            question_text = q_data.get('question', '')
            writer.writerow([row[0], row[1], question_text])
            count += 1
        except Exception as e:
            print(f"Error at row {row[0]}: {e}")
            writer.writerow([row[0], row[1], 'ERROR'])

conn.close()
print(f"✅ {count}問を questions_export_utf8.csv に出力しました")