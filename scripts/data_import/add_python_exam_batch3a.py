import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_python_exam_batch3a():
    """Python試験対策問題追加（第3弾-前半・50問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Python試験対策問題追加スクリプト（第3弾-前半・50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== データベース操作（25問） ====================
    print("[1/2] データベース操作問題を生成中...")
    
    database_questions = [
        ("sqlite3 モジュールの用途は？",
         [{"id":"A","text":"SQLiteデータベース操作"},{"id":"B","text":"MySQL接続"},{"id":"C","text":"NoSQL"},{"id":"D","text":"ファイル操作"}],
         [0], "試験対策_データベース", "3", 10, "組み込みDB", "sqlite3"),
        
        ("cursor.execute() の役割は？",
         [{"id":"A","text":"SQL実行"},{"id":"B","text":"接続開始"},{"id":"C","text":"トランザクション"},{"id":"D","text":"終了"}],
         [0], "試験対策_データベース", "2", 8, "クエリ実行", "execute"),
        
        ("cursor.fetchone() の返り値は？",
         [{"id":"A","text":"1行のタプル"},{"id":"B","text":"全行"},{"id":"C","text":"列名"},{"id":"D","text":"件数"}],
         [0], "試験対策_データベース", "2", 8, "1レコード取得", "fetchone"),
        
        ("cursor.fetchall() の返り値は？",
         [{"id":"A","text":"全行のリスト"},{"id":"B","text":"1行"},{"id":"C","text":"イテレータ"},{"id":"D","text":"件数"}],
         [0], "試験対策_データベース", "2", 8, "全レコード取得", "fetchall"),
        
        ("conn.commit() の役割は？",
         [{"id":"A","text":"変更を確定"},{"id":"B","text":"ロールバック"},{"id":"C","text":"接続"},{"id":"D","text":"終了"}],
         [0], "試験対策_データベース", "2", 8, "トランザクション確定", "commit"),
        
        ("conn.rollback() の役割は？",
         [{"id":"A","text":"変更を取り消し"},{"id":"B","text":"変更を確定"},{"id":"C","text":"接続"},{"id":"D","text":"削除"}],
         [0], "試験対策_データベース", "3", 10, "トランザクション取り消し", "rollback"),
        
        ("SQLインジェクション対策は？",
         [{"id":"A","text":"プレースホルダ使用"},{"id":"B","text":"文字列連結"},{"id":"C","text":"エスケープのみ"},{"id":"D","text":"対策不要"}],
         [0], "試験対策_データベース", "4", 15, "パラメータ化クエリ", "セキュリティ"),
        
        ("executemany() の用途は？",
         [{"id":"A","text":"複数行一括挿入"},{"id":"B","text":"複数クエリ"},{"id":"C","text":"JOIN"},{"id":"D","text":"集計"}],
         [0], "試験対策_データベース", "3", 10, "バッチ処理", "executemany"),
        
        ("with conn: の効果は？",
         [{"id":"A","text":"自動commit/rollback"},{"id":"B","text":"高速化"},{"id":"C","text":"必須構文"},{"id":"D","text":"ログ"}],
         [0], "試験対策_データベース", "3", 12, "コンテキストマネージャ", "with"),
        
        ("PRIMARY KEY の役割は？",
         [{"id":"A","text":"一意な識別子"},{"id":"B","text":"インデックス"},{"id":"C","text":"外部キー"},{"id":"D","text":"ソート"}],
         [0], "試験対策_データベース", "2", 8, "主キー", "PRIMARY KEY"),
        
        ("FOREIGN KEY の役割は？",
         [{"id":"A","text":"他テーブル参照"},{"id":"B","text":"主キー"},{"id":"C","text":"インデックス"},{"id":"D","text":"ユニーク"}],
         [0], "試験対策_データベース", "3", 10, "外部キー制約", "FOREIGN KEY"),
        
        ("INDEX の効果は？",
         [{"id":"A","text":"検索高速化"},{"id":"B","text":"データ圧縮"},{"id":"C","text":"暗号化"},{"id":"D","text":"バックアップ"}],
         [0], "試験対策_データベース", "3", 10, "検索最適化", "INDEX"),
        
        ("INNER JOIN の動作は？",
         [{"id":"A","text":"両方に存在するレコード"},{"id":"B","text":"全レコード"},{"id":"C","text":"左側全て"},{"id":"D","text":"右側全て"}],
         [0], "試験対策_データベース", "3", 10, "内部結合", "INNER JOIN"),
        
        ("LEFT JOIN の動作は？",
         [{"id":"A","text":"左テーブル全て+マッチする右"},{"id":"B","text":"右テーブル全て"},{"id":"C","text":"両方に存在のみ"},{"id":"D","text":"全レコード"}],
         [0], "試験対策_データベース", "3", 10, "左外部結合", "LEFT JOIN"),
        
        ("GROUP BY の用途は？",
         [{"id":"A","text":"集計処理"},{"id":"B","text":"ソート"},{"id":"C","text":"フィルタ"},{"id":"D","text":"結合"}],
         [0], "試験対策_データベース", "3", 10, "グループ化", "GROUP BY"),
        
        ("HAVING 句の用途は？",
         [{"id":"A","text":"集計結果のフィルタ"},{"id":"B","text":"WHERE句と同じ"},{"id":"C","text":"ソート"},{"id":"D","text":"結合"}],
         [0], "試験対策_データベース", "4", 12, "集計後の条件", "HAVING"),
        
        ("DISTINCT の役割は？",
         [{"id":"A","text":"重複削除"},{"id":"B","text":"ソート"},{"id":"C","text":"集計"},{"id":"D","text":"結合"}],
         [0], "試験対策_データベース", "2", 8, "一意な値のみ", "DISTINCT"),
        
        ("LIMIT の役割は？",
         [{"id":"A","text":"取得件数制限"},{"id":"B","text":"削除件数制限"},{"id":"C","text":"更新件数制限"},{"id":"D","text":"タイムアウト"}],
         [0], "試験対策_データベース", "2", 8, "結果件数制限", "LIMIT"),
        
        ("ORDER BY DESC は？",
         [{"id":"A","text":"降順ソート"},{"id":"B","text":"昇順ソート"},{"id":"C","text":"ランダム"},{"id":"D","text":"グループ化"}],
         [0], "試験対策_データベース", "2", 8, "降順", "ORDER BY"),
        
        ("LIKE 演算子の用途は？",
         [{"id":"A","text":"パターンマッチング"},{"id":"B","text":"完全一致"},{"id":"C","text":"数値比較"},{"id":"D","text":"NULL判定"}],
         [0], "試験対策_データベース", "2", 8, "曖昧検索", "LIKE"),
        
        ("NULL の扱い方は？",
         [{"id":"A","text":"IS NULL / IS NOT NULL"},{"id":"B","text":"= NULL"},{"id":"C","text":"== NULL"},{"id":"D","text":"!= NULL"}],
         [0], "試験対策_データベース", "3", 10, "NULL判定", "NULL"),
        
        ("COUNT(*) の役割は？",
         [{"id":"A","text":"レコード数集計"},{"id":"B","text":"合計値"},{"id":"C","text":"平均値"},{"id":"D","text":"最大値"}],
         [0], "試験対策_データベース", "2", 8, "件数カウント", "COUNT"),
        
        ("SUM() の役割は？",
         [{"id":"A","text":"合計値計算"},{"id":"B","text":"平均値"},{"id":"C","text":"件数"},{"id":"D","text":"最大値"}],
         [0], "試験対策_データベース", "2", 8, "合計", "SUM"),
        
        ("AVG() の役割は？",
         [{"id":"A","text":"平均値計算"},{"id":"B","text":"合計値"},{"id":"C","text":"件数"},{"id":"D","text":"中央値"}],
         [0], "試験対策_データベース", "2", 8, "平均", "AVG"),
        
        ("MAX() / MIN() の役割は？",
         [{"id":"A","text":"最大値/最小値"},{"id":"B","text":"合計値"},{"id":"C","text":"平均値"},{"id":"D","text":"件数"}],
         [0], "試験対策_データベース", "2", 8, "極値取得", "MAX/MIN"),
    ]
    
    questions.extend(database_questions)
    print(f"  ✓ データベース操作: {len(database_questions)}問")
    
    # ==================== Web開発基礎（25問） ====================
    print("[2/2] Web開発基礎問題を生成中...")
    
    web_questions = [
        ("HTTP メソッドで取得は？",
         [{"id":"A","text":"GET"},{"id":"B","text":"POST"},{"id":"C","text":"PUT"},{"id":"D","text":"DELETE"}],
         [0], "試験対策_Web", "2", 8, "リソース取得", "HTTP"),
        
        ("HTTP メソッドで作成は？",
         [{"id":"A","text":"POST"},{"id":"B","text":"GET"},{"id":"C","text":"PUT"},{"id":"D","text":"DELETE"}],
         [0], "試験対策_Web", "2", 8, "リソース作成", "POST"),
        
        ("HTTP メソッドで更新は？",
         [{"id":"A","text":"PUT/PATCH"},{"id":"B","text":"GET"},{"id":"C","text":"POST"},{"id":"D","text":"DELETE"}],
         [0], "試験対策_Web", "2", 8, "リソース更新", "PUT"),
        
        ("HTTP メソッドで削除は？",
         [{"id":"A","text":"DELETE"},{"id":"B","text":"GET"},{"id":"C","text":"POST"},{"id":"D","text":"PUT"}],
         [0], "試験対策_Web", "2", 8, "リソース削除", "DELETE"),
        
        ("HTTP ステータス 200 の意味は？",
         [{"id":"A","text":"成功"},{"id":"B","text":"リダイレクト"},{"id":"C","text":"エラー"},{"id":"D","text":"認証必要"}],
         [0], "試験対策_Web", "2", 8, "OK", "HTTPステータス"),
        
        ("HTTP ステータス 201 の意味は？",
         [{"id":"A","text":"作成成功"},{"id":"B","text":"OK"},{"id":"C","text":"エラー"},{"id":"D","text":"リダイレクト"}],
         [0], "試験対策_Web", "2", 8, "Created", "201"),
        
        ("HTTP ステータス 400 の意味は？",
         [{"id":"A","text":"クライアントエラー"},{"id":"B","text":"サーバーエラー"},{"id":"C","text":"成功"},{"id":"D","text":"リダイレクト"}],
         [0], "試験対策_Web", "2", 8, "Bad Request", "400"),
        
        ("HTTP ステータス 401 の意味は？",
         [{"id":"A","text":"認証が必要"},{"id":"B","text":"権限なし"},{"id":"C","text":"Not Found"},{"id":"D","text":"サーバーエラー"}],
         [0], "試験対策_Web", "2", 8, "Unauthorized", "401"),
        
        ("HTTP ステータス 403 の意味は？",
         [{"id":"A","text":"権限なし（禁止）"},{"id":"B","text":"認証必要"},{"id":"C","text":"Not Found"},{"id":"D","text":"成功"}],
         [0], "試験対策_Web", "2", 8, "Forbidden", "403"),
        
        ("HTTP ステータス 404 の意味は？",
         [{"id":"A","text":"Not Found"},{"id":"B","text":"成功"},{"id":"C","text":"サーバーエラー"},{"id":"D","text":"認証必要"}],
         [0], "試験対策_Web", "1", 5, "ページが見つからない", "404"),
        
        ("HTTP ステータス 500 の意味は？",
         [{"id":"A","text":"サーバーエラー"},{"id":"B","text":"クライアントエラー"},{"id":"C","text":"成功"},{"id":"D","text":"リダイレクト"}],
         [0], "試験対策_Web", "2", 8, "Internal Server Error", "500"),
        
        ("REST API の特徴は？",
         [{"id":"A","text":"ステートレス"},{"id":"B","text":"セッション必須"},{"id":"C","text":"Cookie必須"},{"id":"D","text":"SOAP"}],
         [0], "試験対策_Web", "3", 10, "状態を持たない", "REST"),
        
        ("JSON の正式名称は？",
         [{"id":"A","text":"JavaScript Object Notation"},{"id":"B","text":"Java Standard Object Notation"},{"id":"C","text":"JSON Serialization"},{"id":"D","text":"Java Object Network"}],
         [0], "試験対策_Web", "2", 8, "データ交換フォーマット", "JSON"),
        
        ("Cookie の特徴は？",
         [{"id":"A","text":"クライアント側に保存"},{"id":"B","text":"サーバー側のみ"},{"id":"C","text":"暗号化必須"},{"id":"D","text":"容量無制限"}],
         [0], "試験対策_Web", "2", 8, "ブラウザに保存", "Cookie"),
        
        ("Session の特徴は？",
         [{"id":"A","text":"サーバー側に保存"},{"id":"B","text":"クライアント側のみ"},{"id":"C","text":"永続的"},{"id":"D","text":"暗号化不要"}],
         [0], "試験対策_Web", "3", 10, "サーバー状態管理", "Session"),
        
        ("Flask の特徴は？",
         [{"id":"A","text":"軽量Webフレームワーク"},{"id":"B","text":"重量級"},{"id":"C","text":"非同期専用"},{"id":"D","text":"Django"}],
         [0], "試験対策_Web", "2", 8, "マイクロフレームワーク", "Flask"),
        
        ("Django の特徴は？",
         [{"id":"A","text":"フルスタックフレームワーク"},{"id":"B","text":"軽量"},{"id":"C","text":"マイクロ"},{"id":"D","text":"非同期専用"}],
         [0], "試験対策_Web", "3", 10, "バッテリー内蔵", "Django"),
        
        ("FastAPI の特徴は？",
         [{"id":"A","text":"高速・型ヒント・自動ドキュメント"},{"id":"B","text":"軽量のみ"},{"id":"C","text":"同期処理"},{"id":"D","text":"レガシー"}],
         [0], "試験対策_Web", "3", 12, "モダンAPI", "FastAPI"),
        
        ("WSGI とは？",
         [{"id":"A","text":"Web Server Gateway Interface"},{"id":"B","text":"Web Socket Gateway Interface"},{"id":"C","text":"Web Service Gateway Interface"},{"id":"D","text":"Windows Server Gateway"}],
         [0], "試験対策_Web", "4", 12, "PythonとWebサーバーの仕様", "WSGI"),
        
        ("requests.get() の役割は？",
         [{"id":"A","text":"HTTP GETリクエスト"},{"id":"B","text":"POST"},{"id":"C","text":"ファイル取得"},{"id":"D","text":"データ送信"}],
         [0], "試験対策_Web", "2", 8, "HTTPクライアント", "requests"),
        
        ("requests.post() の役割は？",
         [{"id":"A","text":"HTTP POSTリクエスト"},{"id":"B","text":"GET"},{"id":"C","text":"ファイル取得"},{"id":"D","text":"削除"}],
         [0], "試験対策_Web", "2", 8, "データ送信", "POST"),
        
        ("Beautiful Soup の用途は？",
         [{"id":"A","text":"HTMLパース（スクレイピング）"},{"id":"B","text":"HTTP通信"},{"id":"C","text":"JSON解析"},{"id":"D","text":"データベース"}],
         [0], "試験対策_Web", "3", 10, "Webスクレイピング", "BeautifulSoup"),
        
        ("URL エンコードの目的は？",
         [{"id":"A","text":"特殊文字の安全な送信"},{"id":"B","text":"暗号化"},{"id":"C","text":"圧縮"},{"id":"D","text":"高速化"}],
         [0], "試験対策_Web", "3", 10, "パーセントエンコーディング", "URLエンコード"),
        
        ("Content-Type: application/json の意味は？",
         [{"id":"A","text":"JSON形式のデータ"},{"id":"B","text":"HTML"},{"id":"C","text":"テキスト"},{"id":"D","text":"バイナリ"}],
         [0], "試験対策_Web", "2", 8, "MIMEタイプ", "Content-Type"),
        
        ("CORS の目的は？",
         [{"id":"A","text":"クロスオリジンリソース共有"},{"id":"B","text":"認証"},{"id":"C","text":"暗号化"},{"id":"D","text":"圧縮"}],
         [0], "試験対策_Web", "4", 12, "異なるオリジン間の通信", "CORS"),
    ]
    
    questions.extend(web_questions)
    print(f"  ✓ Web開発基礎: {len(web_questions)}問")
    
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
    print("✓ Python試験対策問題追加完了（第3弾-前半）！")
    print("=" * 60)
    print(f"Python全問題数: {py_count}問")
    print(f"  うち試験対策: {exam_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"試験対策目標200問まで残り: {max(0, 200 - exam_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_python_exam_batch3a()