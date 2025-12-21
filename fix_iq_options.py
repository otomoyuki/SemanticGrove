import sqlite3
import json

conn = sqlite3.connect('SemanticGrove.db')
cursor = conn.cursor()

# パターン問題（ID 605-779）と座標問題（ID 780-789）
cursor.execute("""
    SELECT id, question_json 
    FROM questions 
    WHERE language = 'IQ' 
    AND (
        (id BETWEEN 605 AND 779 AND question_json LIKE '%パターン%')
        OR
        (id BETWEEN 780 AND 789)
    )
""")

updated = 0
for row in cursor.fetchall():
    question_id = row[0]
    data = json.loads(row[1])
    
    # 選択肢が「選択肢A」形式の場合のみ更新
    if data.get('options') and data['options'][0]['text'].startswith('選択肢'):
        
        # 新しい選択肢（ABCDラベルなし版）
        new_options = [
            {'id': 'A', 'text': '選択肢1（画像参照）'},
            {'id': 'B', 'text': '選択肢2（画像参照）'},
            {'id': 'C', 'text': '選択肢3（画像参照）'},
            {'id': 'D', 'text': '選択肢4（画像参照）'}
        ]
        
        data['options'] = new_options
        
        cursor.execute(
            "UPDATE questions SET question_json = ? WHERE id = ?",
            [json.dumps(data, ensure_ascii=False), question_id]
        )
        updated += 1
        
        if updated <= 5:
            print(f"更新: ID {question_id} - {data.get('question', '')[:30]}...")

conn.commit()
print(f"\n✅ 合計 {updated} 件の問題を更新しました")
conn.close()

print("\n確認用クエリを実行:")
conn = sqlite3.connect('SemanticGrove.db')
cursor = conn.cursor()
cursor.execute("SELECT id, question_json FROM questions WHERE id = 623")
row = cursor.fetchone()
data = json.loads(row[1])
print(f"\nID 623の選択肢:")
for opt in data['options']:
    print(f"  {opt}")
conn.close()