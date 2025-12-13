import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_python_exam_batch2():
    """Python試験対策問題追加（第2弾・50問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Python試験対策問題追加スクリプト（第2弾・50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== オブジェクト指向プログラミング（15問） ====================
    print("[1/4] オブジェクト指向プログラミング問題を生成中...")
    
    oop_questions = [
        ("カプセル化の目的は？",
         [{"id":"A","text":"データと操作を一体化"},{"id":"B","text":"高速化"},{"id":"C","text":"メモリ節約"},{"id":"D","text":"エラー防止のみ"}],
         [0], "試験対策_OOP", "3", 10, "情報隠蔽と保護", "カプセル化"),
        
        ("継承の利点は？",
         [{"id":"A","text":"コードの再利用"},{"id":"B","text":"高速化"},{"id":"C","text":"メモリ節約"},{"id":"D","text":"必須機能"}],
         [0], "試験対策_OOP", "2", 8, "既存クラスを拡張", "継承"),
        
        ("ポリモーフィズムとは？",
         [{"id":"A","text":"同じメソッド名で異なる動作"},{"id":"B","text":"多重継承"},{"id":"C","text":"型変換"},{"id":"D","text":"並列処理"}],
         [0], "試験対策_OOP", "4", 12, "多態性", "ポリモーフィズム"),
        
        ("抽象クラスの特徴は？",
         [{"id":"A","text":"インスタンス化できない"},{"id":"B","text":"継承できない"},{"id":"C","text":"メソッドなし"},{"id":"D","text":"高速"}],
         [0], "試験対策_OOP", "4", 15, "ABCで定義", "抽象クラス"),
        
        ("from abc import ABC, abstractmethod の用途は？",
         [{"id":"A","text":"抽象クラス定義"},{"id":"B","text":"インターフェース"},{"id":"C","text":"型定義"},{"id":"D","text":"デコレータ"}],
         [0], "試験対策_OOP", "4", 15, "抽象基底クラス", "ABC"),
        
        ("@property デコレータの役割は？",
         [{"id":"A","text":"ゲッターメソッド定義"},{"id":"B","text":"静的メソッド"},{"id":"C","text":"クラスメソッド"},{"id":"D","text":"初期化"}],
         [0], "試験対策_OOP", "3", 12, "属性アクセスをメソッド化", "property"),
        
        ("@setter の役割は？",
         [{"id":"A","text":"セッターメソッド定義"},{"id":"B","text":"ゲッター"},{"id":"C","text":"削除"},{"id":"D","text":"初期化"}],
         [0], "試験対策_OOP", "3", 12, "属性の設定を制御", "setter"),
        
        ("__new__ メソッドの役割は？",
         [{"id":"A","text":"インスタンス生成"},{"id":"B","text":"初期化"},{"id":"C","text":"削除"},{"id":"D","text":"コピー"}],
         [0], "試験対策_OOP", "4", 15, "__init__より前に呼ばれる", "__new__"),
        
        ("__del__ メソッドの役割は？",
         [{"id":"A","text":"デストラクタ（削除時）"},{"id":"B","text":"初期化"},{"id":"C","text":"コピー"},{"id":"D","text":"比較"}],
         [0], "試験対策_OOP", "3", 10, "オブジェクト削除時", "__del__"),
        
        ("__repr__ と __str__ の違いは？",
         [{"id":"A","text":"__repr__は開発者向け"},{"id":"B","text":"同じ"},{"id":"C","text":"__str__は必須"},{"id":"D","text":"__repr__は非推奨"}],
         [0], "試験対策_OOP", "3", 12, "__repr__は明示的、__str__は可読性", "文字列化"),
        
        ("__eq__ メソッドの役割は？",
         [{"id":"A","text":"==演算子の動作定義"},{"id":"B","text":"<演算子"},{"id":"C","text":"代入"},{"id":"D","text":"型チェック"}],
         [0], "試験対策_OOP", "3", 10, "等価性比較", "__eq__"),
        
        ("__len__ メソッドの役割は？",
         [{"id":"A","text":"len()関数の動作定義"},{"id":"B","text":"サイズ制限"},{"id":"C","text":"カウント"},{"id":"D","text":"型変換"}],
         [0], "試験対策_OOP", "2", 8, "長さを返す", "__len__"),
        
        ("__getitem__ メソッドの役割は？",
         [{"id":"A","text":"obj[key]の動作定義"},{"id":"B","text":"属性取得"},{"id":"C","text":"メソッド呼び出し"},{"id":"D","text":"初期化"}],
         [0], "試験対策_OOP", "3", 12, "インデックスアクセス", "__getitem__"),
        
        ("__iter__ メソッドの役割は？",
         [{"id":"A","text":"イテレータを返す"},{"id":"B","text":"次の要素"},{"id":"C","text":"初期化"},{"id":"D","text":"終了"}],
         [0], "試験対策_OOP", "3", 12, "for文で使えるようにする", "__iter__"),
        
        ("__call__ メソッドの役割は？",
         [{"id":"A","text":"obj()で呼び出し可能に"},{"id":"B","text":"初期化"},{"id":"C","text":"削除"},{"id":"D","text":"コピー"}],
         [0], "試験対策_OOP", "4", 15, "関数のように使える", "__call__"),
    ]
    
    questions.extend(oop_questions)
    print(f"  ✓ オブジェクト指向: {len(oop_questions)}問")
    
    # ==================== ジェネレータとイテレータ（15問） ====================
    print("[2/4] ジェネレータとイテレータ問題を生成中...")
    
    generator_questions = [
        ("yield キーワードの役割は？",
         [{"id":"A","text":"ジェネレータ関数を作る"},{"id":"B","text":"return と同じ"},{"id":"C","text":"例外発生"},{"id":"D","text":"ループ"}],
         [0], "試験対策_ジェネレータ", "3", 10, "値を生成して一時停止", "yield"),
        
        ("ジェネレータの利点は？",
         [{"id":"A","text":"メモリ効率が良い"},{"id":"B","text":"高速"},{"id":"C","text":"並列処理"},{"id":"D","text":"型安全"}],
         [0], "試験対策_ジェネレータ", "3", 12, "遅延評価でメモリ節約", "メモリ効率"),
        
        ("(x**2 for x in range(10)) は？",
         [{"id":"A","text":"ジェネレータ式"},{"id":"B","text":"リスト内包表記"},{"id":"C","text":"タプル"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "2", 8, "括弧で囲むとジェネレータ", "generator expression"),
        
        ("next() 関数の役割は？",
         [{"id":"A","text":"イテレータの次の値取得"},{"id":"B","text":"リストの次"},{"id":"C","text":"ループ"},{"id":"D","text":"カウント"}],
         [0], "試験対策_ジェネレータ", "2", 8, "イテレータプロトコル", "next"),
        
        ("StopIteration 例外が発生するのは？",
         [{"id":"A","text":"イテレータの終端"},{"id":"B","text":"エラー"},{"id":"C","text":"キャンセル"},{"id":"D","text":"中断"}],
         [0], "試験対策_ジェネレータ", "3", 10, "next()で要素がない時", "StopIteration"),
        
        ("itertools.islice(range(10), 5) の結果は？",
         [{"id":"A","text":"最初の5要素"},{"id":"B","text":"5番目の要素"},{"id":"C","text":"5を除く要素"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "3", 12, "スライスのイテレータ版", "islice"),
        
        ("itertools.cycle([1,2,3]) の動作は？",
         [{"id":"A","text":"無限に繰り返す"},{"id":"B","text":"3回繰り返す"},{"id":"C","text":"1回のみ"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "3", 10, "無限イテレータ", "cycle"),
        
        ("itertools.count(start=0) の動作は？",
         [{"id":"A","text":"0から無限にカウント"},{"id":"B","text":"0を返す"},{"id":"C","text":"10まで"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "3", 10, "無限カウンタ", "count"),
        
        ("itertools.combinations([1,2,3], 2) の役割は？",
         [{"id":"A","text":"2個の組み合わせ"},{"id":"B","text":"2個の順列"},{"id":"C","text":"2倍"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "3", 12, "組み合わせ生成", "combinations"),
        
        ("itertools.permutations([1,2], 2) の役割は？",
         [{"id":"A","text":"2個の順列"},{"id":"B","text":"2個の組み合わせ"},{"id":"C","text":"2倍"},{"id":"D","text":"エラー"}],
         [0], "試験対策_ジェネレータ", "3", 12, "順列生成", "permutations"),
        
        ("zip_longest の特徴は？",
         [{"id":"A","text":"長い方に合わせる"},{"id":"B","text":"短い方に合わせる"},{"id":"C","text":"エラー"},{"id":"D","text":"通常のzip"}],
         [0], "試験対策_ジェネレータ", "3", 10, "fillvalueで埋める", "zip_longest"),
        
        ("yield from の役割は？",
         [{"id":"A","text":"サブジェネレータに委譲"},{"id":"B","text":"return"},{"id":"C","text":"例外"},{"id":"D","text":"ループ"}],
         [0], "試験対策_ジェネレータ", "4", 15, "別のイテラブルから生成", "yield from"),
        
        ("send() メソッドの役割は？",
         [{"id":"A","text":"ジェネレータに値を送る"},{"id":"B","text":"値を受け取る"},{"id":"C","text":"停止"},{"id":"D","text":"初期化"}],
         [0], "試験対策_ジェネレータ", "5", 18, "双方向通信", "send"),
        
        ("close() メソッドの役割は？",
         [{"id":"A","text":"ジェネレータを終了"},{"id":"B","text":"一時停止"},{"id":"C","text":"初期化"},{"id":"D","text":"値を返す"}],
         [0], "試験対策_ジェネレータ", "4", 12, "GeneratorExitを発生", "close"),
        
        ("throw() メソッドの役割は？",
         [{"id":"A","text":"ジェネレータに例外を送る"},{"id":"B","text":"エラーログ"},{"id":"C","text":"停止"},{"id":"D","text":"初期化"}],
         [0], "試験対策_ジェネレータ", "5", 18, "例外を注入", "throw"),
    ]
    
    questions.extend(generator_questions)
    print(f"  ✓ ジェネレータとイテレータ: {len(generator_questions)}問")
    
    # ==================== 並行処理とマルチスレッド（10問） ====================
    print("[3/4] 並行処理とマルチスレッド問題を生成中...")
    
    concurrent_questions = [
        ("threading モジュールの用途は？",
         [{"id":"A","text":"スレッド並行処理"},{"id":"B","text":"プロセス並行処理"},{"id":"C","text":"非同期処理"},{"id":"D","text":"順次処理"}],
         [0], "試験対策_並行処理", "4", 12, "マルチスレッド", "threading"),
        
        ("multiprocessing モジュールの特徴は？",
         [{"id":"A","text":"プロセス並列実行"},{"id":"B","text":"スレッド並行"},{"id":"C","text":"非同期"},{"id":"D","text":"順次処理"}],
         [0], "試験対策_並行処理", "4", 15, "GILを回避", "multiprocessing"),
        
        ("GIL (Global Interpreter Lock) とは？",
         [{"id":"A","text":"1スレッドのみPython実行"},{"id":"B","text":"複数スレッド実行"},{"id":"C","text":"プロセス制限"},{"id":"D","text":"メモリロック"}],
         [0], "試験対策_並行処理", "5", 18, "CPythonの制約", "GIL"),
        
        ("asyncio の用途は？",
         [{"id":"A","text":"非同期I/O処理"},{"id":"B","text":"マルチスレッド"},{"id":"C","text":"マルチプロセス"},{"id":"D","text":"順次処理"}],
         [0], "試験対策_並行処理", "4", 15, "async/awaitベース", "asyncio"),
        
        ("async def の役割は？",
         [{"id":"A","text":"コルーチン定義"},{"id":"B","text":"スレッド"},{"id":"C","text":"プロセス"},{"id":"D","text":"通常の関数"}],
         [0], "試験対策_並行処理", "4", 12, "非同期関数", "async def"),
        
        ("await の使用場所は？",
         [{"id":"A","text":"async関数内"},{"id":"B","text":"どこでも"},{"id":"C","text":"通常の関数"},{"id":"D","text":"クラス"}],
         [0], "試験対策_並行処理", "3", 10, "コルーチン内でのみ", "await"),
        
        ("threading.Lock() の役割は？",
         [{"id":"A","text":"排他制御"},{"id":"B","text":"スレッド生成"},{"id":"C","text":"待機"},{"id":"D","text":"停止"}],
         [0], "試験対策_並行処理", "4", 15, "共有リソース保護", "Lock"),
        
        ("Queue の特徴は？",
         [{"id":"A","text":"スレッドセーフ"},{"id":"B","text":"高速"},{"id":"C","text":"軽量"},{"id":"D","text":"無限"}],
         [0], "試験対策_並行処理", "4", 12, "スレッド間通信", "Queue"),
        
        ("concurrent.futures.ThreadPoolExecutor の用途は？",
         [{"id":"A","text":"スレッドプール管理"},{"id":"B","text":"プロセスプール"},{"id":"C","text":"非同期"},{"id":"D","text":"順次実行"}],
         [0], "試験対策_並行処理", "4", 15, "スレッド再利用", "ThreadPoolExecutor"),
        
        ("concurrent.futures.ProcessPoolExecutor の利点は？",
         [{"id":"A","text":"CPU並列処理"},{"id":"B","text":"I/O処理"},{"id":"C","text":"メモリ節約"},{"id":"D","text":"高速起動"}],
         [0], "試験対策_並行処理", "4", 15, "CPU集約的処理向け", "ProcessPoolExecutor"),
    ]
    
    questions.extend(concurrent_questions)
    print(f"  ✓ 並行処理: {len(concurrent_questions)}問")
    
    # ==================== パフォーマンスと最適化（10問） ====================
    print("[4/4] パフォーマンスと最適化問題を生成中...")
    
    performance_questions = [
        ("timeit モジュールの用途は？",
         [{"id":"A","text":"実行時間計測"},{"id":"B","text":"メモリ計測"},{"id":"C","text":"CPU使用率"},{"id":"D","text":"デバッグ"}],
         [0], "試験対策_パフォーマンス", "3", 10, "コードベンチマーク", "timeit"),
        
        ("cProfile の用途は？",
         [{"id":"A","text":"プロファイリング"},{"id":"B","text":"デバッグ"},{"id":"C","text":"テスト"},{"id":"D","text":"ログ"}],
         [0], "試験対策_パフォーマンス", "4", 12, "実行時間解析", "cProfile"),
        
        ("メモリ使用量を減らすには？",
         [{"id":"A","text":"ジェネレータ使用"},{"id":"B","text":"リスト多用"},{"id":"C","text":"グローバル変数"},{"id":"D","text":"コピー増やす"}],
         [0], "試験対策_パフォーマンス", "3", 10, "遅延評価", "最適化"),
        
        ("__slots__ の効果は？",
         [{"id":"A","text":"メモリ使用量削減"},{"id":"B","text":"高速化"},{"id":"C","text":"型安全"},{"id":"D","text":"必須機能"}],
         [0], "試験対策_パフォーマンス", "4", 15, "辞書を使わない", "__slots__"),
        
        ("リスト内包表記 vs map() の違いは？",
         [{"id":"A","text":"内包表記が読みやすい"},{"id":"B","text":"map()が速い"},{"id":"C","text":"同じ"},{"id":"D","text":"map()は非推奨"}],
         [0], "試験対策_パフォーマンス", "3", 10, "Pythonicな書き方", "スタイル"),
        
        ("functools.lru_cache の役割は？",
         [{"id":"A","text":"関数結果をキャッシュ"},{"id":"B","text":"メモリ解放"},{"id":"C","text":"ログ"},{"id":"D","text":"デバッグ"}],
         [0], "試験対策_パフォーマンス", "4", 15, "メモ化", "lru_cache"),
        
        ("dis モジュールの用途は？",
         [{"id":"A","text":"バイトコード逆アセンブル"},{"id":"B","text":"デバッグ"},{"id":"C","text":"テスト"},{"id":"D","text":"ログ"}],
         [0], "試験対策_パフォーマンス", "5", 18, "内部動作確認", "dis"),
        
        ("sys.getsizeof() の役割は？",
         [{"id":"A","text":"オブジェクトのバイト数"},{"id":"B","text":"配列長"},{"id":"C","text":"文字数"},{"id":"D","text":"行数"}],
         [0], "試験対策_パフォーマンス", "3", 10, "メモリサイズ取得", "getsizeof"),
        
        ("gc モジュールの役割は？",
         [{"id":"A","text":"ガベージコレクション制御"},{"id":"B","text":"メモリ確保"},{"id":"C","text":"キャッシュ"},{"id":"D","text":"ログ"}],
         [0], "試験対策_パフォーマンス", "4", 12, "メモリ管理", "gc"),
        
        ("weakref の用途は？",
         [{"id":"A","text":"弱参照でメモリリーク防止"},{"id":"B","text":"強参照"},{"id":"C","text":"コピー"},{"id":"D","text":"キャッシュ"}],
         [0], "試験対策_パフォーマンス", "5", 18, "循環参照回避", "weakref"),
    ]
    
    questions.extend(performance_questions)
    print(f"  ✓ パフォーマンスと最適化: {len(performance_questions)}問")
    
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
    print("✓ Python試験対策問題追加完了（第2弾）！")
    print("=" * 60)
    print(f"Python全問題数: {py_count}問")
    print(f"  うち試験対策: {exam_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"試験対策目標200問まで残り: {max(0, 200 - exam_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_python_exam_batch2()