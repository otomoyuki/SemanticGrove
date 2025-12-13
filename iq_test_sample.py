import sqlite3
import json
import os

DB_NAME = "SemanticGrove.db"
IMAGE_DIR = "images"

def test_svg_integration():
    """SVG画像付き問題のサンプルテスト"""
    
    print("=" * 60)
    print("図形問題サンプルテスト")
    print("=" * 60)
    
    # 1. imagesディレクトリの作成確認
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
        print(f"✓ {IMAGE_DIR}/ ディレクトリを作成しました")
    else:
        print(f"✓ {IMAGE_DIR}/ ディレクトリは既に存在します")
    
    # 2. SVGファイルの保存先パス
    svg_filename = "iq_pattern_sample_001.svg"
    svg_path = os.path.join(IMAGE_DIR, svg_filename)
    
    print(f"\n【手動作業が必要】")
    print(f"1. 上のSVGアーティファクトをコピー")
    print(f"2. 以下のパスに保存してください：")
    print(f"   → {svg_path}")
    print(f"\n保存後、Enterキーを押してください...")
    input()
    
    # 3. SVGファイルの存在確認
    if not os.path.exists(svg_path):
        print(f"❌ エラー: {svg_path} が見つかりません")
        print(f"   SVGファイルを保存してから再実行してください")
        return False
    else:
        print(f"✓ SVGファイルを確認しました: {svg_path}")
    
    # 4. サンプル問題データ
    sample_question = {
        "question": "次の図形パターンで？に入るのは？",
        "image": svg_path,  # 画像パス
        "options": [
            {"id": "A", "text": "塗りつぶし円"},
            {"id": "B", "text": "中抜き円"},
            {"id": "C", "text": "三角形"},
            {"id": "D", "text": "四角形"}
        ],
        "answer": [0]  # A: 塗りつぶし円
    }
    
    # 5. データベースへの登録テスト
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        question_json = {
            "question": sample_question["question"],
            "image": sample_question["image"],
            "options": sample_question["options"],
            "answer": sample_question["answer"]
        }
        
        cursor.execute("""
            INSERT INTO questions 
            (language, question_json, category, difficulty, score, meaning, usage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "IQ",
            json.dumps(question_json, ensure_ascii=False),
            "図形パターン",
            "3",
            12,
            "対角線上の塗りつぶしパターン",
            "視覚的パターン認識"
        ))
        
        conn.commit()
        question_id = cursor.lastrowid
        
        print(f"\n✓ データベースに登録成功！")
        print(f"  問題ID: {question_id}")
        print(f"  カテゴリ: 図形パターン")
        print(f"  画像パス: {svg_path}")
        
        # 6. 登録内容の確認
        cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        row = cursor.fetchone()
        
        print(f"\n【登録内容の確認】")
        print(f"ID: {row[0]}")
        print(f"Language: {row[1]}")
        
        stored_json = json.loads(row[2])
        print(f"問題文: {stored_json['question']}")
        print(f"画像: {stored_json['image']}")
        print(f"選択肢数: {len(stored_json['options'])}")
        print(f"正解: {stored_json['answer']}")
        
        # 7. IQ問題の総数確認
        cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
        iq_count = cursor.fetchone()[0]
        print(f"\n現在のIQ問題数: {iq_count}問")
        
        print("\n" + "=" * 60)
        print("✓ テスト完了！")
        print("=" * 60)
        print("\n【次のステップ】")
        print("1. フロントエンドで画像が正しく表示されるか確認")
        print("2. 問題が解答できるか確認")
        print("3. 問題なければ残り49問の作成に進む")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def rollback_test():
    """テストデータの削除（必要に応じて）"""
    print("\nテストデータを削除しますか？ (y/n): ", end="")
    choice = input().lower()
    
    if choice == 'y':
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # 最後に追加された図形問題を削除
        cursor.execute("""
            DELETE FROM questions 
            WHERE language = 'IQ' 
            AND category = '図形パターン'
            ORDER BY id DESC 
            LIMIT 1
        """)
        
        conn.commit()
        conn.close()
        print("✓ テストデータを削除しました")
    else:
        print("テストデータを保持します")

if __name__ == "__main__":
    success = test_svg_integration()
    
    if success:
        print("\n削除する場合は rollback_test() を実行してください")
        # rollback_test()  # 必要に応じてコメント解除