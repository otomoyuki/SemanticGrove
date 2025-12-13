import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_questions_batch2():
    """問題追加（第2弾）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("問題追加スクリプト（第2弾）")
    print("=" * 60)
    
    cursor.execute("SELECT language, COUNT(*) FROM questions GROUP BY language")
    existing = dict(cursor.fetchall())
    
    print("\n現在の問題数:")
    for lang, count in sorted(existing.items()):
        print(f"  {lang}: {count}問")
    
    print("\n問題を追加中...")
    questions = []
    
    # ==================== JavaScript追加問題 ====================
    print("[1/5] JavaScript追加問題を生成中...")
    
    js_more = [
        ("次のコードの出力は？\nconsole.log(0 == false);",
         [{"id":"A","text":"true"},{"id":"B","text":"false"},{"id":"C","text":"undefined"},{"id":"D","text":"エラー"}],
         [0], "型変換", "2", 5, "0とfalseは==で比較すると等しい", "==は型変換を行うため注意が必要"),
        
        ("配列の先頭に要素を追加するメソッドはどれですか？",
         [{"id":"A","text":"unshift()"},{"id":"B","text":"push()"},{"id":"C","text":"shift()"},{"id":"D","text":"pop()"}],
         [0], "配列", "2", 5, "unshift()は配列の先頭に要素を追加", "キューのような動作を実現"),
        
        ("オブジェクトのプロパティを削除する演算子はどれですか？",
         [{"id":"A","text":"delete"},{"id":"B","text":"remove"},{"id":"C","text":"clear"},{"id":"D","text":"unset"}],
         [0], "オブジェクト", "3", 5, "delete演算子でプロパティを削除", "動的なオブジェクト操作に使用"),
        
        ("配列から特定の要素のインデックスを取得するメソッドはどれですか？",
         [{"id":"A","text":"indexOf()"},{"id":"B","text":"findIndex()"},{"id":"C","text":"search()"},{"id":"D","text":"locate()"}],
         [0], "配列", "3", 5, "indexOf()は要素の位置を返す（なければ-1）", "要素の存在確認に使用"),
        
        ("配列の一部を抽出するメソッドはどれですか？",
         [{"id":"A","text":"slice()"},{"id":"B","text":"splice()"},{"id":"C","text":"split()"},{"id":"D","text":"substr()"}],
         [0], "配列", "3", 5, "slice()は元配列を変更せず一部を抽出", "配列のコピーにも使用"),
        
        ("テンプレートリテラルの正しい構文はどれですか？",
         [{"id":"A","text":"`Hello ${name}`"},{"id":"B","text":"'Hello ${name}'"},{"id":"C","text":"\"Hello ${name}\""},{"id":"D","text":"'Hello ' + name"}],
         [0], "ES6", "4", 10, "バッククォートで囲み${変数}で埋め込み", "文字列の組み立てを簡潔に"),
        
        ("スプレッド構文の正しい使い方はどれですか？",
         [{"id":"A","text":"[...arr1, ...arr2]"},{"id":"B","text":"[..arr1, ..arr2]"},{"id":"C","text":"[*arr1, *arr2]"},{"id":"D","text":"[+arr1, +arr2]"}],
         [0], "ES6", "4", 10, "...で配列やオブジェクトを展開", "配列の結合やコピーに便利"),
        
        ("デフォルト引数の正しい構文はどれですか？",
         [{"id":"A","text":"function greet(name = 'Guest') {}"},{"id":"B","text":"function greet(name := 'Guest') {}"},{"id":"C","text":"function greet(name || 'Guest') {}"},{"id":"D","text":"function greet(name default 'Guest') {}"}],
         [0], "関数", "4", 10, "引数名=デフォルト値の形式で指定", "関数の柔軟性を高める"),
        
        ("配列の累積計算を行うメソッドはどれですか？",
         [{"id":"A","text":"reduce()"},{"id":"B","text":"map()"},{"id":"C","text":"filter()"},{"id":"D","text":"forEach()"}],
         [0], "配列メソッド", "5", 15, "reduce()は配列を1つの値に集約", "合計値の計算などに使用"),
        
        ("try-catchでエラーを投げる構文はどれですか？",
         [{"id":"A","text":"throw new Error('message')"},{"id":"B","text":"raise Error('message')"},{"id":"C","text":"error('message')"},{"id":"D","text":"exception('message')"}],
         [0], "エラー処理", "5", 15, "throw文でエラーを発生させる", "意図的なエラー発生に使用"),
    ]
    
    for q in js_more:
        questions.append(create_question("JavaScript", *q))
    
    print(f"  ✓ JavaScript: {len(js_more)}問追加")
    
    # ==================== Python追加問題 ====================
    print("[2/5] Python追加問題を生成中...")
    
    python_more = [
        ("Pythonでセットを作成する構文はどれですか？",
         [{"id":"A","text":"{1, 2, 3}"},{"id":"B","text":"[1, 2, 3]"},{"id":"C","text":"(1, 2, 3)"},{"id":"D","text":"<1, 2, 3>"}],
         [0], "データ型", "2", 5, "{}で囲むとセット（重複なし集合）", "重複削除や集合演算に使用"),
        
        ("Pythonで例外を捕捉する構文はどれですか？",
         [{"id":"A","text":"try-except"},{"id":"B","text":"try-catch"},{"id":"C","text":"try-error"},{"id":"D","text":"begin-rescue"}],
         [0], "例外処理", "3", 5, "exceptブロックで例外を処理", "エラーの安全な処理に必須"),
        
        ("リストの要素を逆順にするメソッドはどれですか？",
         [{"id":"A","text":"reverse()"},{"id":"B","text":"reversed()"},{"id":"C","text":"flip()"},{"id":"D","text":"invert()"}],
         [0], "リスト", "2", 5, "reverse()はリストを直接逆順にする", "データの並び替えに使用"),
        
        ("文字列を大文字に変換するメソッドはどれですか？",
         [{"id":"A","text":"upper()"},{"id":"B","text":"uppercase()"},{"id":"C","text":"toUpper()"},{"id":"D","text":"capitalize()"}],
         [0], "文字列", "2", 5, "upper()は全て大文字に変換", "文字列の正規化に使用"),
        
        ("辞書に新しいキーを追加する方法はどれですか？",
         [{"id":"A","text":"dict['key'] = value"},{"id":"B","text":"dict.add('key', value)"},{"id":"C","text":"dict.insert('key', value)"},{"id":"D","text":"dict.append('key', value)"}],
         [0], "辞書", "2", 5, "直接代入で追加または更新", "辞書の動的な操作"),
        
        ("lambda関数の正しい構文はどれですか？",
         [{"id":"A","text":"lambda x: x * 2"},{"id":"B","text":"lambda x => x * 2"},{"id":"C","text":"lambda x -> x * 2"},{"id":"D","text":"x => x * 2"}],
         [0], "関数", "3", 5, "lambda 引数: 式の形式で無名関数を定義", "簡単な関数を簡潔に記述"),
        
        ("文字列のフォーマット方法として正しいのはどれですか？",
         [{"id":"A","text":"f'Hello {name}'"},{"id":"B","text":"'Hello {name}'.format(name)"},{"id":"C","text":"'Hello %s' % name"},{"id":"D","text":"すべて正しい"}],
         [3], "文字列", "3", 5, "f-string、format()、%演算子が使える", "f-stringが最も推奨される"),
        
        ("リストの要素数を数えるメソッドはどれですか？",
         [{"id":"A","text":"count()"},{"id":"B","text":"length()"},{"id":"C","text":"size()"},{"id":"D","text":"len()"}],
         [0], "リスト", "2", 5, "count()は特定要素の出現回数を返す", "要素の頻度分析に使用"),
        
        ("辞書のキーと値のペアを取得するメソッドはどれですか？",
         [{"id":"A","text":"items()"},{"id":"B","text":"pairs()"},{"id":"C","text":"entries()"},{"id":"D","text":"tuples()"}],
         [0], "辞書", "3", 5, "items()はタプルのリストを返す", "辞書のループ処理で使用"),
        
        ("リストをソートした新しいリストを返す関数はどれですか？",
         [{"id":"A","text":"sorted()"},{"id":"B","text":"sort()"},{"id":"C","text":"order()"},{"id":"D","text":"arrange()"}],
         [0], "組み込み関数", "3", 5, "sorted()は元を変更せず新リストを返す", "元データを保持したい場合に使用"),
        
        ("ファイルを開く正しい方法はどれですか？",
         [{"id":"A","text":"with open('file.txt') as f:"},{"id":"B","text":"open('file.txt') as f:"},{"id":"C","text":"file = open('file.txt')"},{"id":"D","text":"両方A,C"}],
         [3], "ファイル操作", "4", 10, "withを使うと自動でクローズされる", "リソース管理のベストプラクティス"),
        
        ("ジェネレータを作成するキーワードはどれですか？",
         [{"id":"A","text":"yield"},{"id":"B","text":"return"},{"id":"C","text":"generate"},{"id":"D","text":"next"}],
         [0], "ジェネレータ", "5", 15, "yieldは値を返しつつ状態を保持", "大きなデータの効率的処理に使用"),
        
        ("デコレータの正しい構文はどれですか？",
         [{"id":"A","text":"@decorator"},{"id":"B","text":"#decorator"},{"id":"C","text":"[decorator]"},{"id":"D","text":"{decorator}"}],
         [0], "デコレータ", "5", 15, "@記号で関数を装飾", "関数の機能拡張に使用"),
    ]
    
    for q in python_more:
        questions.append(create_question("Python", *q))
    
    print(f"  ✓ Python: {len(python_more)}問追加")
    
    # ==================== HTML問題 ====================
    print("[3/5] HTML問題を生成中...")
    
    html_questions = [
        ("HTMLで段落を作成するタグはどれですか？",
         [{"id":"A","text":"<p>"},{"id":"B","text":"<paragraph>"},{"id":"C","text":"<text>"},{"id":"D","text":"<div>"}],
         [0], "基本タグ", "1", 5, "<p>タグで段落を作成", "テキストの基本単位"),
        
        ("HTMLでリンクを作成するタグはどれですか？",
         [{"id":"A","text":"<a>"},{"id":"B","text":"<link>"},{"id":"C","text":"<href>"},{"id":"D","text":"<url>"}],
         [0], "基本タグ", "1", 5, "<a>タグとhref属性でリンクを作成", "ページ間の移動に使用"),
        
        ("HTMLで画像を表示するタグはどれですか？",
         [{"id":"A","text":"<img>"},{"id":"B","text":"<image>"},{"id":"C","text":"<picture>"},{"id":"D","text":"<photo>"}],
         [0], "基本タグ", "1", 5, "<img>タグとsrc属性で画像を表示", "視覚コンテンツの表示"),
        
        ("HTMLで順序なしリストを作成するタグはどれですか？",
         [{"id":"A","text":"<ul>"},{"id":"B","text":"<ol>"},{"id":"C","text":"<list>"},{"id":"D","text":"<items>"}],
         [0], "リスト", "2", 5, "<ul>は箇条書きリスト", "箇条書きの表現に使用"),
        
        ("HTMLで順序付きリストを作成するタグはどれですか？",
         [{"id":"A","text":"<ol>"},{"id":"B","text":"<ul>"},{"id":"C","text":"<list>"},{"id":"D","text":"<numbered>"}],
         [0], "リスト", "2", 5, "<ol>は番号付きリスト", "手順の表現に使用"),
        
        ("HTMLでテーブルを作成する基本タグはどれですか？",
         [{"id":"A","text":"<table>"},{"id":"B","text":"<tab>"},{"id":"C","text":"<grid>"},{"id":"D","text":"<data>"}],
         [0], "テーブル", "2", 5, "<table>でテーブル構造を作成", "データの表形式表示"),
        
        ("HTMLでフォームを作成するタグはどれですか？",
         [{"id":"A","text":"<form>"},{"id":"B","text":"<input>"},{"id":"C","text":"<submit>"},{"id":"D","text":"<field>"}],
         [0], "フォーム", "2", 5, "<form>でデータ送信フォームを作成", "ユーザー入力の受付"),
        
        ("HTMLで改行するタグはどれですか？",
         [{"id":"A","text":"<br>"},{"id":"B","text":"<break>"},{"id":"C","text":"<newline>"},{"id":"D","text":"<line>"}],
         [0], "基本タグ", "1", 5, "<br>で改行を挿入", "テキストの改行"),
        
        ("HTML5のセマンティック要素はどれですか？",
         [{"id":"A","text":"<header>"},{"id":"B","text":"<div>"},{"id":"C","text":"<span>"},{"id":"D","text":"<block>"}],
         [0], "HTML5", "3", 5, "<header>は意味のある区分を示す", "構造の明確化とSEO向上"),
        
        ("HTMLでメタ情報を記述するタグはどれですか？",
         [{"id":"A","text":"<meta>"},{"id":"B","text":"<info>"},{"id":"C","text":"<data>"},{"id":"D","text":"<metadata>"}],
         [0], "メタデータ", "3", 5, "<meta>で文字コードやSEO情報を記述", "ページの基本情報定義"),
    ]
    
    for q in html_questions:
        questions.append(create_question("HTML", *q))
    
    print(f"  ✓ HTML: {len(html_questions)}問追加")
    
    # ==================== CSS問題 ====================
    print("[4/5] CSS問題を生成中...")
    
    css_questions = [
        ("CSSでフォントサイズを指定するプロパティはどれですか？",
         [{"id":"A","text":"font-size"},{"id":"B","text":"text-size"},{"id":"C","text":"size"},{"id":"D","text":"font"}],
         [0], "フォント", "1", 5, "font-sizeでフォントの大きさを指定", "テキストの視認性調整"),
        
        ("CSSで要素を中央揃えにするプロパティはどれですか？",
         [{"id":"A","text":"text-align: center"},{"id":"B","text":"align: center"},{"id":"C","text":"center: true"},{"id":"D","text":"position: center"}],
         [0], "配置", "2", 5, "text-align: centerでテキストを中央揃え", "デザインの基本"),
        
        ("CSSでマージンを指定するプロパティはどれですか？",
         [{"id":"A","text":"margin"},{"id":"B","text":"padding"},{"id":"C","text":"border"},{"id":"D","text":"spacing"}],
         [0], "ボックスモデル", "2", 5, "marginは要素外側の余白", "レイアウト調整の基本"),
        
        ("CSSでパディングを指定するプロパティはどれですか？",
         [{"id":"A","text":"padding"},{"id":"B","text":"margin"},{"id":"C","text":"space"},{"id":"D","text":"gap"}],
         [0], "ボックスモデル", "2", 5, "paddingは要素内側の余白", "コンテンツの余裕を作る"),
        
        ("CSSでボーダーを指定する省略記法はどれですか？",
         [{"id":"A","text":"border: 1px solid black"},{"id":"B","text":"border: black 1px solid"},{"id":"C","text":"border: solid black 1px"},{"id":"D","text":"すべて正しい"}],
         [0], "ボーダー", "2", 5, "太さ スタイル 色の順で指定", "枠線の描画"),
        
        ("CSSでフレックスボックスを使うプロパティはどれですか？",
         [{"id":"A","text":"display: flex"},{"id":"B","text":"flex: true"},{"id":"C","text":"flexbox: on"},{"id":"D","text":"layout: flex"}],
         [0], "レイアウト", "3", 5, "display: flexでフレックスコンテナに", "柔軟なレイアウト実現"),
        
        ("CSSでグリッドレイアウトを使うプロパティはどれですか？",
         [{"id":"A","text":"display: grid"},{"id":"B","text":"grid: true"},{"id":"C","text":"layout: grid"},{"id":"D","text":"gridbox: on"}],
         [0], "レイアウト", "3", 5, "display: gridでグリッドコンテナに", "複雑なレイアウトの実現"),
        
        ("CSSで要素を非表示にするプロパティはどれですか？",
         [{"id":"A","text":"display: none"},{"id":"B","text":"visibility: hidden"},{"id":"C","text":"両方正しい"},{"id":"D","text":"hide: true"}],
         [2], "表示制御", "3", 5, "display: noneは領域ごと削除", "要素の表示/非表示切り替え"),
        
        ("CSSで要素を重ねる順序を指定するプロパティはどれですか？",
         [{"id":"A","text":"z-index"},{"id":"B","text":"layer"},{"id":"C","text":"depth"},{"id":"D","text":"order"}],
         [0], "配置", "3", 5, "z-indexで重なり順を制御", "レイヤー管理に使用"),
        
        ("CSSアニメーションを定義するルールはどれですか？",
         [{"id":"A","text":"@keyframes"},{"id":"B","text":"@animation"},{"id":"C","text":"@animate"},{"id":"D","text":"@transition"}],
         [0], "アニメーション", "4", 10, "@keyframesでアニメーションを定義", "動的な表現の実現"),
    ]
    
    for q in css_questions:
        questions.append(create_question("CSS", *q))
    
    print(f"  ✓ CSS: {len(css_questions)}問追加")
    
    # ==================== TypeScript問題 ====================
    print("[5/5] TypeScript問題を生成中...")
    
    ts_questions = [
        ("TypeScriptで数値型を指定する型注釈はどれですか？",
         [{"id":"A","text":"number"},{"id":"B","text":"Number"},{"id":"C","text":"int"},{"id":"D","text":"float"}],
         [0], "型注釈", "1", 5, "numberは数値型を表す", "型の基本"),
        
        ("TypeScriptで配列の型を指定する方法はどれですか？",
         [{"id":"A","text":"number[]"},{"id":"B","text":"Array<number>"},{"id":"C","text":"両方正しい"},{"id":"D","text":"[number]"}],
         [2], "型注釈", "2", 5, "number[]またはArray<number>で指定", "配列の型安全性"),
        
        ("TypeScriptでオプショナルなプロパティを示す記号はどれですか？",
         [{"id":"A","text":"?"},{"id":"B","text":"!"},{"id":"C","text":"*"},{"id":"D","text":"~"}],
         [0], "型注釈", "2", 5, "?で省略可能なプロパティを示す", "柔軟な型定義"),
        
        ("TypeScriptでインターフェースを定義するキーワードはどれですか？",
         [{"id":"A","text":"interface"},{"id":"B","text":"type"},{"id":"C","text":"class"},{"id":"D","text":"struct"}],
         [0], "型定義", "3", 5, "interfaceでオブジェクトの構造を定義", "型の再利用性向上"),
        
        ("TypeScriptでユニオン型を表す記号はどれですか？",
         [{"id":"A","text":"|"},{"id":"B","text":"&"},{"id":"C","text":"+"},{"id":"D","text":"||"}],
         [0], "型定義", "3", 5, "|で複数の型のいずれかを表す", "柔軟な型指定"),
    ]
    
    for q in ts_questions:
        questions.append(create_question("TypeScript", *q))
    
    print(f"  ✓ TypeScript: {len(ts_questions)}問追加")
    
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
    print("✓ 問題追加完了（第2弾）！")
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
    add_questions_batch2()