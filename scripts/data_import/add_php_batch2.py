import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_php_batch2():
    """PHP問題追加（第2弾・30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("PHP問題追加スクリプト（第2弾・30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== 配列操作（10問） ====================
    print("[1/3] 配列操作問題を生成中...")
    
    array_questions = [
        ("配列の定義方法は？",
         [{"id":"A","text":"array() または []"},{"id":"B","text":"[] のみ"},{"id":"C","text":"{}"},{"id":"D","text":"()"}],
         [0], "配列", "1", 5, "配列作成", "array"),
        
        ("連想配列の書き方は？",
         [{"id":"A","text":"['key' => 'value']"},{"id":"B","text":"['key': 'value']"},{"id":"C","text":"['key', 'value']"},{"id":"D","text":"{'key': 'value'}"}],
         [0], "配列", "2", 8, "キーと値のペア", "連想配列"),
        
        ("count() の役割は？",
         [{"id":"A","text":"配列の要素数"},{"id":"B","text":"文字数"},{"id":"C","text":"合計値"},{"id":"D","text":"最大値"}],
         [0], "配列", "1", 5, "要素数取得", "count"),
        
        ("array_push() の役割は？",
         [{"id":"A","text":"配列の末尾に追加"},{"id":"B","text":"先頭に追加"},{"id":"C","text":"削除"},{"id":"D","text":"ソート"}],
         [0], "配列", "2", 8, "要素追加", "array_push"),
        
        ("array_pop() の役割は？",
         [{"id":"A","text":"末尾の要素を削除して返す"},{"id":"B","text":"先頭を削除"},{"id":"C","text":"追加"},{"id":"D","text":"ソート"}],
         [0], "配列", "2", 8, "末尾削除", "array_pop"),
        
        ("in_array() の役割は？",
         [{"id":"A","text":"値が配列に存在するか"},{"id":"B","text":"キー存在確認"},{"id":"C","text":"追加"},{"id":"D","text":"削除"}],
         [0], "配列", "2", 8, "値の存在チェック", "in_array"),
        
        ("array_merge() の役割は？",
         [{"id":"A","text":"配列の結合"},{"id":"B","text":"配列の分割"},{"id":"C","text":"ソート"},{"id":"D","text":"削除"}],
         [0], "配列", "2", 8, "配列マージ", "array_merge"),
        
        ("sort() の動作は？",
         [{"id":"A","text":"昇順ソート（破壊的）"},{"id":"B","text":"降順ソート"},{"id":"C","text":"非破壊的"},{"id":"D","text":"キーを保持"}],
         [0], "配列", "2", 8, "ソート", "sort"),
        
        ("array_keys() の役割は？",
         [{"id":"A","text":"全てのキーを取得"},{"id":"B","text":"全ての値を取得"},{"id":"C","text":"要素数"},{"id":"D","text":"ソート"}],
         [0], "配列", "2", 8, "キー配列取得", "array_keys"),
        
        ("array_values() の役割は？",
         [{"id":"A","text":"全ての値を取得"},{"id":"B","text":"全てのキーを取得"},{"id":"C","text":"要素数"},{"id":"D","text":"ソート"}],
         [0], "配列", "2", 8, "値配列取得", "array_values"),
    ]
    
    questions.extend(array_questions)
    print(f"  ✓ 配列操作: {len(array_questions)}問")
    
    # ==================== 関数（10問） ====================
    print("[2/3] 関数問題を生成中...")
    
    function_questions = [
        ("関数の定義方法は？",
         [{"id":"A","text":"function name() { }"},{"id":"B","text":"def name(): {}"},{"id":"C","text":"func name() {}"},{"id":"D","text":"fn name() {}"}],
         [0], "関数", "1", 5, "関数定義", "function"),
        
        ("return文の役割は？",
         [{"id":"A","text":"値を返して関数終了"},{"id":"B","text":"ループ終了"},{"id":"C","text":"出力"},{"id":"D","text":"変数宣言"}],
         [0], "関数", "1", 5, "返り値", "return"),
        
        ("デフォルト引数の書き方は？",
         [{"id":"A","text":"function f($x = 1) { }"},{"id":"B","text":"function f($x := 1) { }"},{"id":"C","text":"function f(int $x = 1) { }のみ"},{"id":"D","text":"不可能"}],
         [0], "関数", "2", 8, "引数デフォルト値", "デフォルト引数"),
        
        ("可変長引数の書き方は？（PHP 5.6+）",
         [{"id":"A","text":"function f(...$args) { }"},{"id":"B","text":"function f($args...) { }"},{"id":"C","text":"function f(*$args) { }"},{"id":"D","text":"不可能"}],
         [0], "関数", "3", 10, "可変引数", "...演算子"),
        
        ("型宣言の書き方は？（PHP 7+）",
         [{"id":"A","text":"function f(int $x): int { }"},{"id":"B","text":"function f($x: int): int { }"},{"id":"C","text":"function f(int $x) -> int { }"},{"id":"D","text":"不可能"}],
         [0], "関数", "3", 10, "型ヒント", "型宣言"),
        
        ("無名関数（クロージャ）の書き方は？",
         [{"id":"A","text":"$f = function() { };"},{"id":"B","text":"$f = () => { };"},{"id":"C","text":"$f = lambda: {};"},{"id":"D","text":"不可能"}],
         [0], "関数", "3", 10, "匿名関数", "クロージャ"),
        
        ("アロー関数の書き方は？（PHP 7.4+）",
         [{"id":"A","text":"fn($x) => $x * 2"},{"id":"B","text":"($x) => $x * 2"},{"id":"C","text":"lambda $x: $x * 2"},{"id":"D","text":"不可能"}],
         [0], "関数", "3", 12, "短縮記法", "アロー関数"),
        
        ("use キーワードの役割（クロージャ）は？",
         [{"id":"A","text":"外部変数を取り込む"},{"id":"B","text":"名前空間"},{"id":"C","text":"継承"},{"id":"D","text":"エラー"}],
         [0], "関数", "4", 12, "変数キャプチャ", "use"),
        
        ("静的変数の宣言は？",
         [{"id":"A","text":"static $var = 0;"},{"id":"B","text":"const $var = 0;"},{"id":"C","text":"global $var = 0;"},{"id":"D","text":"不可能"}],
         [0], "関数", "3", 10, "関数内で値を保持", "static"),
        
        ("可変関数の呼び出し方は？",
         [{"id":"A","text":"$func = 'func_name'; $func();"},{"id":"B","text":"call($func_name);"},{"id":"C","text":"invoke($func_name);"},{"id":"D","text":"不可能"}],
         [0], "関数", "4", 12, "動的関数呼び出し", "可変関数"),
    ]
    
    questions.extend(function_questions)
    print(f"  ✓ 関数: {len(function_questions)}問")
    
    # ==================== 文字列操作（10問） ====================
    print("[3/3] 文字列操作問題を生成中...")
    
    string_questions = [
        ("strlen() の役割は？",
         [{"id":"A","text":"文字列の長さ（バイト数）"},{"id":"B","text":"配列長"},{"id":"C","text":"単語数"},{"id":"D","text":"行数"}],
         [0], "文字列", "1", 5, "文字列長", "strlen"),
        
        ("str_replace() の役割は？",
         [{"id":"A","text":"文字列の置換"},{"id":"B","text":"文字列の検索"},{"id":"C","text":"文字列の分割"},{"id":"D","text":"文字列の結合"}],
         [0], "文字列", "2", 8, "置換", "str_replace"),
        
        ("explode() の役割は？",
         [{"id":"A","text":"文字列を配列に分割"},{"id":"B","text":"配列を文字列に結合"},{"id":"C","text":"置換"},{"id":"D","text":"検索"}],
         [0], "文字列", "2", 8, "分割", "explode"),
        
        ("implode() の役割は？",
         [{"id":"A","text":"配列を文字列に結合"},{"id":"B","text":"文字列を配列に分割"},{"id":"C","text":"置換"},{"id":"D","text":"検索"}],
         [0], "文字列", "2", 8, "結合", "implode"),
        
        ("trim() の役割は？",
         [{"id":"A","text":"前後の空白削除"},{"id":"B","text":"全ての空白削除"},{"id":"C","text":"文字列の一部削除"},{"id":"D","text":"置換"}],
         [0], "文字列", "2", 8, "空白除去", "trim"),
        
        ("strtoupper() の役割は？",
         [{"id":"A","text":"大文字に変換"},{"id":"B","text":"小文字に変換"},{"id":"C","text":"先頭だけ大文字"},{"id":"D","text":"反転"}],
         [0], "文字列", "1", 5, "大文字化", "strtoupper"),
        
        ("substr() の役割は？",
         [{"id":"A","text":"部分文字列の取得"},{"id":"B","text":"文字列の検索"},{"id":"C","text":"置換"},{"id":"D","text":"分割"}],
         [0], "文字列", "2", 8, "部分取得", "substr"),
        
        ("strpos() の役割は？",
         [{"id":"A","text":"文字列の位置を検索"},{"id":"B","text":"文字列の置換"},{"id":"C","text":"文字列の分割"},{"id":"D","text":"文字列の長さ"}],
         [0], "文字列", "2", 8, "位置検索", "strpos"),
        
        ("sprintf() の用途は？",
         [{"id":"A","text":"書式付き文字列生成"},{"id":"B","text":"文字列の分割"},{"id":"C","text":"置換"},{"id":"D","text":"検索"}],
         [0], "文字列", "3", 10, "フォーマット", "sprintf"),
        
        ("mb_strlen() と strlen() の違いは？",
         [{"id":"A","text":"mb_は文字数、strはバイト数"},{"id":"B","text":"同じ"},{"id":"C","text":"mb_が速い"},{"id":"D","text":"mb_は非推奨"}],
         [0], "文字列", "3", 12, "マルチバイト対応", "mb_strlen"),
    ]
    
    questions.extend(string_questions)
    print(f"  ✓ 文字列操作: {len(string_questions)}問")
    
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
        """, ("PHP", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'PHP'")
    php_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ PHP問題追加完了（第2弾）！")
    print("=" * 60)
    print(f"PHP問題数: {php_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標100問まで残り: {max(0, 100 - php_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_php_batch2()