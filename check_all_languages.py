import sqlite3

DB_NAME = "SemanticGrove.db"

def check_all_language_counts():
    """全言語の問題数を確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 70)
    print("全言語の問題数確認")
    print("=" * 70)
    
    # 言語別の問題数
    cursor.execute("""
        SELECT language, COUNT(*) as count 
        FROM questions 
        GROUP BY language 
        ORDER BY count DESC
    """)
    
    languages = cursor.fetchall()
    total = 0
    
    print("\n【言語別問題数】")
    for lang, count in languages:
        total += count
        status = "✅" if count >= 100 else "⚠️" if count >= 50 else "❌"
        print(f"  {status} {lang:15s}: {count:4d}問")
    
    print(f"\n総問題数: {total}問")
    
    # 各言語のカテゴリ内訳（上位5言語のみ）
    print("\n" + "=" * 70)
    print("主要言語のカテゴリ内訳")
    print("=" * 70)
    
    for lang, _ in languages[:8]:  # 上位8言語
        if lang == "IQ":
            continue
        
        cursor.execute("""
            SELECT category, COUNT(*) as count 
            FROM questions 
            WHERE language = ?
            GROUP BY category 
            ORDER BY count DESC
            LIMIT 10
        """, (lang,))
        
        categories = cursor.fetchall()
        print(f"\n【{lang}】")
        for cat, count in categories:
            print(f"  {cat:20s}: {count}問")
    
    conn.close()
    
    # 目標設定
    print("\n" + "=" * 70)
    print("目標設定")
    print("=" * 70)
    print("\n各言語の目標:")
    print("  ✅ JavaScript, Python, PHP, Java, C#: 100問以上")
    print("  🎯 Python（試験対策込み）: 200-300問")
    print("  🎯 PHP（試験対策込み）: 200-300問")
    print("  ✅ その他の言語: 50問以上")

if __name__ == "__main__":
    check_all_language_counts()