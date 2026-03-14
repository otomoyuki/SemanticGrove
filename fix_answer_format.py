"""
SemanticGrove - answer形式修正スクリプト
========================================
問題: answer=[0] → 選択肢シャッフル後に正解がズレる
修正: answer=[0] → answer="A"（選択肢のidで保存）

使い方:
  python fix_answer_format.py               # ドライラン（変更なし・確認のみ）
  python fix_answer_format.py --apply       # 実際に修正を適用

必ずバックアップを取ってから実行してください！
  cp SemanticGrove.db SemanticGrove.db.backup
"""

import sqlite3
import json
import shutil
import sys
from datetime import datetime

DB_PATH = "SemanticGrove.db"
DRY_RUN = "--apply" not in sys.argv

def fix_answers(dry_run=True):
    # バックアップ作成（--apply時のみ）
    if not dry_run:
        backup_path = f"SemanticGrove.db.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(DB_PATH, backup_path)
        print(f"✅ バックアップ作成: {backup_path}")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, question_json FROM questions")
    rows = cur.fetchall()

    updated = 0
    skipped = 0
    errors = []

    for qid, qjson in rows:
        try:
            qj = json.loads(qjson)
            ans = qj.get("answer", [])
            opts = qj.get("options", [])

            # すでに文字列形式ならスキップ
            if isinstance(ans, str):
                skipped += 1
                continue

            if not isinstance(ans, list) or len(ans) == 0:
                errors.append((qid, f"answer形式不明: {ans}"))
                continue

            idx = ans[0]
            if idx >= len(opts):
                errors.append((qid, f"index={idx}だがoptions={len(opts)}件"))
                continue

            # インデックス → 選択肢のidに変換
            correct_option_id = opts[idx].get("id", ["A","B","C","D"][idx])
            qj["answer"] = correct_option_id

            if not dry_run:
                cur.execute(
                    "UPDATE questions SET question_json = ? WHERE id = ?",
                    (json.dumps(qj, ensure_ascii=False), qid)
                )
            updated += 1

        except Exception as e:
            errors.append((qid, str(e)))

    if not dry_run:
        conn.commit()
    conn.close()

    # 結果表示
    mode = "【ドライラン】" if dry_run else "【適用完了】"
    print(f"\n{mode} 修正結果")
    print(f"  変換対象: {updated}件")
    print(f"  スキップ: {skipped}件（すでに文字列形式）")
    print(f"  エラー:   {len(errors)}件")

    if errors:
        print("\nエラー詳細:")
        for qid, msg in errors[:10]:
            print(f"  id={qid}: {msg}")

    if dry_run:
        print("\n※ 実際に修正するには --apply オプションを付けて実行してください")
        print(f"  python {sys.argv[0]} --apply")
    else:
        print("\n✅ 修正完了！")
        print("フロントエンドのanswer判定も確認してください。")
        print("  修正前: qj.answer[0] でインデックス比較")
        print("  修正後: qj.answer で 'A'/'B'/'C'/'D' を直接比較")

if __name__ == "__main__":
    print(f"DB: {DB_PATH}")
    print(f"モード: {'ドライラン（確認のみ）' if DRY_RUN else '実際に適用'}")
    print()
    fix_answers(dry_run=DRY_RUN)