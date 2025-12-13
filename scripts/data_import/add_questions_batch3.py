import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_questions_batch3():
    """問題追加（第3弾）- PHP, Ruby, Go, Java, C#"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("問題追加スクリプト（第3弾）")
    print("=" * 60)
    
    cursor.execute("SELECT language, COUNT(*) FROM questions GROUP BY language")
    existing = dict(cursor.fetchall())
    
    print("\n現在の問題数:")
    for lang, count in sorted(existing.items()):
        print(f"  {lang}: {count}問")
    
    print("\n問題を追加中...")
    questions = []
    
    # ==================== PHP追加問題 ====================
    print("[1/5] PHP追加問題を生成中...")
    
    php_questions = [
        ("PHPでechoとprintの違いとして正しいのはどれですか？",
         [{"id":"A","text":"echoは複数の値を出力可能、printは戻り値あり"},{"id":"B","text":"printの方が速い"},{"id":"C","text":"違いはない"},{"id":"D","text":"echoは関数、printは構文"}],
         [0], "基本文法", "2", 5, "echoは言語構造で複数引数可、printは式で戻り値1を返す", "実用上はechoを使うのが一般的"),
        
        ("PHPで配列に要素を追加する方法として正しいのはどれですか？",
         [{"id":"A","text":"$arr[] = 'value';"},{"id":"B","text":"array_push($arr, 'value');"},{"id":"C","text":"両方正しい"},{"id":"D","text":"$arr.push('value');"}],
         [2], "配列", "2", 5, "[]記法とarray_push()の両方が使える", "[]の方が簡潔で高速"),
        
        ("PHPで連想配列を作成する正しい構文はどれですか？",
         [{"id":"A","text":"['key' => 'value']"},{"id":"B","text":"['key': 'value']"},{"id":"C","text":"{'key': 'value'}"},{"id":"D","text":"('key' => 'value')"}],
         [0], "配列", "2", 5, "=>演算子でキーと値を関連付ける", "連想配列はPHPの強力な機能"),
        
        ("PHPでクラスを定義する正しい構文はどれですか？",
         [{"id":"A","text":"class MyClass {}"},{"id":"B","text":"Class MyClass {}"},{"id":"C","text":"define class MyClass {}"},{"id":"D","text":"new class MyClass {}"}],
         [0], "オブジェクト指向", "3", 5, "classキーワードでクラスを定義", "オブジェクト指向プログラミングの基本"),
        
        ("PHPでコンストラクタを定義するメソッド名はどれですか？",
         [{"id":"A","text":"__construct"},{"id":"B","text":"constructor"},{"id":"C","text":"__init__"},{"id":"D","text":"initialize"}],
         [0], "オブジェクト指向", "3", 5, "__construct()がコンストラクタ", "オブジェクト初期化に使用"),
        
        ("PHPで文字列の長さを取得する関数はどれですか？",
         [{"id":"A","text":"strlen()"},{"id":"B","text":"length()"},{"id":"C","text":"size()"},{"id":"D","text":"count()"}],
         [0], "文字列", "1", 5, "strlen()で文字列のバイト数を取得", "文字列処理の基本"),
        
        ("PHPで配列の要素数を取得する関数はどれですか？",
         [{"id":"A","text":"count()"},{"id":"B","text":"sizeof()"},{"id":"C","text":"両方正しい"},{"id":"D","text":"length()"}],
         [2], "配列", "2", 5, "count()とsizeof()は同じ動作", "count()が一般的"),
        
        ("PHPでincludeとrequireの違いは何ですか？",
         [{"id":"A","text":"requireは失敗時に致命的エラー"},{"id":"B","text":"includeの方が高速"},{"id":"C","text":"違いはない"},{"id":"D","text":"requireは複数回読み込める"}],
         [0], "ファイル操作", "3", 5, "requireはファイルが必須、includeは警告のみ", "重要なファイルにはrequireを使用"),
        
        ("PHPでセッションを開始する関数はどれですか？",
         [{"id":"A","text":"session_start()"},{"id":"B","text":"start_session()"},{"id":"C","text":"begin_session()"},{"id":"D","text":"init_session()"}],
         [0], "セッション", "3", 5, "session_start()でセッションを初期化", "ログイン機能などで必須"),
        
        ("PHPでデータベースに接続する推奨方法はどれですか？",
         [{"id":"A","text":"PDO"},{"id":"B","text":"mysqli"},{"id":"C","text":"mysql"},{"id":"D","text":"どれでも同じ"}],
         [0], "データベース", "4", 10, "PDOはデータベース抽象化レイヤー", "SQLインジェクション対策も容易"),
    ]
    
    for q in php_questions[:20]:
        questions.append(create_question("PHP", *q))
    
    print(f"  ✓ PHP: {len([q for q in questions if q[0]=='PHP'])}問追加")
    
    # ==================== Ruby問題 ====================
    print("[2/5] Ruby問題を生成中...")
    
    ruby_questions = [
        ("Rubyでメソッドを定義する正しい構文はどれですか？",
         [{"id":"A","text":"def method_name ... end"},{"id":"B","text":"function method_name() {}"},{"id":"C","text":"method method_name {}"},{"id":"D","text":"fn method_name {}"}],
         [0], "基本文法", "1", 5, "def メソッド名 ... end でメソッドを定義", "Rubyの基本構文"),
        
        ("Rubyでシンボルを表す記号はどれですか？",
         [{"id":"A","text":":symbol"},{"id":"B","text":"@symbol"},{"id":"C","text":"$symbol"},{"id":"D","text":"#symbol"}],
         [0], "データ型", "2", 5, ":で始まるのがシンボル", "ハッシュのキーなどに使用"),
        
        ("Rubyで配列の各要素に処理を適用するメソッドはどれですか？",
         [{"id":"A","text":"each"},{"id":"B","text":"map"},{"id":"C","text":"両方正しい"},{"id":"D","text":"forEach"}],
         [2], "配列", "2", 5, "eachは反復、mapは変換結果を返す", "ブロックと組み合わせて使用"),
        
        ("Rubyでハッシュを作成する構文はどれですか？",
         [{"id":"A","text":"{key: 'value'}"},{"id":"B","text":"{'key' => 'value'}"},{"id":"C","text":"両方正しい"},{"id":"D","text":"['key', 'value']"}],
         [2], "ハッシュ", "2", 5, "シンボルキーと文字列キーの両方が使える", "用途に応じて使い分け"),
        
        ("Rubyでクラスを定義する構文はどれですか？",
         [{"id":"A","text":"class MyClass ... end"},{"id":"B","text":"Class MyClass {}"},{"id":"C","text":"define MyClass {}"},{"id":"D","text":"new Class MyClass"}],
         [0], "オブジェクト指向", "3", 5, "class クラス名 ... end で定義", "Rubyは純粋なOOP言語"),
        
        ("Rubyでアクセサを自動生成するメソッドはどれですか？",
         [{"id":"A","text":"attr_accessor"},{"id":"B","text":"accessor"},{"id":"C","text":"getter_setter"},{"id":"D","text":"property"}],
         [0], "オブジェクト指向", "3", 5, "attr_accessorでgetter/setterを自動生成", "コードを簡潔にする"),
        
        ("Rubyで文字列補間の正しい構文はどれですか？",
         [{"id":"A","text":"\"Hello #{name}\""},{"id":"B","text":"'Hello #{name}'"},{"id":"C","text":"\"Hello ${name}\""},{"id":"D","text":"'Hello ${name}'"}],
         [0], "文字列", "2", 5, "ダブルクォートと#{}で補間", "文字列の組み立てに便利"),
        
        ("Rubyで範囲を表す演算子はどれですか？",
         [{"id":"A","text":".."},{"id":"B","text":"..."},{"id":"C","text":"両方正しい"},{"id":"D","text":"->"}],
         [2], "範囲", "2", 5, "..は末尾含む、...は末尾含まない", "ループや配列の切り出しに使用"),
        
        ("Rubyでブロックを受け取るメソッドの定義で使うキーワードはどれですか？",
         [{"id":"A","text":"yield"},{"id":"B","text":"block"},{"id":"C","text":"callback"},{"id":"D","text":"lambda"}],
         [0], "ブロック", "4", 10, "yieldでブロックを呼び出す", "イテレータの実装に使用"),
        
        ("Rubyでモジュールを定義する構文はどれですか？",
         [{"id":"A","text":"module MyModule ... end"},{"id":"B","text":"Module MyModule {}"},{"id":"C","text":"namespace MyModule {}"},{"id":"D","text":"package MyModule {}"}],
         [0], "モジュール", "4", 10, "module モジュール名 ... end で定義", "名前空間やミックスインに使用"),
    ]
    
    for q in ruby_questions[:20]:
        questions.append(create_question("Ruby", *q))
    
    print(f"  ✓ Ruby: {len([q for q in questions if q[0]=='Ruby'])}問追加")
    
    # ==================== Go問題 ====================
    print("[3/5] Go問題を生成中...")
    
    go_questions = [
        ("Goで変数を宣言する短縮記法はどれですか？",
         [{"id":"A","text":"x := 10"},{"id":"B","text":"var x = 10"},{"id":"C","text":"両方正しい"},{"id":"D","text":"let x = 10"}],
         [2], "基本文法", "1", 5, ":=は型推論付き宣言、varは明示的宣言", "関数内では:=が一般的"),
        
        ("Goで配列を宣言する構文はどれですか？",
         [{"id":"A","text":"var arr [5]int"},{"id":"B","text":"var arr []int"},{"id":"C","text":"arr := []int{1,2,3}"},{"id":"D","text":"すべて正しい"}],
         [3], "配列", "2", 5, "固定長配列、スライス、リテラル初期化が可能", "用途に応じて使い分け"),
        
        ("Goでスライスと配列の違いとして正しいのはどれですか？",
         [{"id":"A","text":"スライスは可変長、配列は固定長"},{"id":"B","text":"違いはない"},{"id":"C","text":"スライスの方が遅い"},{"id":"D","text":"配列は使えない"}],
         [0], "スライス", "2", 5, "スライスは動的サイズ、配列は静的サイズ", "実用上はスライスを多用"),
        
        ("Goで関数が複数の値を返す正しい構文はどれですか？",
         [{"id":"A","text":"func f() (int, error) {}"},{"id":"B","text":"func f() int, error {}"},{"id":"C","text":"func f() [int, error] {}"},{"id":"D","text":"func f(): (int, error) {}"}],
         [0], "関数", "2", 5, "(型1, 型2)の形式で複数の戻り値を宣言", "エラーハンドリングのパターン"),
        
        ("Goでポインタを取得する演算子はどれですか？",
         [{"id":"A","text":"&"},{"id":"B","text":"*"},{"id":"C","text":"->"},{"id":"D","text":"@"}],
         [0], "ポインタ", "3", 5, "&でアドレスを取得、*でデリファレンス", "メモリ効率の良いプログラミング"),
        
        ("Goでgoroutineを起動するキーワードはどれですか？",
         [{"id":"A","text":"go"},{"id":"B","text":"async"},{"id":"C","text":"thread"},{"id":"D","text":"spawn"}],
         [0], "並行処理", "4", 10, "go funcName()で並行実行", "Goの並行処理の核心"),
        
        ("Goでチャネルを作成する関数はどれですか？",
         [{"id":"A","text":"make(chan int)"},{"id":"B","text":"chan(int)"},{"id":"C","text":"new(chan int)"},{"id":"D","text":"channel(int)"}],
         [0], "チャネル", "4", 10, "makeでチャネルを初期化", "goroutine間通信に使用"),
        
        ("Goで構造体を定義する構文はどれですか？",
         [{"id":"A","text":"type Name struct {}"},{"id":"B","text":"struct Name {}"},{"id":"C","text":"class Name {}"},{"id":"D","text":"define Name struct {}"}],
         [0], "構造体", "3", 5, "type 名前 struct で定義", "Goのデータ構造の基本"),
        
        ("Goでインターフェースを定義する構文はどれですか？",
         [{"id":"A","text":"type Name interface {}"},{"id":"B","text":"interface Name {}"},{"id":"C","text":"define Name interface {}"},{"id":"D","text":"class Name interface {}"}],
         [0], "インターフェース", "4", 10, "type 名前 interface で定義", "暗黙的な実装が特徴"),
        
        ("Goでdeferの役割として正しいのはどれですか？",
         [{"id":"A","text":"関数終了時に実行を遅延"},{"id":"B","text":"エラーを捕捉"},{"id":"C","text":"並行処理を開始"},{"id":"D","text":"メモリを解放"}],
         [0], "defer", "4", 10, "defer文は関数の最後に実行される", "リソースのクリーンアップに使用"),
    ]
    
    for q in go_questions[:20]:
        questions.append(create_question("Go", *q))
    
    print(f"  ✓ Go: {len([q for q in questions if q[0]=='Go'])}問追加")
    
    # ==================== Java問題 ====================
    print("[4/5] Java問題を生成中...")
    
    java_questions = [
        ("Javaでクラスを定義する正しい構文はどれですか？",
         [{"id":"A","text":"public class MyClass {}"},{"id":"B","text":"class public MyClass {}"},{"id":"C","text":"Class MyClass {}"},{"id":"D","text":"define class MyClass {}"}],
         [0], "基本文法", "1", 5, "public class クラス名 で定義", "Javaの基本構造"),
        
        ("Javaでmainメソッドの正しいシグネチャはどれですか？",
         [{"id":"A","text":"public static void main(String[] args)"},{"id":"B","text":"public void main(String[] args)"},{"id":"C","text":"static void main(String[] args)"},{"id":"D","text":"void main()"}],
         [0], "メイン", "1", 5, "プログラムのエントリーポイント", "必ずpublic staticが必要"),
        
        ("Javaで変数を宣言する正しい構文はどれですか？",
         [{"id":"A","text":"int x = 10;"},{"id":"B","text":"var x = 10;"},{"id":"C","text":"x := 10;"},{"id":"D","text":"let x = 10;"}],
         [0], "変数", "1", 5, "型 変数名 = 値; の形式", "型の明示が基本"),
        
        ("Javaで継承を表すキーワードはどれですか？",
         [{"id":"A","text":"extends"},{"id":"B","text":"implements"},{"id":"C","text":"inherit"},{"id":"D","text":"from"}],
         [0], "継承", "2", 5, "extendsでクラス継承", "単一継承のみ"),
        
        ("Javaでインターフェースを実装するキーワードはどれですか？",
         [{"id":"A","text":"implements"},{"id":"B","text":"extends"},{"id":"C","text":"uses"},{"id":"D","text":"with"}],
         [0], "インターフェース", "2", 5, "implementsで実装", "複数実装可能"),
        
        ("Javaでオーバーライドを示すアノテーションはどれですか？",
         [{"id":"A","text":"@Override"},{"id":"B","text":"@Overload"},{"id":"C","text":"@Inherit"},{"id":"D","text":"@Super"}],
         [0], "オーバーライド", "3", 5, "@Overrideで意図を明示", "コンパイラがチェック"),
        
        ("Javaでジェネリクスを使う構文はどれですか？",
         [{"id":"A","text":"List<String>"},{"id":"B","text":"List[String]"},{"id":"C","text":"List(String)"},{"id":"D","text":"List{String}"}],
         [0], "ジェネリクス", "4", 10, "<型>で型パラメータを指定", "型安全性を向上"),
        
        ("Javaでラムダ式の正しい構文はどれですか？",
         [{"id":"A","text":"(x) -> x * 2"},{"id":"B","text":"(x) => x * 2"},{"id":"C","text":"lambda x: x * 2"},{"id":"D","text":"x => x * 2"}],
         [0], "ラムダ式", "4", 10, "(引数) -> 式 の形式", "Java 8以降の機能"),
        
        ("Javaでストリーム処理を開始するメソッドはどれですか？",
         [{"id":"A","text":"stream()"},{"id":"B","text":"forEach()"},{"id":"C","text":"map()"},{"id":"D","text":"filter()"}],
         [0], "ストリーム", "4", 10, "stream()でStreamを生成", "関数型プログラミング"),
        
        ("Javaで例外を投げる構文はどれですか？",
         [{"id":"A","text":"throw new Exception()"},{"id":"B","text":"raise Exception()"},{"id":"C","text":"error Exception()"},{"id":"D","text":"exception Exception()"}],
         [0], "例外処理", "3", 5, "throw new で例外を投げる", "エラーハンドリングの基本"),
    ]
    
    for q in java_questions[:20]:
        questions.append(create_question("Java", *q))
    
    print(f"  ✓ Java: {len([q for q in questions if q[0]=='Java'])}問追加")
    
    # ==================== C#問題（Unity向け） ====================
    print("[5/5] C#問題（Unity向け）を生成中...")
    
    csharp_questions = [
        ("C#でnamespaceを定義する構文はどれですか？",
         [{"id":"A","text":"namespace MyNamespace {}"},{"id":"B","text":"Namespace MyNamespace {}"},{"id":"C","text":"package MyNamespace;"},{"id":"D","text":"module MyNamespace {}"}],
         [0], "基本文法", "1", 5, "namespace 名前空間 で定義", "名前の衝突を防ぐ"),
        
        ("C#でプロパティを定義する構文はどれですか？",
         [{"id":"A","text":"public int Value { get; set; }"},{"id":"B","text":"public int Value()"},{"id":"C","text":"int Value { get set }"},{"id":"D","text":"property int Value"}],
         [0], "プロパティ", "2", 5, "{ get; set; }で自動プロパティ", "フィールドへの安全なアクセス"),
        
        ("UnityでMonoBehaviourを継承する理由は何ですか？",
         [{"id":"A","text":"ゲームオブジェクトにアタッチ可能になる"},{"id":"B","text":"必須ではない"},{"id":"C","text":"高速化される"},{"id":"D","text":"メモリが節約される"}],
         [0], "Unity基礎", "2", 5, "MonoBehaviourでUnityのライフサイクルにアクセス", "Unityスクリプトの基本"),
        
        ("Unityで毎フレーム呼ばれるメソッドはどれですか？",
         [{"id":"A","text":"Update()"},{"id":"B","text":"Start()"},{"id":"C","text":"Awake()"},{"id":"D","text":"OnEnable()"}],
         [0], "Unity基礎", "1", 5, "Update()は毎フレーム実行", "ゲームロジックの更新"),
        
        ("Unityで初期化時に一度だけ呼ばれるメソッドはどれですか？",
         [{"id":"A","text":"Start()"},{"id":"B","text":"Update()"},{"id":"C","text":"FixedUpdate()"},{"id":"D","text":"LateUpdate()"}],
         [0], "Unity基礎", "1", 5, "Start()は最初のフレーム前に実行", "初期化処理に使用"),
        
        ("UnityでGameObjectを取得するメソッドはどれですか？",
         [{"id":"A","text":"GameObject.Find()"},{"id":"B","text":"GetGameObject()"},{"id":"C","text":"FindObject()"},{"id":"D","text":"SearchObject()"}],
         [0], "Unity API", "2", 5, "GameObject.Find()で名前検索", "シーン内のオブジェクト取得"),
        
        ("Unityでコンポーネントを取得するメソッドはどれですか？",
         [{"id":"A","text":"GetComponent<T>()"},{"id":"B","text":"FindComponent<T>()"},{"id":"C","text":"Component<T>()"},{"id":"D","text":"GetScript<T>()"}],
         [0], "Unity API", "2", 5, "GetComponent<型>()でコンポーネント取得", "他のスクリプトへのアクセス"),
        
        ("UnityでオブジェクトをInstantiateする正しい使い方はどれですか？",
         [{"id":"A","text":"Instantiate(prefab)"},{"id":"B","text":"new GameObject(prefab)"},{"id":"C","text":"Create(prefab)"},{"id":"D","text":"Spawn(prefab)"}],
         [0], "Unity API", "3", 5, "Instantiate()でオブジェクト生成", "ランタイムでの動的生成"),
        
        ("UnityでCoroutineを開始するメソッドはどれですか？",
         [{"id":"A","text":"StartCoroutine()"},{"id":"B","text":"BeginCoroutine()"},{"id":"C","text":"RunCoroutine()"},{"id":"D","text":"Coroutine()"}],
         [0], "Unity Coroutine", "4", 10, "StartCoroutine()で非同期処理開始", "時間のかかる処理に使用"),
        
        ("C#でnull条件演算子の構文はどれですか？",
         [{"id":"A","text":"obj?.Method()"},{"id":"B","text":"obj->Method()"},{"id":"C","text":"obj::Method()"},{"id":"D","text":"obj.?Method()"}],
         [0], "null安全", "3", 5, "?.でnullチェック付きアクセス", "NullReferenceException回避"),
    ]
    
    for q in csharp_questions[:20]:
        questions.append(create_question("C#", *q))
    
    print(f"  ✓ C#: {len([q for q in questions if q[0]=='C#'])}問追加")
    
    # データベースに保存
    print("\nデータベースに保存中...")
    
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (language, question_json, category, difficulty, score, meaning, usage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, q)
    
    conn.commit()
    
    # 最終集計
    cursor.execute("SELECT language, COUNT(*) FROM questions GROUP BY language ORDER BY language")
    final_stats = cursor.fetchall()
    
    print("\n" + "=" * 60)
    print("✓ 問題追加完了（第3弾）！")
    print("=" * 60)
    print("\n最終問題数:")
    total = 0
    for lang, count in final_stats:
        print(f"  {lang:15} : {count:3}問")
        total += count
    print("-" * 40)
    print(f"  {'合計':15} : {total:3}問")
    print("=" * 60)
    
    conn.close()


def create_question(language, question, options, answer, category, difficulty, score, meaning, usage):
    """問題データを作成"""
    return (
        language,
        json.dumps({
            'question': question,
            'options': options,
            'answer': answer
        }, ensure_ascii=False),
        category,
        difficulty,
        score,
        meaning,
        usage
    )


if __name__ == "__main__":
    add_questions_batch3()