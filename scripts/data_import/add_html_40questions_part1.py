import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_html_40_questions_part1():
    """HTML問題40問追加（第1弾：20問→60問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("HTML問題追加スクリプト（第1弾：40問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== セマンティックHTML（10問） ====================
    print("[1/4] セマンティックHTML問題を生成中...")
    
    semantic = [
        ("<header>タグの用途は？",
         [{"id":"A","text":"ページやセクションのヘッダー"},{"id":"B","text":"見出し"},{"id":"C","text":"タイトル"},{"id":"D","text":"画像"}],
         [0], "セマンティックHTML", "1", 5, "ヘッダー領域", "header"),
        
        ("<nav>タグの用途は？",
         [{"id":"A","text":"ナビゲーションリンク"},{"id":"B","text":"ページ全体"},{"id":"C","text":"フッター"},{"id":"D","text":"サイドバー"}],
         [0], "セマンティックHTML", "1", 5, "ナビゲーション", "nav"),
        
        ("<main>タグの用途は？",
         [{"id":"A","text":"ページの主要コンテンツ"},{"id":"B","text":"全てのコンテンツ"},{"id":"C","text":"サイドバー"},{"id":"D","text":"フッター"}],
         [0], "セマンティックHTML", "2", 8, "メインコンテンツ", "main"),
        
        ("<article>タグの用途は？",
         [{"id":"A","text":"独立したコンテンツ（記事など）"},{"id":"B","text":"段落"},{"id":"C","text":"見出し"},{"id":"D","text":"リスト"}],
         [0], "セマンティックHTML", "2", 8, "記事コンテンツ", "article"),
        
        ("<section>タグの用途は？",
         [{"id":"A","text":"意味的なセクション"},{"id":"B","text":"スタイル用"},{"id":"C","text":"レイアウト用"},{"id":"D","text":"非推奨"}],
         [0], "セマンティックHTML", "2", 8, "セクション分け", "section"),
        
        ("<aside>タグの用途は？",
         [{"id":"A","text":"補足コンテンツ（サイドバー等）"},{"id":"B","text":"メインコンテンツ"},{"id":"C","text":"フッター"},{"id":"D","text":"ヘッダー"}],
         [0], "セマンティックHTML", "2", 8, "補足情報", "aside"),
        
        ("<footer>タグの用途は？",
         [{"id":"A","text":"ページやセクションのフッター"},{"id":"B","text":"ヘッダー"},{"id":"C","text":"メイン"},{"id":"D","text":"ナビ"}],
         [0], "セマンティックHTML", "1", 5, "フッター領域", "footer"),
        
        ("<figure>と<figcaption>の関係は？",
         [{"id":"A","text":"図表とそのキャプション"},{"id":"B","text":"画像と説明"},{"id":"C","text":"関係なし"},{"id":"D","text":"非推奨"}],
         [0], "セマンティックHTML", "3", 10, "図表とキャプション", "figure"),
        
        ("<time>タグの用途は？",
         [{"id":"A","text":"日時の表現"},{"id":"B","text":"タイマー"},{"id":"C","text":"時計表示"},{"id":"D","text":"非推奨"}],
         [0], "セマンティックHTML", "2", 8, "日時マークアップ", "time"),
        
        ("<mark>タグの用途は？",
         [{"id":"A","text":"ハイライト表示"},{"id":"B","text":"太字"},{"id":"C","text":"斜体"},{"id":"D","text":"下線"}],
         [0], "セマンティックHTML", "2", 8, "強調表示", "mark"),
    ]
    
    questions.extend(semantic)
    print(f"  ✓ セマンティックHTML: {len(semantic)}問")
    
    # ==================== フォーム詳細（15問） ====================
    print("[2/4] フォーム詳細問題を生成中...")
    
    forms = [
        ("<input type=\"email\">の特徴は？",
         [{"id":"A","text":"メールアドレス形式の検証"},{"id":"B","text":"パスワード入力"},{"id":"C","text":"数値入力"},{"id":"D","text":"通常テキスト"}],
         [0], "フォーム", "2", 8, "メール入力", "email"),
        
        ("<input type=\"number\">の特徴は？",
         [{"id":"A","text":"数値入力専用"},{"id":"B","text":"テキスト入力"},{"id":"C","text":"日付入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "1", 5, "数値入力", "number"),
        
        ("<input type=\"date\">の特徴は？",
         [{"id":"A","text":"日付選択UI提供"},{"id":"B","text":"テキスト入力"},{"id":"C","text":"時刻入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "日付入力", "date"),
        
        ("<input type=\"color\">の特徴は？",
         [{"id":"A","text":"カラーピッカー表示"},{"id":"B","text":"テキスト入力"},{"id":"C","text":"数値入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "色選択", "color"),
        
        ("<input type=\"range\">の特徴は？",
         [{"id":"A","text":"スライダーUI"},{"id":"B","text":"テキスト入力"},{"id":"C","text":"チェックボックス"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "範囲選択", "range"),
        
        ("<input type=\"tel\">の用途は？",
         [{"id":"A","text":"電話番号入力"},{"id":"B","text":"メール入力"},{"id":"C","text":"URL入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "電話番号", "tel"),
        
        ("<input type=\"url\">の特徴は？",
         [{"id":"A","text":"URL形式の検証"},{"id":"B","text":"メール検証"},{"id":"C","text":"テキスト入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "URL入力", "url"),
        
        ("required属性の役割は？",
         [{"id":"A","text":"必須入力にする"},{"id":"B","text":"読み取り専用"},{"id":"C","text":"無効化"},{"id":"D","text":"非表示"}],
         [0], "フォーム", "1", 5, "必須項目", "required"),
        
        ("placeholder属性の役割は？",
         [{"id":"A","text":"入力例の表示"},{"id":"B","text":"デフォルト値設定"},{"id":"C","text":"ラベル表示"},{"id":"D","text":"バリデーション"}],
         [0], "フォーム", "1", 5, "プレースホルダー", "placeholder"),
        
        ("pattern属性の役割は？",
         [{"id":"A","text":"正規表現で入力検証"},{"id":"B","text":"パターンマッチ"},{"id":"C","text":"スタイル適用"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "3", 10, "正規表現検証", "pattern"),
        
        ("min/max属性の用途は？",
         [{"id":"A","text":"数値や日付の範囲指定"},{"id":"B","text":"文字数制限"},{"id":"C","text":"スタイル指定"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "範囲制限", "min/max"),
        
        ("maxlength属性の役割は？",
         [{"id":"A","text":"最大文字数制限"},{"id":"B","text":"最小文字数"},{"id":"C","text":"数値範囲"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "1", 5, "文字数制限", "maxlength"),
        
        ("<datalist>タグの用途は？",
         [{"id":"A","text":"入力候補リスト"},{"id":"B","text":"データ保存"},{"id":"C","text":"テーブル"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "3", 10, "オートコンプリート", "datalist"),
        
        ("<textarea>のcols/rows属性は？",
         [{"id":"A","text":"列数と行数の指定"},{"id":"B","text":"文字数制限"},{"id":"C","text":"スタイル指定"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "テキストエリアサイズ", "textarea"),
        
        ("autocomplete=\"off\"の効果は？",
         [{"id":"A","text":"自動補完を無効化"},{"id":"B","text":"自動補完を有効化"},{"id":"C","text":"必須入力"},{"id":"D","text":"非推奨"}],
         [0], "フォーム", "2", 8, "自動補完制御", "autocomplete"),
    ]
    
    questions.extend(forms)
    print(f"  ✓ フォーム詳細: {len(forms)}問")
    
    # ==================== メタデータ・SEO（8問） ====================
    print("[3/4] メタデータ・SEO問題を生成中...")
    
    meta_seo = [
        ("<meta charset=\"UTF-8\">の役割は？",
         [{"id":"A","text":"文字エンコーディング指定"},{"id":"B","text":"言語指定"},{"id":"C","text":"タイトル設定"},{"id":"D","text":"非推奨"}],
         [0], "メタデータ", "1", 5, "文字コード", "charset"),
        
        ("<meta name=\"viewport\">の役割は？",
         [{"id":"A","text":"レスポンシブ対応の設定"},{"id":"B","text":"文字コード"},{"id":"C","text":"タイトル"},{"id":"D","text":"非推奨"}],
         [0], "メタデータ", "2", 8, "ビューポート設定", "viewport"),
        
        ("<meta name=\"description\">の役割は？",
         [{"id":"A","text":"ページ説明（検索結果に表示）"},{"id":"B","text":"タイトル"},{"id":"C","text":"キーワード"},{"id":"D","text":"非推奨"}],
         [0], "メタデータ", "2", 8, "ページ概要", "description"),
        
        ("<meta name=\"keywords\">の現在の扱いは？",
         [{"id":"A","text":"SEO効果はほぼなし"},{"id":"B","text":"必須項目"},{"id":"C","text":"最重要"},{"id":"D","text":"禁止"}],
         [0], "メタデータ", "3", 10, "キーワードタグ", "keywords"),
        
        ("<link rel=\"canonical\">の役割は？",
         [{"id":"A","text":"正規URL指定（重複コンテンツ対策）"},{"id":"B","text":"スタイルシート読み込み"},{"id":"C","text":"JavaScript読み込み"},{"id":"D","text":"非推奨"}],
         [0], "SEO", "4", 12, "正規URL", "canonical"),
        
        ("OGP（Open Graph Protocol）の用途は？",
         [{"id":"A","text":"SNSシェア時の表示制御"},{"id":"B","text":"SEO対策"},{"id":"C","text":"アクセス解析"},{"id":"D","text":"非推奨"}],
         [0], "SEO", "3", 10, "SNS最適化", "OGP"),
        
        ("<meta property=\"og:title\">の役割は？",
         [{"id":"A","text":"SNSシェア時のタイトル"},{"id":"B","text":"ページタイトル"},{"id":"C","text":"見出し"},{"id":"D","text":"非推奨"}],
         [0], "SEO", "2", 8, "OGタイトル", "og:title"),
        
        ("<link rel=\"icon\">の役割は？",
         [{"id":"A","text":"ファビコン指定"},{"id":"B","text":"スタイルシート"},{"id":"C","text":"JavaScript"},{"id":"D","text":"非推奨"}],
         [0], "メタデータ", "1", 5, "ファビコン", "icon"),
    ]
    
    questions.extend(meta_seo)
    print(f"  ✓ メタデータ・SEO: {len(meta_seo)}問")
    
    # ==================== メディア・埋め込み（7問） ====================
    print("[4/4] メディア・埋め込み問題を生成中...")
    
    media = [
        ("<video>のcontrols属性の役割は？",
         [{"id":"A","text":"再生コントロール表示"},{"id":"B","text":"自動再生"},{"id":"C","text":"ループ再生"},{"id":"D","text":"ミュート"}],
         [0], "メディア", "1", 5, "動画コントロール", "controls"),
        
        ("<video>のautoplay属性の効果は？",
         [{"id":"A","text":"自動再生"},{"id":"B","text":"コントロール表示"},{"id":"C","text":"ループ"},{"id":"D","text":"ミュート"}],
         [0], "メディア", "1", 5, "自動再生", "autoplay"),
        
        ("<audio>のloop属性の効果は？",
         [{"id":"A","text":"ループ再生"},{"id":"B","text":"自動再生"},{"id":"C","text":"コントロール表示"},{"id":"D","text":"ミュート"}],
         [0], "メディア", "1", 5, "繰り返し再生", "loop"),
        
        ("<picture>タグの用途は？",
         [{"id":"A","text":"レスポンシブ画像の提供"},{"id":"B","text":"通常の画像"},{"id":"C","text":"動画"},{"id":"D","text":"非推奨"}],
         [0], "メディア", "3", 10, "レスポンシブ画像", "picture"),
        
        ("<img>のsrcset属性の役割は？",
         [{"id":"A","text":"複数解像度の画像指定"},{"id":"B","text":"画像パス"},{"id":"C","text":"代替テキスト"},{"id":"D","text":"非推奨"}],
         [0], "メディア", "3", 10, "高解像度対応", "srcset"),
        
        ("<img>のloading=\"lazy\"の効果は？",
         [{"id":"A","text":"遅延読み込み（スクロール時に読み込み）"},{"id":"B","text":"即座に読み込み"},{"id":"C","text":"読み込まない"},{"id":"D","text":"非推奨"}],
         [0], "メディア", "3", 10, "遅延ロード", "lazy"),
        
        ("<iframe>のsandbox属性の役割は？",
         [{"id":"A","text":"セキュリティ制限の適用"},{"id":"B","text":"スタイル指定"},{"id":"C","text":"サイズ指定"},{"id":"D","text":"非推奨"}],
         [0], "埋め込み", "4", 12, "iframe制限", "sandbox"),
    ]
    
    questions.extend(media)
    print(f"  ✓ メディア・埋め込み: {len(media)}問")
    
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
        """, ("HTML", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'HTML'")
    html_count = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'HTML' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊 HTML第1弾完了！ 🎊")
    print("=" * 60)
    print(f"HTML問題数: {html_count}問 (20問 → {html_count}問)")
    print(f"全体問題数: {total_count}問")
    
    print("\n【HTMLカテゴリ別内訳】")
    for cat, count in categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("✅ Phase 1 - フロントエンド基礎（進行中）")
    print("\n【達成状況】")
    print("  ✅ React: 80問 / 80問 ← 完了！")
    print("  ✅ CSS: 100問 / 100問 ← 完了！")
    print(f"  🔄 HTML: {html_count}問 / 80問（あと{80-html_count}問）")
    print("\n次のステップ:")
    print("  → HTML第2弾（+20問）で80問達成！")
    print("=" * 60)

if __name__ == "__main__":
    add_html_40_questions_part1()