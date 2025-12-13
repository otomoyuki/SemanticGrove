import sqlite3

DB_NAME = "SemanticGrove.db"

def check_schema():
    """questionsテーブルの構造を確認"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # テーブル構造を取得
    cursor.execute("PRAGMA table_info(questions)")
    columns = cursor.fetchall()
    
    print("=" * 60)
    print("questionsテーブルの構造:")
    print("=" * 60)
    for col in columns:
        print(f"カラム名: {col[1]}, 型: {col[2]}, NULL許可: {not col[3]}, デフォルト: {col[4]}")
    
    print("\n" + "=" * 60)
    print("サンプルデータ（最初の1行）:")
    print("=" * 60)
    cursor.execute("SELECT * FROM questions LIMIT 1")
    sample = cursor.fetchone()
    if sample:
        for i, col in enumerate(columns):
            print(f"{col[1]}: {sample[i]}")
    
    conn.close()

if __name__ == "__main__":
    check_schema()