import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_python_batch1():
    """Python問題追加（第1弾・30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Python問題追加スクリプト（第1弾・30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== 制御構文（10問） ====================
    print("[1/3] 制御構文問題を生成中...")
    
    control_questions = [
        ("if x > 0: の行末のコロン(:)は？",
         [{"id":"A","text":"必須"},{"id":"B","text":"省略可"},{"id":"C","text":"非推奨"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "1", 5, "Pythonの構文規則", "if文"),
        
        ("for i in range(3): の実行回数は？",
         [{"id":"A","text":"3回"},{"id":"B","text":"2回"},{"id":"C","text":"4回"},{"id":"D","text":"無限"}],
         [0], "制御構文", "1", 5, "range(3)は0,1,2", "forループ"),
        
        ("while True: の動作は？",
         [{"id":"A","text":"無限ループ"},{"id":"B","text":"1回実行"},{"id":"C","text":"実行しない"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "1", 5, "条件が常に真", "whileループ"),
        
        ("break文の役割は？",
         [{"id":"A","text":"ループを抜ける"},{"id":"B","text":"次の反復へ"},{"id":"C","text":"関数終了"},{"id":"D","text":"エラー発生"}],
         [0], "制御構文", "1", 5, "ループを中断", "break"),
        
        ("continue文の役割は？",
         [{"id":"A","text":"次の反復へ進む"},{"id":"B","text":"ループを抜ける"},{"id":"C","text":"関数終了"},{"id":"D","text":"待機"}],
         [0], "制御構文", "2", 8, "現在の反復をスキップ", "continue"),
        
        ("else節がfor/whileループにも使える？",
         [{"id":"A","text":"使える"},{"id":"B","text":"使えない"},{"id":"C","text":"whileのみ"},{"id":"D","text":"forのみ"}],
         [0], "制御構文", "3", 10, "ループが正常終了時に実行", "loop-else"),
        
        ("pass文の役割は？",
         [{"id":"A","text":"何もしない"},{"id":"B","text":"終了"},{"id":"C","text":"待機"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "2", 8, "空のコードブロック", "pass"),
        
        ("if x == 5: と if x = 5: の違いは？",
         [{"id":"A","text":"==が比較、=が代入（エラー）"},{"id":"B","text":"同じ"},{"id":"C","text":"速度が違う"},{"id":"D","text":"どちらも可"}],
         [0], "制御構文", "1", 5, "比較演算子と代入演算子", "演算子"),
        
        ("match-case文（Python 3.10+）の用途は？",
         [{"id":"A","text":"パターンマッチング"},{"id":"B","text":"ループ"},{"id":"C","text":"エラー処理"},{"id":"D","text":"非推奨"}],
         [0], "制御構文", "3", 10, "構造化パターンマッチング", "match-case"),
        
        ("elif は何の略？",
         [{"id":"A","text":"else if"},{"id":"B","text":"elif"},{"id":"C","text":"else-if"},{"id":"D","text":"略ではない"}],
         [0], "制御構文", "1", 5, "else ifの短縮形", "elif"),
    ]
    
    questions.extend(control_questions)
    print(f"  ✓ 制御構文: {len(control_questions)}問")
    
    # ==================== 関数とスコープ（10問） ====================
    print("[2/3] 関数とスコープ問題を生成中...")
    
    function_questions = [
        ("def func(): の後のインデントは？",
         [{"id":"A","text":"必須"},{"id":"B","text":"省略可"},{"id":"C","text":"タブのみ"},{"id":"D","text":"スペースのみ"}],
         [0], "関数", "1", 5, "Pythonのインデント規則", "インデント"),
        
        ("関数の返り値を返すキーワードは？",
         [{"id":"A","text":"return"},{"id":"B","text":"output"},{"id":"C","text":"result"},{"id":"D","text":"yield"}],
         [0], "関数", "1", 5, "値を返す", "return"),
        
        ("def f(x=1): のx=1は？",
         [{"id":"A","text":"デフォルト引数"},{"id":"B","text":"必須引数"},{"id":"C","text":"エラー"},{"id":"D","text":"型指定"}],
         [0], "関数", "2", 8, "引数のデフォルト値", "デフォルト引数"),
        
        ("*args の役割は？",
         [{"id":"A","text":"可変長位置引数"},{"id":"B","text":"必須引数"},{"id":"C","text":"キーワード引数"},{"id":"D","text":"エラー"}],
         [0], "関数", "3", 10, "任意個の位置引数を受け取る", "*args"),
        
        ("**kwargs の役割は？",
         [{"id":"A","text":"可変長キーワード引数"},{"id":"B","text":"必須引数"},{"id":"C","text":"位置引数"},{"id":"D","text":"エラー"}],
         [0], "関数", "3", 10, "任意個のキーワード引数を辞書で受け取る", "**kwargs"),
        
        ("lambda x: x * 2 は何？",
         [{"id":"A","text":"無名関数"},{"id":"B","text":"通常の関数"},{"id":"C","text":"クラス"},{"id":"D","text":"エラー"}],
         [0], "関数", "2", 8, "1行で書ける無名関数", "lambda"),
        
        ("global キーワードの役割は？",
         [{"id":"A","text":"グローバル変数を変更"},{"id":"B","text":"ローカル変数作成"},{"id":"C","text":"定数宣言"},{"id":"D","text":"エラー"}],
         [0], "スコープ", "3", 10, "関数内でグローバル変数を参照", "global"),
        
        ("nonlocal キーワードの役割は？",
         [{"id":"A","text":"外側の関数の変数を変更"},{"id":"B","text":"グローバル変数参照"},{"id":"C","text":"ローカル変数作成"},{"id":"D","text":"エラー"}],
         [0], "スコープ", "4", 12, "ネストした関数のスコープ", "nonlocal"),
        
        ("関数内で定義した変数のスコープは？",
         [{"id":"A","text":"ローカルスコープ"},{"id":"B","text":"グローバルスコープ"},{"id":"C","text":"モジュールスコープ"},{"id":"D","text":"全体"}],
         [0], "スコープ", "2", 8, "関数内のみで有効", "ローカル変数"),
        
        ("デコレータ @decorator の役割は？",
         [{"id":"A","text":"関数を装飾・拡張"},{"id":"B","text":"コメント"},{"id":"C","text":"型指定"},{"id":"D","text":"エラー"}],
         [0], "関数", "4", 15, "関数の前後に処理を追加", "デコレータ"),
    ]
    
    questions.extend(function_questions)
    print(f"  ✓ 関数とスコープ: {len(function_questions)}問")
    
    # ==================== クラスとオブジェクト指向（10問） ====================
    print("[3/3] クラスとオブジェクト指向問題を生成中...")
    
    class_questions = [
        ("class MyClass: でクラスを定義する際の慣例は？",
         [{"id":"A","text":"CapitalCase（大文字始まり）"},{"id":"B","text":"snake_case"},{"id":"C","text":"camelCase"},{"id":"D","text":"全て小文字"}],
         [0], "クラス", "1", 5, "クラス名はパスカルケース", "命名規則"),
        
        ("__init__ メソッドの役割は？",
         [{"id":"A","text":"コンストラクタ（初期化）"},{"id":"B","text":"デストラクタ"},{"id":"C","text":"文字列化"},{"id":"D","text":"比較"}],
         [0], "クラス", "2", 8, "インスタンス生成時に呼ばれる", "__init__"),
        
        ("self の意味は？",
         [{"id":"A","text":"インスタンス自身"},{"id":"B","text":"クラス自身"},{"id":"C","text":"親クラス"},{"id":"D","text":"キーワード"}],
         [0], "クラス", "2", 8, "インスタンスメソッドの第一引数", "self"),
        
        ("クラス継承の書き方は？",
         [{"id":"A","text":"class Child(Parent):"},{"id":"B","text":"class Child extends Parent:"},{"id":"C","text":"class Child -> Parent:"},{"id":"D","text":"class Child : Parent"}],
         [0], "クラス", "2", 8, "括弧内に親クラスを指定", "継承"),
        
        ("super() の役割は？",
         [{"id":"A","text":"親クラスのメソッド呼び出し"},{"id":"B","text":"インスタンス生成"},{"id":"C","text":"削除"},{"id":"D","text":"コピー"}],
         [0], "クラス", "3", 10, "親クラスへのアクセス", "super"),
        
        ("プライベート変数の慣例は？",
         [{"id":"A","text":"__var（アンダースコア2つ）"},{"id":"B","text":"private var"},{"id":"C","text":"_var（1つ）"},{"id":"D","text":"var_"}],
         [0], "クラス", "3", 10, "名前マングリング", "プライベート変数"),
        
        ("@staticmethod の役割は？",
         [{"id":"A","text":"クラスと独立したメソッド"},{"id":"B","text":"インスタンスメソッド"},{"id":"C","text":"クラスメソッド"},{"id":"D","text":"エラー"}],
         [0], "クラス", "3", 12, "selfもclsも不要", "staticmethod"),
        
        ("@classmethod の第一引数は？",
         [{"id":"A","text":"cls（クラス自身）"},{"id":"B","text":"self"},{"id":"C","text":"なし"},{"id":"D","text":"parent"}],
         [0], "クラス", "3", 12, "クラスを受け取る", "classmethod"),
        
        ("__str__ メソッドの役割は？",
         [{"id":"A","text":"print()時の文字列表現"},{"id":"B","text":"初期化"},{"id":"C","text":"比較"},{"id":"D","text":"削除"}],
         [0], "クラス", "2", 8, "人間向けの文字列化", "__str__"),
        
        ("多重継承は可能？",
         [{"id":"A","text":"可能"},{"id":"B","text":"不可能"},{"id":"C","text":"2つまで"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "4", 15, "複数の親クラスを継承可能", "多重継承"),
    ]
    
    questions.extend(class_questions)
    print(f"  ✓ クラスとオブジェクト指向: {len(class_questions)}問")
    
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
        """, ("Python", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'Python'")
    py_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ Python問題追加完了（第1弾）！")
    print("=" * 60)
    print(f"Python問題数: {py_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標100問まで残り: {max(0, 100 - py_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_python_batch1()