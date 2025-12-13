import sqlite3
import os

DB_PATH = "../../SemanticGrove.db"

# 削除対象のID（IQ問題の完全重複のみ）
DELETE_IDS = [
    # A>B、B>Cの問題（702を残す）
    703, 704, 705, 706, 707, 708, 709, 710, 711,
    
    # 論理AND回路：A=1, B=1（672を残す）
    674, 676, 678, 680,
    
    # 論理AND回路：A=1, B=0（673を残す）
    675, 677, 679, 681,
    
    # サイコロ問題（最初のIDを残す）
    688,  # 2が出る（682を残す）
    689,  # 3が出る（683を残す）
    690,  # 4が出る（684を残す）
    691,  # 5が出る（685を残す）
]

def delete_duplicates():
    # バックアップを作成
    backup_path = "../../SemanticGrove_backup_before_delete.db"
    
    if not os.path.exists(backup_path):
        print("📦 バックアップを作成中...")
        import shutil
        shutil.copy2(DB_PATH, backup_path)
        print(f"✅ バックアップ完了: {backup_path}")
    else:
        print(f"ℹ️  既存のバックアップを使用: {backup_path}")
    
    # データベースに接続
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "=" * 80)
    print("削除対象の問題を確認")
    print("=" * 80)
    
    # 削除前に内容を確認
    placeholders = ','.join('?' * len(DELETE_IDS))
    cursor.execute(f"""
        SELECT id, language, question_json
        FROM questions
        WHERE id IN ({placeholders})
        ORDER BY id
    """, DELETE_IDS)
    
    import json
    print(f"\n削除対象: {len(DELETE_IDS)}問\n")
    
    for row in cursor.fetchall():
        try:
            q_data = json.loads(row[2])
            question_text = q_data.get('question', '')
            print(f"ID {row[0]:5d} | {row[1]:15s} | {question_text[:60]}")
        except:
            print(f"ID {row[0]:5d} | {row[1]:15s} | [解析エラー]")
    
    # 確認
    print("\n" + "=" * 80)
    response = input(f"\n本当に {len(DELETE_IDS)} 問を削除しますか？ (yes/no): ")
    
    if response.lower() != 'yes':
        print("❌ キャンセルしました")
        conn.close()
        return
    
    # 削除実行
    print("\n🗑️  削除中...")
    cursor.execute(f"""
        DELETE FROM questions
        WHERE id IN ({placeholders})
    """, DELETE_IDS)
    
    deleted_count = cursor.rowcount
    conn.commit()
    
    # 結果確認
    cursor.execute("SELECT COUNT(*) FROM questions")
    remaining_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("削除完了")
    print("=" * 80)
    print(f"✅ 削除した問題数: {deleted_count}問")
    print(f"📊 残りの問題数: {remaining_count}問")
    print(f"💾 バックアップ: {backup_path}")
    print("=" * 80)
    
    print("\n⚠️  削除を元に戻したい場合:")
    print(f"   copy {backup_path} {DB_PATH}")

if __name__ == "__main__":
    delete_duplicates()