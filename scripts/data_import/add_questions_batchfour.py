import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_questions_batchfour():
    """問題追加（第4弾）- React, COBOL, VBA + 既存言語の充実"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("問題追加スクリプト（第4弾）")
    print("=" * 60)
    
    cursor.execute("SELECT language, COUNT(*) FROM questions GROUP BY language")
    existing = dict(cursor.fetchall())
    
    print("\n現在の問題数:")
    for lang, count in sorted(existing.items()):
        print(f"  {lang}: {count}問")
    
    print("\n問題を追加中...")
    questions = []
    
    # ==================== React問題 ====================
    print("[1/6] React問題を生成中...")
    
    react_questions = [
        ("Reactでコンポーネントを定義する方法として正しいのはどれですか？",
         [{"id":"A","text":"function MyComponent() {}"},{"id":"B","text":"class MyComponent extends React.Component {}"},{"id":"C","text":"両方正しい"},{"id":"D","text":"component MyComponent {}"}],
         [2], "基本", "1", 5, "関数コンポーネントとクラスコンポーネントがある", "関数コンポーネントが主流"),
        
        ("ReactでJSXを使う理由は何ですか？",
         [{"id":"A","text":"UIを宣言的に記述できる"},{"id":"B","text":"必須ではない"},{"id":"C","text":"高速化される"},{"id":"D","text":"メモリが節約される"}],
         [0], "JSX", "1", 5, "JSXはJavaScript内でHTMLライクな記述が可能", "Reactの中心的な機能"),
        
        ("Reactで状態管理を行うフックはどれですか？",
         [{"id":"A","text":"useState"},{"id":"B","text":"useEffect"},{"id":"C","text":"useContext"},{"id":"D","text":"useRef"}],
         [0], "Hooks", "2", 5, "useStateでコンポーネントの状態を管理", "最も基本的なフック"),
        
        ("Reactで副作用を扱うフックはどれですか？",
         [{"id":"A","text":"useEffect"},{"id":"B","text":"useState"},{"id":"C","text":"useCallback"},{"id":"D","text":"useMemo"}],
         [0], "Hooks", "2", 5, "useEffectはレンダリング後の処理を実行", "データ取得やDOM操作に使用"),
        
        ("ReactでPropsを受け取る正しい方法はどれですか？",
         [{"id":"A","text":"function MyComp(props) {}"},{"id":"B","text":"function MyComp({name}) {}"},{"id":"C","text":"両方正しい"},{"id":"D","text":"function MyComp[props] {}"}],
         [2], "Props", "2", 5, "propsオブジェクトまたは分割代入で受け取る", "親から子へのデータ渡し"),
        
        ("ReactでイベントハンドラをBindする必要があるのはどの場合ですか？",
         [{"id":"A","text":"クラスコンポーネントの通常メソッド"},{"id":"B","text":"関数コンポーネント"},{"id":"C","text":"アロー関数"},{"id":"D","text":"すべて"}],
         [0], "イベント", "3", 5, "クラスメソッドはthisをbindする必要がある", "アロー関数で回避可能"),
        
        ("Reactでリストをレンダリングする際に必須の属性はどれですか？",
         [{"id":"A","text":"key"},{"id":"B","text":"id"},{"id":"C","text":"index"},{"id":"D","text":"name"}],
         [0], "リスト", "2", 5, "keyはReactが要素を識別するために必要", "ユニークな値を指定"),
        
        ("ReactでContextを作成する関数はどれですか？",
         [{"id":"A","text":"React.createContext()"},{"id":"B","text":"new Context()"},{"id":"C","text":"Context.create()"},{"id":"D","text":"useContext()"}],
         [0], "Context", "4", 10, "createContextでContextオブジェクトを作成", "グローバル状態の共有に使用"),
        
        ("Reactでメモ化されたコンポーネントを作る関数はどれですか？",
         [{"id":"A","text":"React.memo()"},{"id":"B","text":"useMemo()"},{"id":"C","text":"useCallback()"},{"id":"D","text":"React.PureComponent"}],
         [0], "パフォーマンス", "4", 10, "React.memo()で不要な再レンダリングを防ぐ", "パフォーマンス最適化"),
        
        ("ReactでRefを作成するフックはどれですか？",
         [{"id":"A","text":"useRef"},{"id":"B","text":"createRef"},{"id":"C","text":"useState"},{"id":"D","text":"useEffect"}],
         [0], "Ref", "3", 5, "useRefでDOM要素への参照を保持", "フックではcreateRefより推奨"),
        
        ("Reactでカスタムフックの命名規則として正しいのはどれですか？",
         [{"id":"A","text":"useで始める"},{"id":"B","text":"hookで始める"},{"id":"C","text":"customで始める"},{"id":"D","text":"規則はない"}],
         [0], "カスタムフック", "3", 5, "useプレフィックスが必須", "Reactがフックと認識するため"),
        
        ("ReactでuseEffectのクリーンアップ関数はいつ実行されますか？",
         [{"id":"A","text":"コンポーネントのアンマウント時"},{"id":"B","text":"マウント時"},{"id":"C","text":"レンダリング時"},{"id":"D","text":"実行されない"}],
         [0], "useEffect", "4", 10, "クリーンアップ関数はアンマウント時や依存値変更前に実行", "リソースの解放に使用"),
        
        ("Reactでパフォーマンスを測定するツールはどれですか？",
         [{"id":"A","text":"React Developer Tools Profiler"},{"id":"B","text":"console.log()"},{"id":"C","text":"debugger"},{"id":"D","text":"alert()"}],
         [0], "デバッグ", "4", 10, "ProfilerでコンポーネントのレンダリングTime計測", "ボトルネック特定に使用"),
        
        ("Reactでエラーバウンダリはどのメソッドで実装しますか？",
         [{"id":"A","text":"componentDidCatch"},{"id":"B","text":"useError"},{"id":"C","text":"try-catch"},{"id":"D","text":"onError"}],
         [0], "エラー処理", "5", 15, "componentDidCatchでエラーをキャッチ", "クラスコンポーネントのみ"),
        
        ("ReactでSuspenseの用途として正しいのはどれですか？",
         [{"id":"A","text":"非同期読み込み中のフォールバック表示"},{"id":"B","text":"エラー処理"},{"id":"C","text":"状態管理"},{"id":"D","text":"ルーティング"}],
         [0], "Suspense", "5", 15, "Suspenseはローディング状態を宣言的に扱う", "React.lazyと組み合わせて使用"),
    ]
    
    for q in react_questions[:25]:
        questions.append(create_question("React", *q))
    
    print(f"  ✓ React: {len([q for q in questions if q[0]=='React'])}問追加")
    
    # ==================== COBOL問題 ====================
    print("[2/6] COBOL問題を生成中...")
    
    cobol_questions = [
        ("COBOLプログラムの4つのDIVISIONの順序として正しいのはどれですか？",
         [{"id":"A","text":"IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE"},{"id":"B","text":"DATA, PROCEDURE, ENVIRONMENT, IDENTIFICATION"},{"id":"C","text":"PROCEDURE, DATA, ENVIRONMENT, IDENTIFICATION"},{"id":"D","text":"順序は自由"}],
         [0], "構造", "1", 5, "この順序が必須", "COBOLプログラムの基本構造"),
        
        ("COBOLで変数の最大桁数を指定する記号はどれですか？",
         [{"id":"A","text":"PIC 9(5)"},{"id":"B","text":"VAR[5]"},{"id":"C","text":"INT(5)"},{"id":"D","text":"NUM:5"}],
         [0], "データ定義", "2", 5, "PIC（PICTURE）で型と桁数を指定", "数値はPIC 9、文字はPIC X"),
        
        ("COBOLで処理手続きを記述するDIVISIONはどれですか？",
         [{"id":"A","text":"PROCEDURE DIVISION"},{"id":"B","text":"DATA DIVISION"},{"id":"C","text":"ENVIRONMENT DIVISION"},{"id":"D","text":"IDENTIFICATION DIVISION"}],
         [0], "構造", "1", 5, "PROCEDURE DIVISIONが処理ロジック部分", "プログラムの本体"),
        
        ("COBOLで条件分岐を行う構文はどれですか？",
         [{"id":"A","text":"IF ... THEN ... END-IF"},{"id":"B","text":"if (...) {}"},{"id":"C","text":"IF ... FI"},{"id":"D","text":"CASE ... END"}],
         [0], "制御構造", "2", 5, "IFとEND-IFで条件分岐", "構造化プログラミング"),
        
        ("COBOLで繰り返し処理を行う構文はどれですか？",
         [{"id":"A","text":"PERFORM"},{"id":"B","text":"LOOP"},{"id":"C","text":"FOR"},{"id":"D","text":"WHILE"}],
         [0], "制御構造", "2", 5, "PERFORMで反復処理", "段落単位で実行"),
        
        ("COBOLでファイルを開く動詞はどれですか？",
         [{"id":"A","text":"OPEN"},{"id":"B","text":"READ"},{"id":"C","text":"START"},{"id":"D","text":"BEGIN"}],
         [0], "ファイル操作", "2", 5, "OPENでファイルをオープン", "INPUT, OUTPUT, I-Oモード"),
        
        ("COBOLでファイルからレコードを読むコマンドはどれですか？",
         [{"id":"A","text":"READ"},{"id":"B","text":"GET"},{"id":"C","text":"FETCH"},{"id":"D","text":"LOAD"}],
         [0], "ファイル操作", "2", 5, "READでレコードを読み込む", "AT ENDで終了判定"),
        
        ("COBOLで数値計算を行う動詞はどれですか？",
         [{"id":"A","text":"COMPUTE"},{"id":"B","text":"CALC"},{"id":"C","text":"MATH"},{"id":"D","text":"EVAL"}],
         [0], "計算", "3", 5, "COMPUTEで算術式を評価", "ADD, SUBTRACTより柔軟"),
        
        ("COBOLでプログラムを終了する動詞はどれですか？",
         [{"id":"A","text":"STOP RUN"},{"id":"B","text":"END"},{"id":"C","text":"EXIT"},{"id":"D","text":"QUIT"}],
         [0], "制御", "1", 5, "STOP RUNでプログラム終了", "正常終了の基本"),
        
        ("COBOLで画面に出力する動詞はどれですか？",
         [{"id":"A","text":"DISPLAY"},{"id":"B","text":"PRINT"},{"id":"C","text":"WRITE"},{"id":"D","text":"SHOW"}],
         [0], "入出力", "1", 5, "DISPLAYで標準出力", "デバッグにも使用"),
    ]
    
    for q in cobol_questions[:15]:
        questions.append(create_question("COBOL", *q))
    
    print(f"  ✓ COBOL: {len([q for q in questions if q[0]=='COBOL'])}問追加")
    
    # ==================== VBA問題 ====================
    print("[3/6] VBA問題を生成中...")
    
    vba_questions = [
        ("VBAで定数を宣言するキーワードはどれですか？",
         [{"id":"A","text":"Const"},{"id":"B","text":"Dim"},{"id":"C","text":"Static"},{"id":"D","text":"Let"}],
         [0], "変数", "1", 5, "Constで定数を宣言", "変更不可の値を定義"),
        
        ("VBAで関数を定義するキーワードはどれですか？",
         [{"id":"A","text":"Function"},{"id":"B","text":"Sub"},{"id":"C","text":"Proc"},{"id":"D","text":"Method"}],
         [0], "関数", "1", 5, "Functionは戻り値あり、Subは戻り値なし", "用途に応じて使い分け"),
        
        ("VBAでセル範囲を指定する方法として正しいのはどれですか？",
         [{"id":"A","text":"Range(\"A1:B10\")"},{"id":"B","text":"Cell(\"A1:B10\")"},{"id":"C","text":"Area(\"A1:B10\")"},{"id":"D","text":"Select(\"A1:B10\")"}],
         [0], "Excel操作", "2", 5, "Rangeオブジェクトでセルを操作", "Excel VBAの基本"),
        
        ("VBAでセルの値を取得するプロパティはどれですか？",
         [{"id":"A","text":"Value"},{"id":"B","text":"Text"},{"id":"C","text":"Data"},{"id":"D","text":"Content"}],
         [0], "Excel操作", "2", 5, "Valueプロパティで値を取得・設定", "最も基本的な操作"),
        
        ("VBAで条件分岐を行う構文はどれですか？",
         [{"id":"A","text":"If ... Then ... End If"},{"id":"B","text":"if (...) {}"},{"id":"C","text":"IF ... FI"},{"id":"D","text":"when ... then"}],
         [0], "制御構造", "1", 5, "If文で条件分岐", "ElseIfやElseも使用可能"),
        
        ("VBAで繰り返し処理を行う構文として正しいのはどれですか？",
         [{"id":"A","text":"For i = 1 To 10"},{"id":"B","text":"for (i=1; i<=10; i++)"},{"id":"C","text":"loop i from 1 to 10"},{"id":"D","text":"repeat 10 times"}],
         [0], "制御構造", "2", 5, "For...Nextループで反復処理", "回数指定のループ"),
        
        ("VBAでコレクション内の各要素を処理する構文はどれですか？",
         [{"id":"A","text":"For Each ... Next"},{"id":"B","text":"ForAll"},{"id":"C","text":"Each ... Do"},{"id":"D","text":"Loop Each"}],
         [0], "制御構造", "2", 5, "For Each...Nextでコレクション走査", "範囲やWorksheetなどに使用"),
        
        ("VBAでメッセージボックスを表示する関数はどれですか？",
         [{"id":"A","text":"MsgBox"},{"id":"B","text":"Alert"},{"id":"C","text":"MessageBox"},{"id":"D","text":"ShowMessage"}],
         [0], "ダイアログ", "1", 5, "MsgBoxでメッセージを表示", "ユーザーへの通知"),
        
        ("VBAでエラーを無視する構文はどれですか？",
         [{"id":"A","text":"On Error Resume Next"},{"id":"B","text":"Try ... Catch"},{"id":"C","text":"Ignore Error"},{"id":"D","text":"Skip Error"}],
         [0], "エラー処理", "3", 5, "On Error Resume Nextで次の行に進む", "エラー処理の基本"),
        
        ("VBAで配列を宣言する構文はどれですか？",
         [{"id":"A","text":"Dim arr(10) As Integer"},{"id":"B","text":"Dim arr[10] As Integer"},{"id":"C","text":"Integer arr[10]"},{"id":"D","text":"Array arr(10)"}],
         [0], "配列", "2", 5, "Dim 配列名(サイズ) As 型で宣言", "複数データの管理"),
    ]
    
    for q in vba_questions[:15]:
        questions.append(create_question("VBA", *q))
    
    print(f"  ✓ VBA: {len([q for q in questions if q[0]=='VBA'])}問追加")
    
    # ==================== 既存言語の追加 ====================
    print("[4/6] C#追加問題を生成中...")
    
    csharp_more = [
        ("C#でLINQを使って配列をフィルタリングする方法はどれですか？",
         [{"id":"A","text":"arr.Where(x => x > 5)"},{"id":"B","text":"arr.filter(x => x > 5)"},{"id":"C","text":"arr.select(x > 5)"},{"id":"D","text":"arr.find(x > 5)"}],
         [0], "LINQ", "4", 10, "WhereでフィルタリングクエリO式", "LINQの基本メソッド"),
        
        ("UnityでRigidbodyに力を加えるメソッドはどれですか？",
         [{"id":"A","text":"AddForce()"},{"id":"B","text":"ApplyForce()"},{"id":"C","text":"PushForce()"},{"id":"D","text":"SetForce()"}],
         [0], "Unity Physics", "3", 5, "AddForce()で物理的な力を加える", "物理演算の基本"),
    ]
    
    for q in csharp_more:
        questions.append(create_question("C#", *q))
    
    print(f"  ✓ C#: {len([q for q in questions if q[0]=='C#'])}問追加")
    
    print("[5/6] Go追加問題を生成中...")
    
    go_more = [
        ("Goでエラーを返す慣習的なパターンはどれですか？",
         [{"id":"A","text":"func f() (Type, error)"},{"id":"B","text":"func f() throws Type"},{"id":"C","text":"func f() Type or Error"},{"id":"D","text":"func f() try Type"}],
         [0], "エラー処理", "3", 5, "正常値とerrorを返すのが慣習", "Goのエラーハンドリングパターン"),
    ]
    
    for q in go_more:
        questions.append(create_question("Go", *q))
    
    print(f"  ✓ Go: {len([q for q in questions if q[0]=='Go'])}問追加")
    
    print("[6/6] TypeScript追加問題を生成中...")
    
    ts_more = [
        ("TypeScriptでインターセクション型を表す記号はどれですか？",
         [{"id":"A","text":"&"},{"id":"B","text":"|"},{"id":"C","text":"+"},{"id":"D","text":"*"}],
         [0], "型定義", "4", 10, "&で複数の型を結合", "型の合成に使用"),
        
        ("TypeScriptでtype aliasを定義するキーワードはどれですか？",
         [{"id":"A","text":"type"},{"id":"B","text":"alias"},{"id":"C","text":"typedef"},{"id":"D","text":"define"}],
         [0], "型定義", "3", 5, "type 名前 = 型 の形式", "interfaceと使い分け"),
        
        ("TypeScriptでジェネリクスの構文はどれですか？",
         [{"id":"A","text":"function f<T>(arg: T)"},{"id":"B","text":"function f[T](arg: T)"},{"id":"C","text":"function f(T)(arg: T)"},{"id":"D","text":"function f{T}(arg: T)"}],
         [0], "ジェネリクス", "4", 10, "<T>で型パラメータを宣言", "再利用可能な型定義"),
    ]
    
    for q in ts_more:
        questions.append(create_question("TypeScript", *q))
    
    print(f"  ✓ TypeScript: {len([q for q in questions if q[0]=='TypeScript'])}問追加")
    
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
    print("✓ 問題追加完了（第4弾）！")
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
    add_questions_batchfour()