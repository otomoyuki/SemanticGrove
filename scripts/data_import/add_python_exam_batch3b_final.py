import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_python_exam_batch3b_final():
    """Python試験対策問題追加（第3弾-後半・最終50問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Python試験対策問題追加スクリプト（第3弾-後半・最終50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== データサイエンス基礎（25問） ====================
    print("[1/2] データサイエンス基礎問題を生成中...")
    
    datascience_questions = [
        ("NumPy の主な用途は？",
         [{"id":"A","text":"数値計算・配列操作"},{"id":"B","text":"Web開発"},{"id":"C","text":"データベース"},{"id":"D","text":"GUI"}],
         [0], "試験対策_データサイエンス", "3", 10, "科学計算ライブラリ", "NumPy"),
        
        ("pandas の主な用途は？",
         [{"id":"A","text":"データ分析・操作"},{"id":"B","text":"機械学習"},{"id":"C","text":"画像処理"},{"id":"D","text":"Web"}],
         [0], "試験対策_データサイエンス", "3", 10, "データフレーム", "pandas"),
        
        ("matplotlib の用途は？",
         [{"id":"A","text":"データ可視化"},{"id":"B","text":"データ収集"},{"id":"C","text":"データクリーニング"},{"id":"D","text":"モデル構築"}],
         [0], "試験対策_データサイエンス", "2", 8, "グラフ描画", "matplotlib"),
        
        ("DataFrame の特徴は？",
         [{"id":"A","text":"2次元ラベル付きデータ"},{"id":"B","text":"1次元のみ"},{"id":"C","text":"3次元"},{"id":"D","text":"配列"}],
         [0], "試験対策_データサイエンス", "3", 10, "表形式データ", "DataFrame"),
        
        ("Series の特徴は？",
         [{"id":"A","text":"1次元ラベル付きデータ"},{"id":"B","text":"2次元"},{"id":"C","text":"配列"},{"id":"D","text":"辞書"}],
         [0], "試験対策_データサイエンス", "3", 10, "列データ", "Series"),
        
        ("df.head() の役割は？",
         [{"id":"A","text":"先頭数行表示"},{"id":"B","text":"全体表示"},{"id":"C","text":"末尾表示"},{"id":"D","text":"統計表示"}],
         [0], "試験対策_データサイエンス", "2", 8, "データ確認", "head"),
        
        ("df.tail() の役割は？",
         [{"id":"A","text":"末尾数行表示"},{"id":"B","text":"先頭表示"},{"id":"C","text":"全体表示"},{"id":"D","text":"統計表示"}],
         [0], "試験対策_データサイエンス", "2", 8, "最後を確認", "tail"),
        
        ("df.describe() の役割は？",
         [{"id":"A","text":"統計情報表示"},{"id":"B","text":"データ表示"},{"id":"C","text":"型情報"},{"id":"D","text":"欠損値"}],
         [0], "試験対策_データサイエンス", "2", 8, "基本統計量", "describe"),
        
        ("df.info() の役割は？",
         [{"id":"A","text":"データ型・メモリ情報"},{"id":"B","text":"統計情報"},{"id":"C","text":"データ表示"},{"id":"D","text":"ソート"}],
         [0], "試験対策_データサイエンス", "2", 8, "データフレーム概要", "info"),
        
        ("df.isnull() の役割は？",
         [{"id":"A","text":"欠損値判定"},{"id":"B","text":"データ型"},{"id":"C","text":"統計"},{"id":"D","text":"削除"}],
         [0], "試験対策_データサイエンス", "2", 8, "NULL検出", "isnull"),
        
        ("df.fillna(0) の役割は？",
         [{"id":"A","text":"欠損値を0で埋める"},{"id":"B","text":"0を削除"},{"id":"C","text":"0を探す"},{"id":"D","text":"型変換"}],
         [0], "試験対策_データサイエンス", "2", 8, "欠損値補完", "fillna"),
        
        ("df.dropna() の役割は？",
         [{"id":"A","text":"欠損値を含む行削除"},{"id":"B","text":"欠損値補完"},{"id":"C","text":"重複削除"},{"id":"D","text":"ソート"}],
         [0], "試験対策_データサイエンス", "2", 8, "欠損値削除", "dropna"),
        
        ("df.groupby() の用途は？",
         [{"id":"A","text":"グループ別集計"},{"id":"B","text":"ソート"},{"id":"C","text":"フィルタ"},{"id":"D","text":"結合"}],
         [0], "試験対策_データサイエンス", "3", 10, "集約処理", "groupby"),
        
        ("df.merge() の用途は？",
         [{"id":"A","text":"DataFrame結合"},{"id":"B","text":"行追加"},{"id":"C","text":"列追加"},{"id":"D","text":"削除"}],
         [0], "試験対策_データサイエンス", "3", 10, "テーブル結合", "merge"),
        
        ("df.sort_values() の役割は？",
         [{"id":"A","text":"値でソート"},{"id":"B","text":"インデックスでソート"},{"id":"C","text":"グループ化"},{"id":"D","text":"フィルタ"}],
         [0], "試験対策_データサイエンス", "2", 8, "並び替え", "sort_values"),
        
        ("np.array() の役割は？",
         [{"id":"A","text":"NumPy配列作成"},{"id":"B","text":"リスト作成"},{"id":"C","text":"辞書作成"},{"id":"D","text":"タプル作成"}],
         [0], "試験対策_データサイエンス", "2", 8, "ndarray生成", "array"),
        
        ("np.mean() の役割は？",
         [{"id":"A","text":"平均値計算"},{"id":"B","text":"中央値"},{"id":"C","text":"最大値"},{"id":"D","text":"合計"}],
         [0], "試験対策_データサイエンス", "2", 8, "算術平均", "mean"),
        
        ("np.median() の役割は？",
         [{"id":"A","text":"中央値計算"},{"id":"B","text":"平均値"},{"id":"C","text":"最頻値"},{"id":"D","text":"分散"}],
         [0], "試験対策_データサイエンス", "2", 8, "メディアン", "median"),
        
        ("np.std() の役割は？",
         [{"id":"A","text":"標準偏差計算"},{"id":"B","text":"分散"},{"id":"C","text":"平均"},{"id":"D","text":"中央値"}],
         [0], "試験対策_データサイエンス", "3", 10, "ばらつき", "std"),
        
        ("sklearn の正式名称は？",
         [{"id":"A","text":"scikit-learn"},{"id":"B","text":"science kit"},{"id":"C","text":"sklearn library"},{"id":"D","text":"statistical kit"}],
         [0], "試験対策_データサイエンス", "3", 10, "機械学習ライブラリ", "scikit-learn"),
        
        ("train_test_split の役割は？",
         [{"id":"A","text":"訓練データとテストデータ分割"},{"id":"B","text":"クロスバリデーション"},{"id":"C","text":"特徴量抽出"},{"id":"D","text":"モデル評価"}],
         [0], "試験対策_データサイエンス", "3", 10, "データ分割", "split"),
        
        ("正規化の目的は？",
         [{"id":"A","text":"スケール統一"},{"id":"B","text":"欠損値処理"},{"id":"C","text":"外れ値除去"},{"id":"D","text":"次元削減"}],
         [0], "試験対策_データサイエンス", "3", 12, "前処理", "正規化"),
        
        ("過学習（overfitting）とは？",
         [{"id":"A","text":"訓練データに特化しすぎ"},{"id":"B","text":"学習不足"},{"id":"C","text":"データ不足"},{"id":"D","text":"正常"}],
         [0], "試験対策_データサイエンス", "4", 15, "汎化性能低下", "overfitting"),
        
        ("交差検証の目的は？",
         [{"id":"A","text":"モデル性能評価"},{"id":"B","text":"データ分割"},{"id":"C","text":"特徴量選択"},{"id":"D","text":"前処理"}],
         [0], "試験対策_データサイエンス", "4", 12, "クロスバリデーション", "CV"),
        
        ("混同行列の用途は？",
         [{"id":"A","text":"分類精度の評価"},{"id":"B","text":"回帰評価"},{"id":"C","text":"データ分割"},{"id":"D","text":"前処理"}],
         [0], "試験対策_データサイエンス", "4", 12, "TP/TN/FP/FN", "confusion matrix"),
    ]
    
    questions.extend(datascience_questions)
    print(f"  ✓ データサイエンス基礎: {len(datascience_questions)}問")
    
    # ==================== セキュリティとベストプラクティス（25問） ====================
    print("[2/2] セキュリティとベストプラクティス問題を生成中...")
    
    security_questions = [
        ("パスワードの保存方法は？",
         [{"id":"A","text":"ハッシュ化して保存"},{"id":"B","text":"平文で保存"},{"id":"C","text":"暗号化のみ"},{"id":"D","text":"Base64エンコード"}],
         [0], "試験対策_セキュリティ", "4", 15, "bcrypt等", "ハッシュ"),
        
        ("SQLインジェクション対策は？",
         [{"id":"A","text":"プリペアドステートメント"},{"id":"B","text":"文字列連結"},{"id":"C","text":"入力制限のみ"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 15, "パラメータバインド", "SQLi対策"),
        
        ("XSS（クロスサイトスクリプティング）対策は？",
         [{"id":"A","text":"出力時のエスケープ"},{"id":"B","text":"入力制限のみ"},{"id":"C","text":"JavaScript無効化"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 15, "HTMLエスケープ", "XSS対策"),
        
        ("CSRF対策は？",
         [{"id":"A","text":"CSRFトークン"},{"id":"B","text":"Cookie無効化"},{"id":"C","text":"セッションのみ"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 15, "トークン検証", "CSRF対策"),
        
        ("HTTPS の役割は？",
         [{"id":"A","text":"通信の暗号化"},{"id":"B","text":"高速化"},{"id":"C","text":"圧縮"},{"id":"D","text":"認証のみ"}],
         [0], "試験対策_セキュリティ", "3", 10, "SSL/TLS", "暗号化"),
        
        ("secrets モジュールの用途は？",
         [{"id":"A","text":"暗号学的に安全な乱数"},{"id":"B","text":"通常の乱数"},{"id":"C","text":"設定管理"},{"id":"D","text":"ログ"}],
         [0], "試験対策_セキュリティ", "4", 12, "トークン生成", "secrets"),
        
        ("環境変数の用途は？",
         [{"id":"A","text":"機密情報の管理"},{"id":"B","text":"高速化"},{"id":"C","text":"デバッグ"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "3", 10, "設定の外部化", "環境変数"),
        
        (".env ファイルの扱いは？",
         [{"id":"A","text":"gitignoreに追加"},{"id":"B","text":"コミットする"},{"id":"C","text":"公開する"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "3", 10, "機密情報保護", ".env"),
        
        ("eval() 関数の危険性は？",
         [{"id":"A","text":"任意コード実行のリスク"},{"id":"B","text":"遅い"},{"id":"C","text":"メモリ消費"},{"id":"D","text":"危険なし"}],
         [0], "試験対策_セキュリティ", "4", 15, "コードインジェクション", "eval"),
        
        ("pickle の危険性は？",
         [{"id":"A","text":"信頼できないデータで危険"},{"id":"B","text":"遅い"},{"id":"C","text":"大きい"},{"id":"D","text":"危険なし"}],
         [0], "試験対策_セキュリティ", "4", 15, "任意コード実行", "pickle"),
        
        ("入力検証の原則は？",
         [{"id":"A","text":"ホワイトリスト方式"},{"id":"B","text":"ブラックリスト方式"},{"id":"C","text":"検証不要"},{"id":"D","text":"出力のみ"}],
         [0], "試験対策_セキュリティ", "3", 12, "許可リスト", "validation"),
        
        ("最小権限の原則とは？",
         [{"id":"A","text":"必要最小限の権限のみ付与"},{"id":"B","text":"全権限付与"},{"id":"C","text":"権限なし"},{"id":"D","text":"管理者権限"}],
         [0], "試験対策_セキュリティ", "3", 10, "セキュリティ原則", "least privilege"),
        
        ("ログに記録すべきでないもの？",
         [{"id":"A","text":"パスワード"},{"id":"B","text":"エラー"},{"id":"C","text":"アクセス情報"},{"id":"D","text":"処理時間"}],
         [0], "試験対策_セキュリティ", "3", 10, "機密情報保護", "logging"),
        
        ("OWASP Top 10 とは？",
         [{"id":"A","text":"Webアプリの脆弱性トップ10"},{"id":"B","text":"人気言語トップ10"},{"id":"C","text":"フレームワークトップ10"},{"id":"D","text":"ツールトップ10"}],
         [0], "試験対策_セキュリティ", "4", 12, "セキュリティ指針", "OWASP"),
        
        ("Two-Factor Authentication の略は？",
         [{"id":"A","text":"2FA"},{"id":"B","text":"TFA"},{"id":"C","text":"2AUTH"},{"id":"D","text":"MFA"}],
         [0], "試験対策_セキュリティ", "3", 10, "二要素認証", "2FA"),
        
        ("JWT の署名目的は？",
         [{"id":"A","text":"改ざん検出"},{"id":"B","text":"暗号化"},{"id":"C","text":"圧縮"},{"id":"D","text":"高速化"}],
         [0], "試験対策_セキュリティ", "4", 12, "完全性保証", "JWT署名"),
        
        ("CORS エラーの解決方法は？",
         [{"id":"A","text":"サーバー側でヘッダー設定"},{"id":"B","text":"クライアント変更"},{"id":"C","text":"無視"},{"id":"D","text":"不可能"}],
         [0], "試験対策_セキュリティ", "3", 10, "Access-Control-Allow-Origin", "CORS設定"),
        
        ("Content Security Policy の目的は？",
         [{"id":"A","text":"XSS対策"},{"id":"B","text":"SQLi対策"},{"id":"C","text":"CSRF対策"},{"id":"D","text":"高速化"}],
         [0], "試験対策_セキュリティ", "4", 15, "コンテンツ制限", "CSP"),
        
        ("同一生成元ポリシーとは？",
         [{"id":"A","text":"同じオリジンのみアクセス可"},{"id":"B","text":"全てアクセス可"},{"id":"C","text":"認証必須"},{"id":"D","text":"非推奨"}],
         [0], "試験対策_セキュリティ", "4", 12, "Same-Origin Policy", "SOP"),
        
        ("Rate Limiting の目的は？",
         [{"id":"A","text":"過剰リクエスト防止"},{"id":"B","text":"高速化"},{"id":"C","text":"認証"},{"id":"D","text":"暗号化"}],
         [0], "試験対策_セキュリティ", "3", 10, "DoS対策", "レート制限"),
        
        ("API キーの管理方法は？",
         [{"id":"A","text":"環境変数やシークレット管理"},{"id":"B","text":"ソースコードに記述"},{"id":"C","text":"公開"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 12, "機密情報管理", "APIキー"),
        
        ("ソルト（Salt）の目的は？",
         [{"id":"A","text":"ハッシュの一意性向上"},{"id":"B","text":"暗号化"},{"id":"C","text":"圧縮"},{"id":"D","text":"高速化"}],
         [0], "試験対策_セキュリティ", "4", 15, "レインボーテーブル対策", "Salt"),
        
        ("セッションハイジャック対策は？",
         [{"id":"A","text":"HTTPSとセキュアCookie"},{"id":"B","text":"HTTP使用"},{"id":"C","text":"Cookie無効化"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 15, "セッション保護", "セキュリティ"),
        
        ("依存パッケージの脆弱性チェックツールは？",
         [{"id":"A","text":"pip-audit, safety"},{"id":"B","text":"pip"},{"id":"C","text":"pytest"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "4", 12, "脆弱性スキャン", "セキュリティツール"),
        
        ("Pythonバージョンのサポート期限を確認すべき理由は？",
         [{"id":"A","text":"セキュリティ更新が止まる"},{"id":"B","text":"動作しなくなる"},{"id":"C","text":"高速化"},{"id":"D","text":"不要"}],
         [0], "試験対策_セキュリティ", "3", 10, "EOL確認", "バージョン管理"),
    ]
    
    questions.extend(security_questions)
    print(f"  ✓ セキュリティとベストプラクティス: {len(security_questions)}問")
    
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
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'Python' AND category LIKE '試験対策%'
        GROUP BY category 
        ORDER BY count DESC
    """)
    exam_categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊🎊🎊 Python試験対策 200問達成！！！ 🎊🎊🎊")
    print("=" * 60)
    print(f"Python全問題数: {py_count}問")
    print(f"  基礎問題: {py_count - exam_count}問")
    print(f"  試験対策: {exam_count}問")
    print(f"全体問題数: {total_count}問")
    
    print("\n【試験対策カテゴリ別内訳】")
    for cat, count in exam_categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("✅ Python試験対策 200問達成！")
    print("✅ Python合計: 300問超え！")
    print("\n次の目標:")
    print("  🎯 PHP: 100問（現在13問 → +87問）")
    print("  🎯 Java: 100問（現在15問 → +85問）")
    print("  🎯 その他言語の拡充")
    print("=" * 60)

if __name__ == "__main__":
    add_python_exam_batch3b_final()