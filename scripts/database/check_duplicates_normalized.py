import sqlite3
import json
import re
from collections import defaultdict

DB_PATH = "../../SemanticGrove.db"

def normalize_question(text):
    """問題文を正規化（細かい違いを吸収）"""
    # 小文字化
    text = text.lower()
    # 空白を削除
    text = re.sub(r'\s+', '', text)
    # 句読点・記号を削除
    text = re.sub(r'[？?。．、，！!（）()「」『』【】\[\]〜～]', '', text)
    # 「〜は」「〜を」などの助詞を統一
    text = text.replace('では', 'で').replace('には', 'に')
    text = text.replace('とは', 'と').replace('から', 'か')
    return text

def check_duplicates_normalized():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 80)
    print("問題文の正規化重複チェック")
    print("（表現の違いを吸収して類似問題を検出）")
    print("=" * 80)
    
    cursor.execute("""
        SELECT id, language, question_json, category, difficulty
        FROM questions
        ORDER BY id
    """)
    
    question_map = defaultdict(list)  # 正規化後の問題文 -> [元の問題情報]
    
    for row in cursor.fetchall():
        try:
            q_data = json.loads(row[2])
            original_text = q_data.get('question', '').strip()
            
            if original_text:
                normalized = normalize_question(original_text)
                
                question_map[normalized].append({
                    'id': row[0],
                    'language': row[1],
                    'original': original_text,
                    'category': row[3],
                    'difficulty': row[4]
                })
        except Exception as e:
            print(f"Error at ID {row[0]}: {e}")
    
    conn.close()
    
    # 重複をチェック
    duplicates = {norm: entries for norm, entries in question_map.items() if len(entries) > 1}
    
    total_questions = sum(len(entries) for entries in question_map.values())
    
    print(f"\n総問題数: {total_questions}問")
    print(f"正規化後のユニーク問題: {len(question_map)}種類")
    print(f"重複グループ: {len(duplicates)}種類")
    print(f"重複問題の総数: {sum(len(entries) for entries in duplicates.values())}問")
    
    if duplicates:
        print("\n" + "=" * 80)
        print("類似問題リスト（正規化後に一致）")
        print("=" * 80)
        
        # 重複度の高い順にソート
        sorted_dups = sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)
        
        for idx, (normalized, entries) in enumerate(sorted_dups, 1):
            print(f"\n【グループ {idx}: {len(entries)}問が類似】")
            print(f"正規化後: {normalized[:80]}...")
            print("\n元の問題文:")
            for entry in entries:
                print(f"  ID:{entry['id']:5d} | {entry['language']:15s} | {entry['category']:20s} | 難易度:{entry['difficulty']}")
                print(f"    → {entry['original'][:100]}")
            print("-" * 80)
        
        # CSVに出力
        with open('../../duplicates_normalized_report.csv', 'w', encoding='utf-8-sig') as f:
            f.write('グループID,重複数,言語,ID,問題文\n')
            for group_id, (normalized, entries) in enumerate(sorted_dups, 1):
                for entry in entries:
                    f.write(f'{group_id},{len(entries)},{entry["language"]},{entry["id"]},"{entry["original"]}"\n')
        
        print("\n✅ duplicates_normalized_report.csv に詳細を出力しました")
        
        # 言語別の重複統計
        print("\n" + "=" * 80)
        print("言語別の重複統計")
        print("=" * 80)
        
        lang_stats = defaultdict(int)
        for entries in duplicates.values():
            for entry in entries:
                lang_stats[entry['language']] += 1
        
        for lang, count in sorted(lang_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {lang:15s}: {count}問")
        
    else:
        print("\n✅ 正規化後も重複はありませんでした！")
    
    print("=" * 80)

if __name__ == "__main__":
    check_duplicates_normalized()