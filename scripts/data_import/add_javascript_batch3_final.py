import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_javascript_batch3_final():
    """JavaScript問題追加（第3弾・最終10問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("JavaScript問題追加スクリプト（第3弾・最終10問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== エラーハンドリングとデバッグ（5問） ====================
    print("[1/2] エラーハンドリング問題を生成中...")
    
    error_questions = [
        ("try-catchでエラーを捕捉する構文は？",
         [{"id":"A","text":"try {} catch(e) {}"},{"id":"B","text":"try {} error(e) {}"},{"id":"C","text":"catch {} try {}"},{"id":"D","text":"handle {}"}],
         [0], "エラーハンドリング", "2", 8, "例外処理の基本構文", "try-catch"),
        
        ("throw new Error('message') の役割は？",
         [{"id":"A","text":"エラーを投げる"},{"id":"B","text":"エラーを捕捉"},{"id":"C","text":"エラーを無視"},{"id":"D","text":"ログ出力"}],
         [0], "エラーハンドリング", "2", 8, "意図的にエラーを発生させる", "throw"),
        
        ("finallyブロックの実行タイミングは？",
         [{"id":"A","text":"成功・失敗に関わらず必ず実行"},{"id":"B","text":"成功時のみ"},{"id":"C","text":"失敗時のみ"},{"id":"D","text":"実行されない"}],
         [0], "エラーハンドリング", "2", 8, "クリーンアップ処理に使う", "finally"),
        
        ("console.log()の役割は？",
         [{"id":"A","text":"デバッグ出力"},{"id":"B","text":"エラー処理"},{"id":"C","text":"ファイル書き込み"},{"id":"D","text":"変数宣言"}],
         [0], "デバッグ", "1", 5, "コンソールに出力", "console.log"),
        
        ("typeof null の結果は？",
         [{"id":"A","text":"'object'"},{"id":"B","text":"'null'"},{"id":"C","text":"'undefined'"},{"id":"D","text":"エラー"}],
         [0], "デバッグ", "3", 10, "JavaScriptの歴史的なバグ", "typeof"),
    ]
    
    questions.extend(error_questions)
    print(f"  ✓ エラーハンドリング: {len(error_questions)}問")
    
    # ==================== 実践的な応用問題（5問） ====================
    print("[2/2] 実践的な応用問題を生成中...")
    
    practical_questions = [
        ("JSON.parse()の役割は？",
         [{"id":"A","text":"JSON文字列をオブジェクトに変換"},{"id":"B","text":"オブジェクトをJSON文字列に変換"},{"id":"C","text":"検証"},{"id":"D","text":"圧縮"}],
         [0], "JSON", "2", 8, "JSON文字列をパース", "JSON.parse"),
        
        ("JSON.stringify()の役割は？",
         [{"id":"A","text":"オブジェクトをJSON文字列に変換"},{"id":"B","text":"JSON文字列をオブジェクトに変換"},{"id":"C","text":"検証"},{"id":"D","text":"圧縮"}],
         [0], "JSON", "2", 8, "オブジェクトをJSON化", "JSON.stringify"),
        
        ("localStorage.setItem('key', 'value')の役割は？",
         [{"id":"A","text":"ブラウザにデータ保存"},{"id":"B","text":"サーバーに送信"},{"id":"C","text":"Cookie作成"},{"id":"D","text":"セッション開始"}],
         [0], "ブラウザAPI", "2", 8, "ローカルストレージに保存", "localStorage"),
        
        ("setInterval(fn, 1000)の動作は？",
         [{"id":"A","text":"1秒ごとにfnを実行"},{"id":"B","text":"1秒後に1回実行"},{"id":"C","text":"即座に実行"},{"id":"D","text":"実行しない"}],
         [0], "タイマー", "2", 8, "定期的に関数を実行", "setInterval"),
        
        ("clearInterval(id)の役割は？",
         [{"id":"A","text":"setIntervalを停止"},{"id":"B","text":"setTimeoutを停止"},{"id":"C","text":"全タイマー停止"},{"id":"D","text":"エラー"}],
         [0], "タイマー", "2", 8, "インターバルをクリア", "clearInterval"),
    ]
    
    questions.extend(practical_questions)
    print(f"  ✓ 実践的な応用問題: {len(practical_questions)}問")
    
    # データベースに挿入
    print("\nデータベースに保存中...")
    for q in questions:
        question_json = {
            "question": q[0],
            "options": q[1],
            "answer": q[2]
        }
        
        cursor.execute("""
            INSERT INTO questions 
            (language, question_json, category, difficulty, score, meaning, usage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("JavaScript", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'JavaScript'")
    js_count = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'JavaScript' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊🎊🎊 JavaScript 100問達成！！！ 🎊🎊🎊")
    print("=" * 60)
    print(f"JavaScript問題数: {js_count}問")
    print(f"全体問題数: {total_count}問")
    
    if js_count >= 100:
        print("\n【達成したカテゴリ】")
        for cat, count in categories:
            print(f"  {cat}: {count}問")
        
        print("\n" + "=" * 60)
        print("✅ JavaScript 100問達成！")
        print("次はPython 100問を目指しましょう！")
        print("=" * 60)
    else:
        print(f"\n目標100問まで残り: {100 - js_count}問")
    
    print("=" * 60)

if __name__ == "__main__":
    add_javascript_batch3_final()