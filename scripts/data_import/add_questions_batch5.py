import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_questions_batch5():
    """問題追加（第5弾）- 各言語を30問以上に"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("問題追加スクリプト（第5弾）")
    print("=" * 60)
    
    cursor.execute("SELECT language, COUNT(*) FROM questions GROUP BY language")
    existing = dict(cursor.fetchall())
    
    print("\n現在の問題数:")
    for lang, count in sorted(existing.items()):
        print(f"  {lang}: {count}問")
    
    print("\n問題を追加中...")
    questions = []
    
    # ==================== React追加（15問） ====================
    print("[1/7] React追加問題を生成中...")
    
    react_more = [
        ("ReactでuseCallbackの役割は何ですか？",
         [{"id":"A","text":"関数のメモ化"},{"id":"B","text":"値のメモ化"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "Hooks", "4", 10, "useCallbackは関数をメモ化", "子コンポーネントへの props 最適化"),
        
        ("ReactでuseMemoの役割は何ですか？",
         [{"id":"A","text":"計算結果のメモ化"},{"id":"B","text":"関数のメモ化"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "Hooks", "4", 10, "useMemoは計算結果をメモ化", "重い計算の最適化"),
        
        ("ReactでuseReducerの役割は何ですか？",
         [{"id":"A","text":"複雑な状態管理"},{"id":"B","text":"副作用処理"},{"id":"C","text":"メモ化"},{"id":"D","text":"参照保持"}],
         [0], "Hooks", "5", 15, "useReducerはRedux的な状態管理", "複数の関連する状態を管理"),
        
        ("ReactでフラグメントをJSXで書く短縮記法はどれですか？",
         [{"id":"A","text":"<>...</>"},{"id":"B","text":"<Fragment>...</Fragment>"},{"id":"C","text":"両方正しい"},{"id":"D","text":"<Frag>...</Frag>"}],
         [2], "JSX", "2", 5, "<>が短縮記法", "不要なdivを避ける"),
        
        ("ReactでStrictModeの役割は何ですか？",
         [{"id":"A","text":"開発時の問題検出"},{"id":"B","text":"本番ビルドの最適化"},{"id":"C","text":"型チェック"},{"id":"D","text":"エラーハンドリング"}],
         [0], "StrictMode", "4", 10, "StrictModeは潜在的な問題を検出", "開発時のみ動作"),
        
        ("ReactでPortalの用途として正しいのはどれですか？",
         [{"id":"A","text":"DOM階層外へのレンダリング"},{"id":"B","text":"ルーティング"},{"id":"C","text":"状態管理"},{"id":"D","text":"データ取得"}],
         [0], "Portal", "5", 15, "Portalは親外のDOMノードにレンダリング", "モーダルやツールチップに使用"),
        
        ("ReactでuseLayoutEffectとuseEffectの違いは何ですか？",
         [{"id":"A","text":"useLayoutEffectは同期的に実行"},{"id":"B","text":"useLayoutEffectは速い"},{"id":"C","text":"違いはない"},{"id":"D","text":"useLayoutEffectは非推奨"}],
         [0], "Hooks", "5", 15, "useLayoutEffectは描画前に同期実行", "DOM測定などに使用"),
        
        ("Reactで制御コンポーネントの説明として正しいのはどれですか？",
         [{"id":"A","text":"フォームの値をReactの状態で管理"},{"id":"B","text":"親が子を制御"},{"id":"C","text":"条件付きレンダリング"},{"id":"D","text":"エラー制御"}],
         [0], "フォーム", "4", 10, "入力値を state で管理", "React推奨のフォーム管理"),
        
        ("ReactでuseImperativeHandleの用途は何ですか？",
         [{"id":"A","text":"子から親への参照公開"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"メモ化"}],
         [0], "Hooks", "5", 15, "forwardRefと組み合わせて使用", "子の内部メソッドを公開"),
        
        ("ReactでHydrationとは何ですか？",
         [{"id":"A","text":"SSRしたHTMLにイベントを付与"},{"id":"B","text":"データの取得"},{"id":"C","text":"キャッシュの更新"},{"id":"D","text":"状態の初期化"}],
         [0], "SSR", "5", 15, "サーバーレンダリング後のインタラクティブ化", "Next.jsなどで重要"),
        
        ("Reactでコンポーネントの表示名を設定するプロパティはどれですか？",
         [{"id":"A","text":"displayName"},{"id":"B","text":"name"},{"id":"C","text":"componentName"},{"id":"D","text":"label"}],
         [0], "デバッグ", "3", 5, "displayNameでDevToolsの表示名設定", "デバッグの可読性向上"),
        
        ("ReactでdefaultPropsの役割は何ですか？",
         [{"id":"A","text":"propsのデフォルト値設定"},{"id":"B","text":"初期状態の設定"},{"id":"C","text":"型定義"},{"id":"D","text":"バリデーション"}],
         [0], "Props", "3", 5, "props未指定時の初期値", "関数コンポーネントでも使用可能"),
        
        ("ReactでpropTypesの役割は何ですか？",
         [{"id":"A","text":"propsの型チェック"},{"id":"B","text":"デフォルト値設定"},{"id":"C","text":"状態管理"},{"id":"D","text":"パフォーマンス最適化"}],
         [0], "Props", "4", 10, "開発時にpropsの型を検証", "TypeScriptが主流だが選択肢"),
        
        ("ReactでDangerouslySetInnerHTMLを使う理由は何ですか？",
         [{"id":"A","text":"HTML文字列を直接挿入"},{"id":"B","text":"高速化"},{"id":"C","text":"セキュリティ向上"},{"id":"D","text":"推奨される方法"}],
         [0], "セキュリティ", "4", 10, "XSSリスクがあるため注意が必要", "信頼できる内容のみ使用"),
        
        ("ReactでConcurrent Modeの特徴は何ですか？",
         [{"id":"A","text":"中断可能なレンダリング"},{"id":"B","text":"並列処理"},{"id":"C","text":"高速化"},{"id":"D","text":"エラー処理"}],
         [0], "Concurrent", "5", 15, "優先度に応じてレンダリングを中断・再開", "React 18の新機能"),
    ]
    
    for q in react_more:
        questions.append(create_question("React", *q))
    
    print(f"  ✓ React: {len([q for q in questions if q[0]=='React'])}問追加")
    
    # ==================== HTML追加（10問） ====================
    print("[2/7] HTML追加問題を生成中...")
    
    html_more = [
        ("HTMLでボタンを作成するタグはどれですか？",
         [{"id":"A","text":"<button>"},{"id":"B","text":"<btn>"},{"id":"C","text":"<input type=\"button\">"},{"id":"D","text":"AとCが正しい"}],
         [3], "フォーム", "2", 5, "buttonタグまたはinput type=\"button\"", "用途に応じて使い分け"),
        
        ("HTMLでテキスト入力欄を作成するタグはどれですか？",
         [{"id":"A","text":"<input type=\"text\">"},{"id":"B","text":"<textbox>"},{"id":"C","text":"<text>"},{"id":"D","text":"<field>"}],
         [0], "フォーム", "1", 5, "input type=\"text\"でテキスト入力", "最も基本的な入力欄"),
        
        ("HTML5のセマンティック要素でナビゲーションを示すタグはどれですか？",
         [{"id":"A","text":"<nav>"},{"id":"B","text":"<navigation>"},{"id":"C","text":"<menu>"},{"id":"D","text":"<navbar>"}],
         [0], "HTML5", "2", 5, "<nav>でナビゲーション領域を定義", "サイト内リンクのグループ化"),
        
        ("HTMLでコンテンツの主要部分を示すタグはどれですか？",
         [{"id":"A","text":"<main>"},{"id":"B","text":"<content>"},{"id":"C","text":"<body>"},{"id":"D","text":"<article>"}],
         [0], "HTML5", "2", 5, "<main>で主コンテンツを定義", "ページに1つだけ"),
        
        ("HTMLでフッター領域を示すタグはどれですか？",
         [{"id":"A","text":"<footer>"},{"id":"B","text":"<bottom>"},{"id":"C","text":"<foot>"},{"id":"D","text":"<end>"}],
         [0], "HTML5", "2", 5, "<footer>でフッター領域を定義", "著作権情報などに使用"),
        
        ("HTMLで記事を示すセマンティックタグはどれですか？",
         [{"id":"A","text":"<article>"},{"id":"B","text":"<post>"},{"id":"C","text":"<content>"},{"id":"D","text":"<story>"}],
         [0], "HTML5", "3", 5, "<article>で独立したコンテンツを定義", "ブログ記事やニュース記事"),
        
        ("HTMLでセクションを示すタグはどれですか？",
         [{"id":"A","text":"<section>"},{"id":"B","text":"<div>"},{"id":"C","text":"<part>"},{"id":"D","text":"<block>"}],
         [0], "HTML5", "3", 5, "<section>でテーマ別のまとまりを定義", "divより意味のある区分"),
        
        ("HTMLで動画を埋め込むタグはどれですか？",
         [{"id":"A","text":"<video>"},{"id":"B","text":"<movie>"},{"id":"C","text":"<media>"},{"id":"D","text":"<embed>"}],
         [0], "メディア", "2", 5, "<video>で動画を埋め込み", "HTML5の標準機能"),
        
        ("HTMLで音声を埋め込むタグはどれですか？",
         [{"id":"A","text":"<audio>"},{"id":"B","text":"<sound>"},{"id":"C","text":"<music>"},{"id":"D","text":"<media>"}],
         [0], "メディア", "2", 5, "<audio>で音声を埋め込み", "HTML5の標準機能"),
        
        ("HTMLでキャンバス描画を行うタグはどれですか？",
         [{"id":"A","text":"<canvas>"},{"id":"B","text":"<draw>"},{"id":"C","text":"<graphic>"},{"id":"D","text":"<svg>"}],
         [0], "グラフィック", "3", 5, "<canvas>でJavaScriptによる描画", "ゲームやグラフに使用"),
    ]
    
    for q in html_more:
        questions.append(create_question("HTML", *q))
    
    print(f"  ✓ HTML: {len([q for q in questions if q[0]=='HTML'])}問追加")
    
    # ==================== CSS追加（10問） ====================
    print("[3/7] CSS追加問題を生成中...")
    
    css_more = [
        ("CSSでFlexboxの子要素を中央揃えにするプロパティはどれですか？",
         [{"id":"A","text":"justify-content: center"},{"id":"B","text":"align-center: true"},{"id":"C","text":"center: both"},{"id":"D","text":"flex-center: on"}],
         [0], "Flexbox", "3", 5, "justify-contentで主軸方向の配置", "align-itemsで交差軸方向"),
        
        ("CSSでGridレイアウトの列を定義するプロパティはどれですか？",
         [{"id":"A","text":"grid-template-columns"},{"id":"B","text":"columns"},{"id":"C","text":"grid-columns"},{"id":"D","text":"template-columns"}],
         [0], "Grid", "4", 10, "grid-template-columnsで列の定義", "複雑なレイアウトに使用"),
        
        ("CSSで要素を画面中央に配置するFlexboxの設定はどれですか？",
         [{"id":"A","text":"display:flex; justify-content:center; align-items:center"},{"id":"B","text":"center:true"},{"id":"C","text":"position:center"},{"id":"D","text":"align:center"}],
         [0], "配置", "3", 5, "両方向の中央揃え", "よく使うパターン"),
        
        ("CSSで疑似クラスの構文として正しいのはどれですか？",
         [{"id":"A","text":":hover"},{"id":"B","text":"::hover"},{"id":"C","text":"#hover"},{"id":"D","text":".hover"}],
         [0], "疑似クラス", "2", 5, ":で疑似クラス、::で疑似要素", "インタラクションの実装"),
        
        ("CSSで疑似要素の構文として正しいのはどれですか？",
         [{"id":"A","text":"::before"},{"id":"B","text":":before"},{"id":"C","text":"両方使える"},{"id":"D","text":"#before"}],
         [2], "疑似要素", "3", 5, "::が推奨だが:も動作", "装飾要素の追加"),
        
        ("CSSで変数を定義する構文はどれですか？",
         [{"id":"A","text":"--color: red"},{"id":"B","text":"$color: red"},{"id":"C","text":"@color: red"},{"id":"D","text":"var color = red"}],
         [0], "CSS変数", "4", 10, "--で変数定義、var()で使用", "テーマの管理に便利"),
        
        ("CSSでメディアクエリの構文はどれですか？",
         [{"id":"A","text":"@media (max-width: 768px) {}"},{"id":"B","text":"media (max-width: 768px) {}"},{"id":"C","text":"@screen (max-width: 768px) {}"},{"id":"D","text":"query (max-width: 768px) {}"}],
         [0], "レスポンシブ", "3", 5, "@mediaで画面サイズに応じた切替", "レスポンシブデザインの基本"),
        
        ("CSSでtransitionの短縮記法として正しいのはどれですか？",
         [{"id":"A","text":"transition: all 0.3s ease"},{"id":"B","text":"animation: all 0.3s"},{"id":"C","text":"transform: 0.3s"},{"id":"D","text":"delay: 0.3s"}],
         [0], "アニメーション", "3", 5, "プロパティ 時間 イージングの順", "スムーズな変化"),
        
        ("CSSでtransformで回転させる関数はどれですか？",
         [{"id":"A","text":"rotate()"},{"id":"B","text":"turn()"},{"id":"C","text":"spin()"},{"id":"D","text":"angle()"}],
         [0], "Transform", "3", 5, "rotate(45deg)で回転", "2D変形の基本"),
        
        ("CSSで要素を非表示にする方法でスペースも削除するのはどれですか？",
         [{"id":"A","text":"display: none"},{"id":"B","text":"visibility: hidden"},{"id":"C","text":"opacity: 0"},{"id":"D","text":"すべて同じ"}],
         [0], "表示制御", "3", 5, "display:noneは領域ごと削除", "visibility:hiddenは領域を保持"),
    ]
    
    for q in css_more:
        questions.append(create_question("CSS", *q))
    
    print(f"  ✓ CSS: {len([q for q in questions if q[0]=='CSS'])}問追加")
    
    # ==================== TypeScript追加（残り問題） ====================
    print("[4/7] TypeScript追加問題を生成中...")
    
    ts_more = [
        ("TypeScriptでenumを定義する構文はどれですか？",
         [{"id":"A","text":"enum Color { Red, Green }"},{"id":"B","text":"Enum Color { Red, Green }"},{"id":"C","text":"define enum Color { Red, Green }"},{"id":"D","text":"const enum = { Red, Green }"}],
         [0], "enum", "3", 5, "enumで列挙型を定義", "定数のグループ化"),
        
        ("TypeScriptでreadonly修飾子の役割は何ですか？",
         [{"id":"A","text":"プロパティを読み取り専用にする"},{"id":"B","text":"変数を定数にする"},{"id":"C","text":"関数を実行できなくする"},{"id":"D","text":"削除できなくする"}],
         [0], "修飾子", "3", 5, "readonlyで再代入を防ぐ", "イミュータブルな設計"),
        
        ("TypeScriptでnever型の用途として正しいのはどれですか？",
         [{"id":"A","text":"決して戻らない関数の戻り値"},{"id":"B","text":"null許容型"},{"id":"C","text":"任意の型"},{"id":"D","text":"未定義の型"}],
         [0], "型", "5", 15, "例外を投げるなど到達不可能", "型の安全性向上"),
    ]
    
    for q in ts_more:
        questions.append(create_question("TypeScript", *q))
    
    print(f"  ✓ TypeScript: {len([q for q in questions if q[0]=='TypeScript'])}問追加")
    
    # ==================== Java追加（20問） ====================
    print("[5/7] Java追加問題を生成中...")
    
    java_more = [
        ("Javaでfinalキーワードの役割として正しくないのはどれですか？",
         [{"id":"A","text":"パフォーマンス向上"},{"id":"B","text":"変数の再代入防止"},{"id":"C","text":"メソッドのオーバーライド防止"},{"id":"D","text":"クラスの継承防止"}],
         [0], "final", "3", 5, "finalは変更を防ぐが速度は無関係", "イミュータブルな設計"),
        
        ("Javaでstaticキーワードの説明として正しいのはどれですか？",
         [{"id":"A","text":"クラスに属する"},{"id":"B","text":"インスタンスに属する"},{"id":"C","text":"高速化される"},{"id":"D","text":"必須キーワード"}],
         [0], "static", "2", 5, "staticはクラス変数・メソッド", "インスタンス不要で呼び出し可能"),
        
        ("Javaでabstractクラスの説明として正しいのはどれですか？",
         [{"id":"A","text":"インスタンス化できない"},{"id":"B","text":"メソッドを持てない"},{"id":"C","text":"継承できない"},{"id":"D","text":"高速化される"}],
         [0], "abstract", "4", 10, "抽象クラスは直接インスタンス化不可", "抽象メソッドを含める"),
        
        ("Javaでインターフェースのデフォルトメソッドを定義するキーワードはどれですか？",
         [{"id":"A","text":"default"},{"id":"B","text":"def"},{"id":"C","text":"implement"},{"id":"D","text":"base"}],
         [0], "インターフェース", "4", 10, "Java 8以降でdefaultメソッド", "実装を持つメソッド"),
        
        ("Javaでコレクションのサイズを取得するメソッドはどれですか？",
         [{"id":"A","text":"size()"},{"id":"B","text":"length()"},{"id":"C","text":"count()"},{"id":"D","text":"len()"}],
         [0], "コレクション", "2", 5, "size()で要素数を取得", "ListやSetで使用"),
    ]
    
    for q in java_more[:10]:
        questions.append(create_question("Java", *q))
    
    print(f"  ✓ Java: {len([q for q in questions if q[0]=='Java'])}問追加")
    
    # ==================== Ruby追加（10問） ====================
    print("[6/7] Ruby追加問題を生成中...")
    
    ruby_more = [
        ("Rubyで真偽値の反転を行う演算子はどれですか？",
         [{"id":"A","text":"!"},{"id":"B","text":"not"},{"id":"C","text":"両方正しい"},{"id":"D","text":"~"}],
         [2], "演算子", "2", 5, "!またはnotで否定", "優先順位に注意"),
        
        ("Rubyでメソッド名の最後に?を付ける慣習は何を意味しますか？",
         [{"id":"A","text":"真偽値を返す"},{"id":"B","text":"省略可能"},{"id":"C","text":"非推奨"},{"id":"D","text":"特に意味はない"}],
         [0], "命名規則", "2", 5, "?は真偽値を返すメソッド", "empty?、nil?など"),
        
        ("Rubyでメソッド名の最後に!を付ける慣習は何を意味しますか？",
         [{"id":"A","text":"破壊的メソッド"},{"id":"B","text":"重要なメソッド"},{"id":"C","text":"必須メソッド"},{"id":"D","text":"非推奨"}],
         [0], "命名規則", "3", 5, "!は元のオブジェクトを変更", "sort!、reverse!など"),
        
        ("Rubyでクラスの継承を表す記号はどれですか？",
         [{"id":"A","text":"<"},{"id":"B","text":"extends"},{"id":"C","text":"inherits"},{"id":"D","text":"from"}],
         [0], "継承", "2", 5, "class Child < Parent で継承", "単一継承のみ"),
        
        ("Rubyでモジュールをクラスに取り込む方法はどれですか？",
         [{"id":"A","text":"include"},{"id":"B","text":"prepend"},{"id":"C","text":"extend"},{"id":"D","text":"すべて正しい"}],
         [3], "モジュール", "4", 10, "include、prepend、extendで取込", "用途で使い分け"),
    ]
    
    for q in ruby_more[:10]:
        questions.append(create_question("Ruby", *q))
    
    print(f"  ✓ Ruby: {len([q for q in questions if q[0]=='Ruby'])}問追加")
    
    # ==================== COBOL追加（5問） ====================
    print("[7/7] COBOL追加問題を生成中...")
    
    cobol_more = [
        ("COBOLで文字列型を定義する記号はどれですか？",
         [{"id":"A","text":"PIC X"},{"id":"B","text":"PIC 9"},{"id":"C","text":"PIC A"},{"id":"D","text":"PIC S"}],
         [0], "データ定義", "2", 5, "PIC Xで文字列、PIC 9で数値", "データ型の基本"),
        
        ("COBOLでファイルを閉じるコマンドはどれですか？",
         [{"id":"A","text":"CLOSE"},{"id":"B","text":"END"},{"id":"C","text":"FINISH"},{"id":"D","text":"STOP"}],
         [0], "ファイル操作", "2", 5, "CLOSEでファイルをクローズ", "リソースの解放"),
        
        ("COBOLで加算を行う動詞はどれですか？",
         [{"id":"A","text":"ADD"},{"id":"B","text":"PLUS"},{"id":"C","text":"SUM"},{"id":"D","text":"INCREASE"}],
         [0], "計算", "1", 5, "ADDで加算", "TO句と組み合わせて使用"),
        
        ("COBOLで減算を行う動詞はどれですか？",
         [{"id":"A","text":"SUBTRACT"},{"id":"B","text":"MINUS"},{"id":"C","text":"DECREASE"},{"id":"D","text":"REMOVE"}],
         [0], "計算", "1", 5, "SUBTRACTで減算", "FROM句と組み合わせて使用"),
        
        ("COBOLで乗算を行う動詞はどれですか？",
         [{"id":"A","text":"MULTIPLY"},{"id":"B","text":"TIMES"},{"id":"C","text":"PRODUCT"},{"id":"D","text":"MUL"}],
         [0], "計算", "2", 5, "MULTIPLYで乗算", "BY句と組み合わせて使用"),
    ]
    
    for q in cobol_more:
        questions.append(create_question("COBOL", *q))
    
    print(f"  ✓ COBOL: {len([q for q in questions if q[0]=='COBOL'])}問追加")
    
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
    print("✓ 問題追加完了（第5弾）！")
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
    add_questions_batch5()