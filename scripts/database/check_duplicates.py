import sqlite3
import json
from collections import defaultdict

DB_PATH = "../../SemanticGrove.db"

def check_duplicates():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 80)
    print("問題文の重複チェック")
    print("=" * 80)
    
    cursor.execute("""
        SELECT id, language, question_json, category, difficulty
        FROM questions
        ORDER BY id
    """)
    
    questions = []
    question_map = defaultdict(list)  # 問題文 -> [(id, language, category)]
    
    for row in cursor.fetchall():
        try:
            q_data = json.loads(row[1])
            question_text = q_data.get('question', '').strip()
            
            if question_text:
                questions.append({
                    'id': row[0],
                    'language': row[1],
                    'question': question_text,
                    'category': row[3],
                    'difficulty': row[4]
                })
                
                # 問題文をキーにIDをマッピング
                question_map[question_text].append({
                    'id': row[0],
                    'language': row[1],
                    'category': row[3],
                    'difficulty': row[4]
                })
        except Exception as e:
            print(f"Error at ID {row[0]}: {e}")
    
    conn.close()
    
    # 重複をチェック
    duplicates = {q: ids for q, ids in question_map.items() if len(ids) > 1}
    
    print(f"\n総問題数: {len(questions)}問")
    print(f"ユニークな問題文: {len(question_map)}種類")
    print(f"重複している問題文: {len(duplicates)}種類")
    
    if duplicates:
        print("\n" + "=" * 80)
        print("重複問題リスト")
        print("=" * 80)
        
        for question_text, entries in sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"\n【重複度: {len(entries)}問】")
            print(f"問題文: {question_text[:100]}...")
            print("\n含まれるID:")
            for entry in entries:
                print(f"  ID:{entry['id']:5d} | {entry['language']:15s} | {entry['category']:20s} | 難易度:{entry['difficulty']}")
            print("-" * 80)
        
        # CSVに出力
        with open('../../duplicates_report.csv', 'w', encoding='utf-8-sig') as f:
            f.write('問題文,重複数,ID一覧\n')
            for question_text, entries in sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True):
                ids = ', '.join([str(e['id']) for e in entries])
                f.write(f'"{question_text}",{len(entries)},"{ids}"\n')
        
        print("\n✅ duplicates_report.csv に詳細を出力しました")
    else:
        print("\n✅ 重複はありませんでした！")
    
    print("=" * 80)

if __name__ == "__main__":
    check_duplicates()