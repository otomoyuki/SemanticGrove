import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_php8_exam_batch1():
    """PHP8試験対策問題追加（第1弾・50問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("PHP8試験対策問題追加スクリプト（第1弾・50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== PHP8新機能（15問） ====================
    print("[1/4] PHP8新機能問題を生成中...")
    
    php8_features = [
        ("PHP8の名前付き引数の書き方は？",
         [{"id":"A","text":"func(param: value)"},{"id":"B","text":"func(param=value)"},{"id":"C","text":"func($param: value)"},{"id":"D","text":"func(param => value)"}],
         [0], "PHP8試験対策_新機能", "3", 10, "名前付き引数", "Named Arguments"),
        
        ("Union型の書き方は？",
         [{"id":"A","text":"int|string"},{"id":"B","text":"int or string"},{"id":"C","text":"int, string"},{"id":"D","text":"int & string"}],
         [0], "PHP8試験対策_新機能", "3", 10, "複数型の許可", "Union Types"),
        
        ("match式の特徴は？",
         [{"id":"A","text":"厳密比較、値を返す"},{"id":"B","text":"switch と同じ"},{"id":"C","text":"緩い比較"},{"id":"D","text":"文を実行"}],
         [0], "PHP8試験対策_新機能", "3", 12, "switch の改良版", "match"),
        
        ("Null Safe演算子の書き方は？",
         [{"id":"A","text":"?->"},{"id":"B","text":"?."},{"id":"C","text":"??->"},{"id":"D","text":"->?"}],
         [0], "PHP8試験対策_新機能", "3", 10, "nullチェック付きアクセス", "?->"),
        
        ("コンストラクタプロパティプロモーションとは？",
         [{"id":"A","text":"引数から自動でプロパティ生成"},{"id":"B","text":"型チェック"},{"id":"C","text":"継承"},{"id":"D","text":"デストラクタ"}],
         [0], "PHP8試験対策_新機能", "4", 12, "public __construct(public $x)", "プロパティプロモーション"),
        
        ("Attributes（属性）の書き方は？",
         [{"id":"A","text":"#[Route('/api')]"},{"id":"B","text":"@Route('/api')"},{"id":"C","text":"[Route('/api')]"},{"id":"D","text":"Route('/api')"}],
         [0], "PHP8試験対策_新機能", "4", 15, "メタデータ注釈", "Attributes"),
        
        ("WeakMap の特徴は？",
         [{"id":"A","text":"オブジェクトを弱参照で保持"},{"id":"B","text":"強参照"},{"id":"C","text":"配列の別名"},{"id":"D","text":"高速化"}],
         [0], "PHP8試験対策_新機能", "5", 18, "メモリリーク防止", "WeakMap"),
        
        ("Stringable インターフェースの役割は？",
         [{"id":"A","text":"__toString()を保証"},{"id":"B","text":"型変換"},{"id":"C","text":"文字列操作"},{"id":"D","text":"バリデーション"}],
         [0], "PHP8試験対策_新機能", "3", 12, "文字列化可能を示す", "Stringable"),
        
        ("throw式の特徴は？",
         [{"id":"A","text":"式として使える（??と併用可）"},{"id":"B","text":"文としてのみ"},{"id":"C","text":"非推奨"},{"id":"D","text":"PHP7と同じ"}],
         [0], "PHP8試験対策_新機能", "3", 10, "throw が式に", "throw expression"),
        
        ("str_contains() の役割は？",
         [{"id":"A","text":"文字列に部分文字列が含まれるか"},{"id":"B","text":"文字列の置換"},{"id":"C","text":"文字列の分割"},{"id":"D","text":"文字列の結合"}],
         [0], "PHP8試験対策_新機能", "2", 8, "PHP8で追加された関数", "str_contains"),
        
        ("str_starts_with() の役割は？",
         [{"id":"A","text":"文字列が指定文字列で始まるか"},{"id":"B","text":"文字列が終わるか"},{"id":"C","text":"文字列の検索"},{"id":"D","text":"文字列の置換"}],
         [0], "PHP8試験対策_新機能", "2", 8, "前方一致チェック", "str_starts_with"),
        
        ("str_ends_with() の役割は？",
         [{"id":"A","text":"文字列が指定文字列で終わるか"},{"id":"B","text":"文字列が始まるか"},{"id":"C","text":"文字列の検索"},{"id":"D","text":"文字列の置換"}],
         [0], "PHP8試験対策_新機能", "2", 8, "後方一致チェック", "str_ends_with"),
        
        ("mixed型とは？",
         [{"id":"A","text":"全ての型を許可"},{"id":"B","text":"int と float のみ"},{"id":"C","text":"string のみ"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_新機能", "3", 10, "任意の型", "mixed type"),
        
        ("static戻り値型の意味は？",
         [{"id":"A","text":"呼び出されたクラスの型"},{"id":"B","text":"親クラスの型"},{"id":"C","text":"静的メソッド"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_新機能", "4", 15, "Late Static Binding", "static return"),
        
        ("JITコンパイラの効果は？",
         [{"id":"A","text":"特定の処理で高速化"},{"id":"B","text":"全てが速くなる"},{"id":"C","text":"メモリ節約"},{"id":"D","text":"影響なし"}],
         [0], "PHP8試験対策_新機能", "4", 15, "実行時コンパイル", "JIT"),
    ]
    
    questions.extend(php8_features)
    print(f"  ✓ PHP8新機能: {len(php8_features)}問")
    
    # ==================== 型システム（15問） ====================
    print("[2/4] 型システム問題を生成中...")
    
    type_system = [
        ("厳密な型チェックを有効にするには？",
         [{"id":"A","text":"declare(strict_types=1);"},{"id":"B","text":"strict_types = true;"},{"id":"C","text":"enable_strict();"},{"id":"D","text":"type_checking(true);"}],
         [0], "PHP8試験対策_型システム", "3", 10, "ファイル先頭で宣言", "strict_types"),
        
        ("戻り値の型宣言の書き方は？",
         [{"id":"A","text":"function f(): int { }"},{"id":"B","text":"function f() -> int { }"},{"id":"C","text":"function f() : int { }"},{"id":"D","text":"int function f() { }"}],
         [0], "PHP8試験対策_型システム", "2", 8, "関数定義時の型指定", "return type"),
        
        ("void戻り値型の意味は？",
         [{"id":"A","text":"何も返さない"},{"id":"B","text":"NULL を返す"},{"id":"C","text":"任意の値"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "2", 8, "返り値なし", "void"),
        
        ("never戻り値型の意味は？（PHP 8.1+）",
         [{"id":"A","text":"returnしない（例外 or exit）"},{"id":"B","text":"NULL を返す"},{"id":"C","text":"void と同じ"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "4", 15, "制御が戻らない", "never"),
        
        ("nullable型の書き方は？",
         [{"id":"A","text":"?int"},{"id":"B","text":"int?"},{"id":"C","text":"int|null"},{"id":"D","text":"nullable int"}],
         [0], "PHP8試験対策_型システム", "2", 8, "null許可", "nullable"),
        
        ("array型と配列の型ヒントの違いは？",
         [{"id":"A","text":"arrayは要素型を指定できない"},{"id":"B","text":"同じ"},{"id":"C","text":"arrayが厳密"},{"id":"D","text":"配列の型ヒントは存在しない"}],
         [0], "PHP8試験対策_型システム", "3", 10, "ジェネリクスなし", "array type"),
        
        ("callable型とは？",
         [{"id":"A","text":"呼び出し可能な型"},{"id":"B","text":"文字列型"},{"id":"C","text":"配列型"},{"id":"D","text":"オブジェクト型"}],
         [0], "PHP8試験対策_型システム", "3", 10, "関数やメソッド", "callable"),
        
        ("iterable型とは？",
         [{"id":"A","text":"foreachで使える型"},{"id":"B","text":"配列のみ"},{"id":"C","text":"文字列のみ"},{"id":"D","text":"オブジェクトのみ"}],
         [0], "PHP8試験対策_型システム", "3", 10, "arrayまたはTraversable", "iterable"),
        
        ("object型とは？",
         [{"id":"A","text":"全てのオブジェクト"},{"id":"B","text":"特定のクラスのみ"},{"id":"C","text":"配列"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "2", 8, "任意のオブジェクト型", "object"),
        
        ("false型とは？（PHP 8.0+）",
         [{"id":"A","text":"falseのみを許可"},{"id":"B","text":"bool型と同じ"},{"id":"C","text":"NULL を含む"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "3", 12, "false専用型", "false type"),
        
        ("true型とは？（PHP 8.2+）",
         [{"id":"A","text":"trueのみを許可"},{"id":"B","text":"bool型と同じ"},{"id":"C","text":"NULL を含む"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "4", 15, "true専用型", "true type"),
        
        ("型の共変性（covariance）とは？",
         [{"id":"A","text":"戻り値型を子クラスで特化できる"},{"id":"B","text":"引数型を変更"},{"id":"C","text":"エラー"},{"id":"D","text":"型なし"}],
         [0], "PHP8試験対策_型システム", "5", 18, "戻り値の型制約緩和", "covariance"),
        
        ("型の反変性（contravariance）とは？",
         [{"id":"A","text":"引数型を親クラスで一般化できる"},{"id":"B","text":"戻り値型を変更"},{"id":"C","text":"エラー"},{"id":"D","text":"型なし"}],
         [0], "PHP8試験対策_型システム", "5", 18, "引数の型制約緩和", "contravariance"),
        
        ("Intersection型とは？（PHP 8.1+）",
         [{"id":"A","text":"複数の型を同時に満たす"},{"id":"B","text":"Union型と同じ"},{"id":"C","text":"エラー"},{"id":"D","text":"配列型"}],
         [0], "PHP8試験対策_型システム", "4", 15, "A&B", "Intersection Types"),
        
        ("DNF型とは？（PHP 8.2+）",
         [{"id":"A","text":"選言標準形の型組み合わせ"},{"id":"B","text":"Union型"},{"id":"C","text":"Intersection型"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_型システム", "5", 18, "(A&B)|C", "DNF Types"),
    ]
    
    questions.extend(type_system)
    print(f"  ✓ 型システム: {len(type_system)}問")
    
    # ==================== Enum（列挙型）（10問） ====================
    print("[3/4] Enum問題を生成中...")
    
    enum_questions = [
        ("Enumの定義方法は？（PHP 8.1+）",
         [{"id":"A","text":"enum Status { }"},{"id":"B","text":"class Status enum { }"},{"id":"C","text":"const Status { }"},{"id":"D","text":"define Status { }"}],
         [0], "PHP8試験対策_Enum", "3", 10, "列挙型定義", "enum"),
        
        ("Pure Enumのケース定義は？",
         [{"id":"A","text":"case Active;"},{"id":"B","text":"const Active;"},{"id":"C","text":"Active,"},{"id":"D","text":"$Active;"}],
         [0], "PHP8試験対策_Enum", "3", 10, "値なしEnum", "Pure Enum"),
        
        ("Backed Enumとは？",
         [{"id":"A","text":"値を持つEnum"},{"id":"B","text":"値なしEnum"},{"id":"C","text":"エラー"},{"id":"D","text":"メソッドなし"}],
         [0], "PHP8試験対策_Enum", "3", 12, "int または string", "Backed Enum"),
        
        ("Backed Enumの書き方は？",
         [{"id":"A","text":"enum Status: int { case Active = 1; }"},{"id":"B","text":"enum Status(int) { Active = 1; }"},{"id":"C","text":"enum Status<int> { Active = 1; }"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "3", 12, "型指定付き", "Backed Enum定義"),
        
        ("Enumのメソッド定義は可能？",
         [{"id":"A","text":"可能"},{"id":"B","text":"不可能"},{"id":"C","text":"static のみ"},{"id":"D","text":"public のみ"}],
         [0], "PHP8試験対策_Enum", "3", 10, "メソッド追加可能", "Enumメソッド"),
        
        ("Enum::cases() の役割は？",
         [{"id":"A","text":"全てのケースの配列を返す"},{"id":"B","text":"ケース数を返す"},{"id":"C","text":"特定のケースを返す"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "3", 10, "ケース一覧取得", "cases()"),
        
        ("Backed Enumの->value の役割は？",
         [{"id":"A","text":"バッキング値を取得"},{"id":"B","text":"名前を取得"},{"id":"C","text":"型を取得"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "2", 8, "バッキング値アクセス", "->value"),
        
        ("Enumの->name プロパティの値は？",
         [{"id":"A","text":"ケース名"},{"id":"B","text":"バッキング値"},{"id":"C","text":"型"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "2", 8, "ケース名取得", "->name"),
        
        ("Backed Enum::from() の役割は？",
         [{"id":"A","text":"値からケースを取得"},{"id":"B","text":"名前からケース取得"},{"id":"C","text":"ケース作成"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "3", 12, "値からEnum", "from()"),
        
        ("Backed Enum::tryFrom() と from() の違いは？",
         [{"id":"A","text":"tryFromはnull返却、fromは例外"},{"id":"B","text":"同じ"},{"id":"C","text":"fromがnull返却"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Enum", "3", 12, "エラーハンドリング", "tryFrom()"),
    ]
    
    questions.extend(enum_questions)
    print(f"  ✓ Enum: {len(enum_questions)}問")
    
    # ==================== ReadOnly とFiber（10問） ====================
    print("[4/4] ReadOnly とFiber問題を生成中...")
    
    readonly_fiber = [
        ("readonly プロパティの特徴は？（PHP 8.1+）",
         [{"id":"A","text":"初期化後は変更不可"},{"id":"B","text":"変更可能"},{"id":"C","text":"読み取り専用"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_ReadOnly", "3", 10, "イミュータブル", "readonly"),
        
        ("readonly プロパティの初期化タイミングは？",
         [{"id":"A","text":"宣言時かコンストラクタ"},{"id":"B","text":"いつでも"},{"id":"C","text":"宣言時のみ"},{"id":"D","text":"メソッド内のみ"}],
         [0], "PHP8試験対策_ReadOnly", "3", 10, "初期化制限", "初期化"),
        
        ("readonly クラスとは？（PHP 8.2+）",
         [{"id":"A","text":"全プロパティがreadonly"},{"id":"B","text":"メソッドなし"},{"id":"C","text":"継承不可"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_ReadOnly", "4", 12, "クラスレベルreadonly", "readonly class"),
        
        ("Fiber とは？（PHP 8.1+）",
         [{"id":"A","text":"軽量な並行処理"},{"id":"B","text":"スレッド"},{"id":"C","text":"プロセス"},{"id":"D","text":"非同期I/O"}],
         [0], "PHP8試験対策_Fiber", "5", 18, "コルーチン", "Fiber"),
        
        ("Fiber::start() の役割は？",
         [{"id":"A","text":"Fiber実行開始"},{"id":"B","text":"Fiber停止"},{"id":"C","text":"Fiber再開"},{"id":"D","text":"Fiber終了"}],
         [0], "PHP8試験対策_Fiber", "4", 15, "初回実行", "start()"),
        
        ("Fiber::suspend() の役割は？",
         [{"id":"A","text":"実行を一時停止"},{"id":"B","text":"実行開始"},{"id":"C","text":"実行終了"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Fiber", "4", 15, "中断", "suspend()"),
        
        ("Fiber::resume() の役割は？",
         [{"id":"A","text":"実行を再開"},{"id":"B","text":"実行開始"},{"id":"C","text":"実行停止"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_Fiber", "4", 15, "再開", "resume()"),
        
        ("First-class callable syntax とは？（PHP 8.1+）",
         [{"id":"A","text":"関数名(...)で関数参照"},{"id":"B","text":"通常の呼び出し"},{"id":"C","text":"エラー"},{"id":"D","text":"非推奨"}],
         [0], "PHP8試験対策_新機能", "4", 12, "callable取得", "callable syntax"),
        
        ("new in initializers とは？（PHP 8.1+）",
         [{"id":"A","text":"デフォルト引数でnew可能"},{"id":"B","text":"コンストラクタ"},{"id":"C","text":"エラー"},{"id":"D","text":"非推奨"}],
         [0], "PHP8試験対策_新機能", "4", 12, "初期化式", "new in initializers"),
        
        ("Final class constants とは？（PHP 8.1+）",
         [{"id":"A","text":"オーバーライド不可の定数"},{"id":"B","text":"変更不可の定数"},{"id":"C","text":"通常の定数"},{"id":"D","text":"エラー"}],
         [0], "PHP8試験対策_新機能", "3", 10, "final const", "final constants"),
    ]
    
    questions.extend(readonly_fiber)
    print(f"  ✓ ReadOnly とFiber: {len(readonly_fiber)}問")
    
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
    
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'PHP' AND category LIKE 'PHP8試験対策%'")
    php8_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ PHP8試験対策問題追加完了（第1弾）！")
    print("=" * 60)
    print(f"PHP全問題数: {php_count}問")
    print(f"  基礎問題: {php_count - php8_count}問")
    print(f"  PHP8試験対策: {php8_count}問")
    print(f"全体問題数: {total_count}問")
    print("=" * 60)

if __name__ == "__main__":
    add_php8_exam_batch1()