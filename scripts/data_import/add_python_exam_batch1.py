import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_python_exam_batch1():
    """Python試験対策問題追加（第1弾・50問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Python試験対策問題追加スクリプト（第1弾・50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== データ型と演算（15問） ====================
    print("[1/4] データ型と演算問題を生成中...")
    
    datatype_questions = [
        ("type(3.14) の結果は？",
         [{"id":"A","text":"<class 'float'>"},{"id":"B","text":"<class 'int'>"},{"id":"C","text":"<class 'double'>"},{"id":"D","text":"<class 'number'>"}],
         [0], "試験対策_データ型", "2", 8, "浮動小数点型", "型判定"),
        
        ("int('10', 2) の結果は？",
         [{"id":"A","text":"2"},{"id":"B","text":"10"},{"id":"C","text":"エラー"},{"id":"D","text":"8"}],
         [0], "試験対策_データ型", "3", 12, "2進数'10'を10進数に変換→2", "基数変換"),
        
        ("bin(10) の結果は？",
         [{"id":"A","text":"'0b1010'"},{"id":"B","text":"'1010'"},{"id":"C","text":"10"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "3", 10, "10進数を2進数文字列に", "進数変換"),
        
        ("hex(255) の結果は？",
         [{"id":"A","text":"'0xff'"},{"id":"B","text":"'ff'"},{"id":"C","text":"255"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "3", 10, "10進数を16進数文字列に", "16進数"),
        
        ("bool([]) の結果は？",
         [{"id":"A","text":"False"},{"id":"B","text":"True"},{"id":"C","text":"None"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "2", 8, "空のリストはFalsy", "真偽値変換"),
        
        ("10 // 3 の結果は？",
         [{"id":"A","text":"3"},{"id":"B","text":"3.333..."},{"id":"C","text":"4"},{"id":"D","text":"エラー"}],
         [0], "試験対策_演算", "2", 8, "整数除算（切り捨て）", "//演算子"),
        
        ("10 % 3 の結果は？",
         [{"id":"A","text":"1"},{"id":"B","text":"3"},{"id":"C","text":"3.333..."},{"id":"D","text":"エラー"}],
         [0], "試験対策_演算", "1", 5, "剰余（余り）", "%演算子"),
        
        ("2 ** 3 の結果は？",
         [{"id":"A","text":"8"},{"id":"B","text":"6"},{"id":"C","text":"9"},{"id":"D","text":"エラー"}],
         [0], "試験対策_演算", "2", 8, "べき乗（2の3乗）", "**演算子"),
        
        ("round(3.5) の結果は？",
         [{"id":"A","text":"4"},{"id":"B","text":"3"},{"id":"C","text":"3.5"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "3", 10, "偶数丸め（銀行丸め）", "round"),
        
        ("abs(-5) の結果は？",
         [{"id":"A","text":"5"},{"id":"B","text":"-5"},{"id":"C","text":"0"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "1", 5, "絶対値", "abs"),
        
        ("divmod(10, 3) の結果は？",
         [{"id":"A","text":"(3, 1)"},{"id":"B","text":"3"},{"id":"C","text":"1"},{"id":"D","text":"エラー"}],
         [0], "試験対策_演算", "3", 10, "商と余りのタプル", "divmod"),
        
        ("complex(2, 3) の型は？",
         [{"id":"A","text":"complex（複素数）"},{"id":"B","text":"tuple"},{"id":"C","text":"float"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "3", 10, "複素数型", "complex"),
        
        ("None の型は？",
         [{"id":"A","text":"NoneType"},{"id":"B","text":"null"},{"id":"C","text":"None"},{"id":"D","text":"Object"}],
         [0], "試験対策_データ型", "2", 8, "None型", "NoneType"),
        
        ("0.1 + 0.2 == 0.3 の結果は？",
         [{"id":"A","text":"False（浮動小数点誤差）"},{"id":"B","text":"True"},{"id":"C","text":"エラー"},{"id":"D","text":"None"}],
         [0], "試験対策_演算", "4", 15, "浮動小数点の精度問題", "浮動小数点"),
        
        ("isinstance(5, int) の結果は？",
         [{"id":"A","text":"True"},{"id":"B","text":"False"},{"id":"C","text":"int"},{"id":"D","text":"エラー"}],
         [0], "試験対策_データ型", "2", 8, "型チェック", "isinstance"),
    ]
    
    questions.extend(datatype_questions)
    print(f"  ✓ データ型と演算: {len(datatype_questions)}問")
    
    # ==================== アルゴリズム基礎（15問） ====================
    print("[2/4] アルゴリズム基礎問題を生成中...")
    
    algorithm_questions = [
        ("リストをソートするメソッドは？",
         [{"id":"A","text":"sort() と sorted()"},{"id":"B","text":"order()"},{"id":"C","text":"arrange()"},{"id":"D","text":"sequence()"}],
         [0], "試験対策_アルゴリズム", "2", 8, "sort()は破壊的、sorted()は新規", "ソート"),
        
        ("[1,2,3].reverse() と reversed([1,2,3]) の違いは？",
         [{"id":"A","text":"前者は破壊的、後者はイテレータ"},{"id":"B","text":"同じ"},{"id":"C","text":"前者はエラー"},{"id":"D","text":"後者はエラー"}],
         [0], "試験対策_アルゴリズム", "3", 10, "破壊的変更 vs イテレータ", "逆順"),
        
        ("線形探索の計算量は？",
         [{"id":"A","text":"O(n)"},{"id":"B","text":"O(log n)"},{"id":"C","text":"O(n²)"},{"id":"D","text":"O(1)"}],
         [0], "試験対策_アルゴリズム", "3", 12, "要素数に比例", "線形探索"),
        
        ("二分探索の前提条件は？",
         [{"id":"A","text":"ソート済み"},{"id":"B","text":"重複なし"},{"id":"C","text":"数値のみ"},{"id":"D","text":"条件なし"}],
         [0], "試験対策_アルゴリズム", "3", 12, "整列済みデータが必要", "二分探索"),
        
        ("二分探索の計算量は？",
         [{"id":"A","text":"O(log n)"},{"id":"B","text":"O(n)"},{"id":"C","text":"O(n²)"},{"id":"D","text":"O(1)"}],
         [0], "試験対策_アルゴリズム", "3", 12, "対数時間", "計算量"),
        
        ("バブルソートの最悪計算量は？",
         [{"id":"A","text":"O(n²)"},{"id":"B","text":"O(n log n)"},{"id":"C","text":"O(n)"},{"id":"D","text":"O(1)"}],
         [0], "試験対策_アルゴリズム", "4", 15, "2重ループ", "バブルソート"),
        
        ("再帰関数の特徴は？",
         [{"id":"A","text":"自分自身を呼び出す"},{"id":"B","text":"ループを使う"},{"id":"C","text":"高速"},{"id":"D","text":"エラーが出ない"}],
         [0], "試験対策_アルゴリズム", "2", 8, "自己参照", "再帰"),
        
        ("スタックの操作は？",
         [{"id":"A","text":"LIFO（後入れ先出し）"},{"id":"B","text":"FIFO（先入れ先出し）"},{"id":"C","text":"ランダム"},{"id":"D","text":"ソート"}],
         [0], "試験対策_データ構造", "3", 10, "Last In First Out", "スタック"),
        
        ("キューの操作は？",
         [{"id":"A","text":"FIFO（先入れ先出し）"},{"id":"B","text":"LIFO（後入れ先出し）"},{"id":"C","text":"ランダム"},{"id":"D","text":"ソート"}],
         [0], "試験対策_データ構造", "3", 10, "First In First Out", "キュー"),
        
        ("ハッシュテーブルの平均検索時間は？",
         [{"id":"A","text":"O(1)"},{"id":"B","text":"O(n)"},{"id":"C","text":"O(log n)"},{"id":"D","text":"O(n²)"}],
         [0], "試験対策_データ構造", "4", 15, "定数時間", "ハッシュ"),
        
        ("collections.deque の特徴は？",
         [{"id":"A","text":"両端操作が高速"},{"id":"B","text":"ソート済み"},{"id":"C","text":"重複なし"},{"id":"D","text":"不変"}],
         [0], "試験対策_データ構造", "3", 12, "両端キュー", "deque"),
        
        ("heapq モジュールの用途は？",
         [{"id":"A","text":"優先度付きキュー"},{"id":"B","text":"スタック"},{"id":"C","text":"ソート"},{"id":"D","text":"検索"}],
         [0], "試験対策_データ構造", "4", 15, "ヒープ（優先度キュー）", "heap"),
        
        ("動的計画法の特徴は？",
         [{"id":"A","text":"部分問題の結果を記憶"},{"id":"B","text":"再帰のみ"},{"id":"C","text":"貪欲法"},{"id":"D","text":"全探索"}],
         [0], "試験対策_アルゴリズム", "5", 18, "メモ化で効率化", "DP"),
        
        ("貪欲法（greedy）の特徴は？",
         [{"id":"A","text":"その時点で最良の選択"},{"id":"B","text":"全探索"},{"id":"C","text":"最適解保証"},{"id":"D","text":"バックトラック"}],
         [0], "試験対策_アルゴリズム", "4", 15, "局所最適を選択", "greedy"),
        
        ("in演算子でリスト検索の計算量は？",
         [{"id":"A","text":"O(n)"},{"id":"B","text":"O(1)"},{"id":"C","text":"O(log n)"},{"id":"D","text":"O(n²)"}],
         [0], "試験対策_アルゴリズム", "3", 12, "線形探索", "検索計算量"),
    ]
    
    questions.extend(algorithm_questions)
    print(f"  ✓ アルゴリズム基礎: {len(algorithm_questions)}問")
    
    # ==================== 標準ライブラリ応用（10問） ====================
    print("[3/4] 標準ライブラリ応用問題を生成中...")
    
    stdlib_advanced = [
        ("sys.argv の用途は？",
         [{"id":"A","text":"コマンドライン引数取得"},{"id":"B","text":"環境変数"},{"id":"C","text":"システム情報"},{"id":"D","text":"エラー情報"}],
         [0], "試験対策_標準ライブラリ", "3", 10, "プログラム引数のリスト", "sys.argv"),
        
        ("os.environ の用途は？",
         [{"id":"A","text":"環境変数の取得・設定"},{"id":"B","text":"コマンド実行"},{"id":"C","text":"ファイル操作"},{"id":"D","text":"プロセス管理"}],
         [0], "試験対策_標準ライブラリ", "3", 10, "環境変数辞書", "os.environ"),
        
        ("pathlib.Path の利点は？",
         [{"id":"A","text":"オブジェクト指向でパス操作"},{"id":"B","text":"高速"},{"id":"C","text":"後方互換性"},{"id":"D","text":"メモリ効率"}],
         [0], "試験対策_標準ライブラリ", "3", 12, "モダンなパス操作", "pathlib"),
        
        ("subprocess.run() の用途は？",
         [{"id":"A","text":"外部コマンド実行"},{"id":"B","text":"スレッド起動"},{"id":"C","text":"非同期処理"},{"id":"D","text":"ファイル実行"}],
         [0], "試験対策_標準ライブラリ", "4", 15, "サブプロセス管理", "subprocess"),
        
        ("logging モジュールのレベルで最も重要度が高いのは？",
         [{"id":"A","text":"CRITICAL"},{"id":"B","text":"ERROR"},{"id":"C","text":"WARNING"},{"id":"D","text":"INFO"}],
         [0], "試験対策_標準ライブラリ", "3", 10, "重大なエラー", "logging"),
        
        ("argparse の用途は？",
         [{"id":"A","text":"コマンドライン引数のパース"},{"id":"B","text":"JSON解析"},{"id":"C","text":"正規表現"},{"id":"D","text":"数値計算"}],
         [0], "試験対策_標準ライブラリ", "3", 12, "CLI引数パーサ", "argparse"),
        
        ("unittest の役割は？",
         [{"id":"A","text":"単体テストフレームワーク"},{"id":"B","text":"統合テスト"},{"id":"C","text":"負荷テスト"},{"id":"D","text":"デバッガ"}],
         [0], "試験対策_標準ライブラリ", "3", 10, "テストケース管理", "unittest"),
        
        ("csv.reader() の用途は？",
         [{"id":"A","text":"CSVファイルの読み込み"},{"id":"B","text":"JSONファイル読み込み"},{"id":"C","text":"XMLファイル読み込み"},{"id":"D","text":"バイナリ読み込み"}],
         [0], "試験対策_標準ライブラリ", "2", 8, "CSV解析", "csv"),
        
        ("urllib.request の用途は？",
         [{"id":"A","text":"HTTP通信"},{"id":"B","text":"ファイル操作"},{"id":"C","text":"データベース接続"},{"id":"D","text":"暗号化"}],
         [0], "試験対策_標準ライブラリ", "3", 10, "URLからデータ取得", "urllib"),
        
        ("hashlib.sha256() の用途は？",
         [{"id":"A","text":"SHA-256ハッシュ生成"},{"id":"B","text":"暗号化"},{"id":"C","text":"圧縮"},{"id":"D","text":"復号化"}],
         [0], "試験対策_標準ライブラリ", "4", 12, "ハッシュ関数", "hashlib"),
    ]
    
    questions.extend(stdlib_advanced)
    print(f"  ✓ 標準ライブラリ応用: {len(stdlib_advanced)}問")
    
    # ==================== プログラミング実践（10問） ====================
    print("[4/4] プログラミング実践問題を生成中...")
    
    practice_questions = [
        ("PEP 8 は何の規約？",
         [{"id":"A","text":"Pythonコーディング規約"},{"id":"B","text":"パッケージ管理"},{"id":"C","text":"テスト規約"},{"id":"D","text":"セキュリティ"}],
         [0], "試験対策_実践", "2", 8, "スタイルガイド", "PEP8"),
        
        ("snake_case が推奨されるのは？",
         [{"id":"A","text":"関数名・変数名"},{"id":"B","text":"クラス名"},{"id":"C","text":"定数"},{"id":"D","text":"モジュール名"}],
         [0], "試験対策_実践", "2", 8, "小文字とアンダースコア", "命名規則"),
        
        ("UPPER_CASE が推奨されるのは？",
         [{"id":"A","text":"定数"},{"id":"B","text":"関数名"},{"id":"C","text":"変数名"},{"id":"D","text":"クラス名"}],
         [0], "試験対策_実践", "2", 8, "全て大文字", "定数命名"),
        
        ("docstring の書き方は？",
         [{"id":"A","text":"\"\"\"三重クォート\"\"\""},{"id":"B","text":"# コメント"},{"id":"C","text":"/* */"},{"id":"D","text":"// コメント"}],
         [0], "試験対策_実践", "2", 8, "関数・クラスの説明", "docstring"),
        
        ("type hinting (型ヒント) の書き方は？",
         [{"id":"A","text":"def f(x: int) -> int:"},{"id":"B","text":"def f(int x) -> int:"},{"id":"C","text":"def f(x) -> int:"},{"id":"D","text":"def f<int>(x):"}],
         [0], "試験対策_実践", "3", 10, "型注釈", "type hint"),
        
        ("仮想環境（venv）の用途は？",
         [{"id":"A","text":"プロジェクト毎の独立環境"},{"id":"B","text":"高速化"},{"id":"C","text":"デバッグ"},{"id":"D","text":"暗号化"}],
         [0], "試験対策_実践", "3", 10, "依存関係の分離", "venv"),
        
        ("pip の役割は？",
         [{"id":"A","text":"パッケージ管理"},{"id":"B","text":"実行"},{"id":"C","text":"デバッグ"},{"id":"D","text":"コンパイル"}],
         [0], "試験対策_実践", "2", 8, "Pythonパッケージインストーラ", "pip"),
        
        ("requirements.txt の用途は？",
         [{"id":"A","text":"依存パッケージ一覧"},{"id":"B","text":"設定ファイル"},{"id":"C","text":"ログ"},{"id":"D","text":"ドキュメント"}],
         [0], "試験対策_実践", "3", 10, "パッケージバージョン管理", "requirements"),
        
        ("__pycache__ の役割は？",
         [{"id":"A","text":"バイトコードキャッシュ"},{"id":"B","text":"ログ保存"},{"id":"C","text":"設定保存"},{"id":"D","text":"エラー情報"}],
         [0], "試験対策_実践", "3", 10, "コンパイル済みファイル", "pycache"),
        
        ("if __name__ == '__main__': の意味は？",
         [{"id":"A","text":"直接実行時のみ実行"},{"id":"B","text":"必須の構文"},{"id":"C","text":"エラーチェック"},{"id":"D","text":"デバッグモード"}],
         [0], "試験対策_実践", "2", 8, "スクリプト直接実行判定", "main"),
    ]
    
    questions.extend(practice_questions)
    print(f"  ✓ プログラミング実践: {len(practice_questions)}問")
    
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
    
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'Python' AND category LIKE '試験対策%'")
    exam_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ Python試験対策問題追加完了（第1弾）！")
    print("=" * 60)
    print(f"Python全問題数: {py_count}問")
    print(f"  うち試験対策: {exam_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"試験対策目標200問まで残り: {max(0, 200 - exam_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_python_exam_batch1()