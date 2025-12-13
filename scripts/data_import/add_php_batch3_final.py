import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_php_batch3_final():
    """PHP問題追加（第3弾・最終30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("PHP問題追加スクリプト（第3弾・最終30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== クラスとOOP（10問） ====================
    print("[1/3] クラスとOOP問題を生成中...")
    
    oop_questions = [
        ("クラスの定義方法は？",
         [{"id":"A","text":"class MyClass { }"},{"id":"B","text":"Class MyClass { }"},{"id":"C","text":"def MyClass: {}"},{"id":"D","text":"struct MyClass {}"}],
         [0], "クラス", "1", 5, "クラス定義", "class"),
        
        ("インスタンス生成の方法は？",
         [{"id":"A","text":"$obj = new MyClass();"},{"id":"B","text":"$obj = MyClass();"},{"id":"C","text":"$obj = create MyClass();"},{"id":"D","text":"$obj = MyClass.new();"}],
         [0], "クラス", "1", 5, "new演算子", "インスタンス化"),
        
        ("__construct() の役割は？",
         [{"id":"A","text":"コンストラクタ"},{"id":"B","text":"デストラクタ"},{"id":"C","text":"ゲッター"},{"id":"D","text":"セッター"}],
         [0], "クラス", "2", 8, "初期化メソッド", "コンストラクタ"),
        
        ("$this の意味は？",
         [{"id":"A","text":"現在のオブジェクト"},{"id":"B","text":"親クラス"},{"id":"C","text":"静的参照"},{"id":"D","text":"グローバル変数"}],
         [0], "クラス", "2", 8, "自己参照", "$this"),
        
        ("public, private, protected の違いは？",
         [{"id":"A","text":"アクセス範囲が異なる"},{"id":"B","text":"同じ"},{"id":"C","text":"速度が違う"},{"id":"D","text":"型が違う"}],
         [0], "クラス", "3", 10, "アクセス修飾子", "可視性"),
        
        ("extends の役割は？",
         [{"id":"A","text":"クラスの継承"},{"id":"B","text":"インターフェース実装"},{"id":"C","text":"トレイト使用"},{"id":"D","text":"名前空間"}],
         [0], "クラス", "2", 8, "継承", "extends"),
        
        ("implements の役割は？",
         [{"id":"A","text":"インターフェースの実装"},{"id":"B","text":"継承"},{"id":"C","text":"トレイト使用"},{"id":"D","text":"名前空間"}],
         [0], "クラス", "3", 10, "インターフェース", "implements"),
        
        ("abstract class の特徴は？",
         [{"id":"A","text":"インスタンス化できない"},{"id":"B","text":"継承できない"},{"id":"C","text":"メソッドなし"},{"id":"D","text":"高速"}],
         [0], "クラス", "4", 12, "抽象クラス", "abstract"),
        
        ("static の役割は？",
         [{"id":"A","text":"クラスレベルのメンバー"},{"id":"B","text":"インスタンスメンバー"},{"id":"C","text":"定数"},{"id":"D","text":"変数"}],
         [0], "クラス", "3", 10, "静的メンバー", "static"),
        
        ("trait の用途は？",
         [{"id":"A","text":"コードの再利用"},{"id":"B","text":"継承"},{"id":"C","text":"インターフェース"},{"id":"D","text":"名前空間"}],
         [0], "クラス", "4", 12, "トレイト", "trait"),
    ]
    
    questions.extend(oop_questions)
    print(f"  ✓ クラスとOOP: {len(oop_questions)}問")
    
    # ==================== ファイル・DB・セッション（10問） ====================
    print("[2/3] ファイル・DB・セッション問題を生成中...")
    
    file_db_questions = [
        ("ファイルの読み込み方法は？",
         [{"id":"A","text":"file_get_contents() または fopen()"},{"id":"B","text":"read()"},{"id":"C","text":"open()"},{"id":"D","text":"load()"}],
         [0], "ファイル操作", "2", 8, "ファイル読み込み", "file操作"),
        
        ("file_put_contents() の役割は？",
         [{"id":"A","text":"ファイルへ書き込み"},{"id":"B","text":"ファイル読み込み"},{"id":"C","text":"ファイル削除"},{"id":"D","text":"ファイル移動"}],
         [0], "ファイル操作", "2", 8, "ファイル書き込み", "書き込み"),
        
        ("MySQLへの接続方法（推奨）は？",
         [{"id":"A","text":"PDO または mysqli"},{"id":"B","text":"mysql_connect()"},{"id":"C","text":"db_connect()"},{"id":"D","text":"connect()"}],
         [0], "データベース", "3", 10, "DB接続", "PDO/mysqli"),
        
        ("PDO のプリペアドステートメントの利点は？",
         [{"id":"A","text":"SQLインジェクション対策"},{"id":"B","text":"高速化のみ"},{"id":"C","text":"メモリ節約"},{"id":"D","text":"必須機能"}],
         [0], "データベース", "4", 15, "セキュリティ", "プリペアド"),
        
        ("session_start() の役割は？",
         [{"id":"A","text":"セッション開始"},{"id":"B","text":"セッション終了"},{"id":"C","text":"セッション削除"},{"id":"D","text":"セッション確認"}],
         [0], "セッション", "2", 8, "セッション初期化", "session"),
        
        ("$_SESSION の用途は？",
         [{"id":"A","text":"セッション変数の保存"},{"id":"B","text":"Cookie保存"},{"id":"C","text":"POST送信"},{"id":"D","text":"GET送信"}],
         [0], "セッション", "2", 8, "セッションデータ", "$_SESSION"),
        
        ("$_POST の用途は？",
         [{"id":"A","text":"POSTデータ取得"},{"id":"B","text":"GETデータ取得"},{"id":"C","text":"セッションデータ"},{"id":"D","text":"Cookie取得"}],
         [0], "スーパーグローバル", "1", 5, "POST変数", "$_POST"),
        
        ("$_GET の用途は？",
         [{"id":"A","text":"GETデータ取得"},{"id":"B","text":"POSTデータ取得"},{"id":"C","text":"セッションデータ"},{"id":"D","text":"Cookie取得"}],
         [0], "スーパーグローバル", "1", 5, "GET変数", "$_GET"),
        
        ("$_COOKIE の用途は？",
         [{"id":"A","text":"Cookie値の取得"},{"id":"B","text":"Cookie設定"},{"id":"C","text":"セッション取得"},{"id":"D","text":"POST取得"}],
         [0], "スーパーグローバル", "2", 8, "Cookie変数", "$_COOKIE"),
        
        ("$_SERVER['REQUEST_METHOD'] の値は？",
         [{"id":"A","text":"GET, POST等のHTTPメソッド"},{"id":"B","text":"サーバー名"},{"id":"C","text":"IPアドレス"},{"id":"D","text":"ポート番号"}],
         [0], "スーパーグローバル", "2", 8, "リクエストメソッド", "$_SERVER"),
    ]
    
    questions.extend(file_db_questions)
    print(f"  ✓ ファイル・DB・セッション: {len(file_db_questions)}問")
    
    # ==================== エラーハンドリングとセキュリティ（10問） ====================
    print("[3/3] エラーハンドリングとセキュリティ問題を生成中...")
    
    error_security_questions = [
        ("try-catch文の役割は？",
         [{"id":"A","text":"例外処理"},{"id":"B","text":"ループ"},{"id":"C","text":"条件分岐"},{"id":"D","text":"関数定義"}],
         [0], "エラー処理", "2", 8, "例外ハンドリング", "try-catch"),
        
        ("throw の役割は？",
         [{"id":"A","text":"例外を投げる"},{"id":"B","text":"例外を捕捉"},{"id":"C","text":"エラーログ"},{"id":"D","text":"デバッグ"}],
         [0], "エラー処理", "2", 8, "例外発生", "throw"),
        
        ("finally ブロックの実行タイミングは？",
         [{"id":"A","text":"必ず実行される"},{"id":"B","text":"成功時のみ"},{"id":"C","text":"失敗時のみ"},{"id":"D","text":"実行されない"}],
         [0], "エラー処理", "2", 8, "クリーンアップ", "finally"),
        
        ("htmlspecialchars() の目的は？",
         [{"id":"A","text":"XSS対策（エスケープ）"},{"id":"B","text":"SQLi対策"},{"id":"C","text":"暗号化"},{"id":"D","text":"圧縮"}],
         [0], "セキュリティ", "4", 15, "特殊文字変換", "XSS対策"),
        
        ("password_hash() の用途は？",
         [{"id":"A","text":"パスワードのハッシュ化"},{"id":"B","text":"パスワードの暗号化"},{"id":"C","text":"パスワードの検証"},{"id":"D","text":"パスワードの保存"}],
         [0], "セキュリティ", "4", 15, "安全なパスワード保存", "ハッシュ"),
        
        ("password_verify() の用途は？",
         [{"id":"A","text":"パスワードの検証"},{"id":"B","text":"パスワードのハッシュ化"},{"id":"C","text":"パスワードの暗号化"},{"id":"D","text":"パスワードの生成"}],
         [0], "セキュリティ", "4", 12, "ハッシュ照合", "検証"),
        
        ("filter_var() の用途は？",
         [{"id":"A","text":"入力値のフィルタリング"},{"id":"B","text":"出力"},{"id":"C","text":"暗号化"},{"id":"D","text":"圧縮"}],
         [0], "セキュリティ", "3", 10, "バリデーション", "filter"),
        
        ("CSRF対策の方法は？",
         [{"id":"A","text":"トークン検証"},{"id":"B","text":"Cookie無効化"},{"id":"C","text":"セッションのみ"},{"id":"D","text":"不要"}],
         [0], "セキュリティ", "4", 15, "トークンベース保護", "CSRF"),
        
        ("error_reporting() の役割は？",
         [{"id":"A","text":"エラー報告レベル設定"},{"id":"B","text":"エラー表示"},{"id":"C","text":"エラーログ"},{"id":"D","text":"例外処理"}],
         [0], "エラー処理", "2", 8, "エラー制御", "error_reporting"),
        
        ("ini_set('display_errors', '0') の効果は？",
         [{"id":"A","text":"エラー表示を無効化"},{"id":"B","text":"エラー表示を有効化"},{"id":"C","text":"エラーログ"},{"id":"D","text":"例外処理"}],
         [0], "エラー処理", "3", 10, "本番環境設定", "display_errors"),
    ]
    
    questions.extend(error_security_questions)
    print(f"  ✓ エラーハンドリングとセキュリティ: {len(error_security_questions)}問")
    
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
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'PHP' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊🎊🎊 PHP 100問達成！！！ 🎊🎊🎊")
    print("=" * 60)
    print(f"PHP問題数: {php_count}問")
    print(f"全体問題数: {total_count}問")
    
    print("\n【PHPカテゴリ別内訳】")
    for cat, count in categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("✅ PHP 100問達成！")
    print("\n【達成状況まとめ】")
    print("  ✅ IQ: 500問")
    print("  ✅ JavaScript: 104問")
    print("  ✅ Python: 314問（基礎114問 + 試験対策200問）")
    print("  ✅ PHP: 100問超え！")
    print("\n次の目標:")
    print("  🎯 Java: 100問（現在15問 → +85問）")
    print("  🎯 C#: 100問（現在12問 → +88問）")
    print("=" * 60)

if __name__ == "__main__":
    add_php_batch3_final()