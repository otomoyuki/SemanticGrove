import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_php_batch1():
    """PHP問題追加（第1弾・30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("PHP問題追加スクリプト（第1弾・30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== 基本文法（10問） ====================
    print("[1/3] 基本文法問題を生成中...")
    
    basic_questions = [
        ("PHPスクリプトの開始タグは？",
         [{"id":"A","text":"<?php"},{"id":"B","text":"<php>"},{"id":"C","text":"<%php%>"},{"id":"D","text":"<script php>"}],
         [0], "基本文法", "1", 5, "PHPコード開始", "開始タグ"),
        
        ("PHPの変数は何で始まる？",
         [{"id":"A","text":"$記号"},{"id":"B","text":"@記号"},{"id":"C","text":"#記号"},{"id":"D","text":"&記号"}],
         [0], "基本文法", "1", 5, "ドル記号", "変数"),
        
        ("文の終わりに必要なのは？",
         [{"id":"A","text":"セミコロン;"},{"id":"B","text":"コロン:"},{"id":"C","text":"カンマ,"},{"id":"D","text":"ピリオド."}],
         [0], "基本文法", "1", 5, "文末記号", "セミコロン"),
        
        ("コメントの書き方（1行）は？",
         [{"id":"A","text":"// または #"},{"id":"B","text":"<!-- -->"},{"id":"C","text":"/* */"},{"id":"D","text":"-- --"}],
         [0], "基本文法", "1", 5, "単一行コメント", "コメント"),
        
        ("複数行コメントの書き方は？",
         [{"id":"A","text":"/* */"},{"id":"B","text":"// //"},{"id":"C","text":"# #"},{"id":"D","text":"<!-- -->"}],
         [0], "基本文法", "2", 8, "複数行コメント", "コメント"),
        
        ("echo と print の違いは？",
         [{"id":"A","text":"echoは複数引数可、高速"},{"id":"B","text":"同じ"},{"id":"C","text":"printが高速"},{"id":"D","text":"echoは非推奨"}],
         [0], "基本文法", "2", 8, "出力命令", "echo/print"),
        
        ("文字列連結演算子は？",
         [{"id":"A","text":".（ドット）"},{"id":"B","text":"+"},{"id":"C","text":"&"},{"id":"D","text":"||"}],
         [0], "基本文法", "1", 5, "文字列結合", "連結演算子"),
        
        ("変数の型を調べる関数は？",
         [{"id":"A","text":"gettype() または var_dump()"},{"id":"B","text":"typeof()"},{"id":"C","text":"type()"},{"id":"D","text":"checktype()"}],
         [0], "基本文法", "2", 8, "型確認", "gettype"),
        
        ("定数の定義方法は？",
         [{"id":"A","text":"define() または const"},{"id":"B","text":"const のみ"},{"id":"C","text":"var"},{"id":"D","text":"let"}],
         [0], "基本文法", "2", 8, "定数定義", "define"),
        
        ("変数のスコープで関数内でグローバル変数を使うには？",
         [{"id":"A","text":"global キーワード"},{"id":"B","text":"public"},{"id":"C","text":"static"},{"id":"D","text":"extern"}],
         [0], "基本文法", "3", 10, "グローバルスコープ", "global"),
    ]
    
    questions.extend(basic_questions)
    print(f"  ✓ 基本文法: {len(basic_questions)}問")
    
    # ==================== データ型と演算子（10問） ====================
    print("[2/3] データ型と演算子問題を生成中...")
    
    datatype_questions = [
        ("PHPの主なデータ型は？",
         [{"id":"A","text":"string, int, float, bool, array, object, NULL"},{"id":"B","text":"int, float のみ"},{"id":"C","text":"string のみ"},{"id":"D","text":"型なし"}],
         [0], "データ型", "2", 8, "8つの基本型", "データ型"),
        
        ("'5' == 5 の結果は？",
         [{"id":"A","text":"true"},{"id":"B","text":"false"},{"id":"C","text":"エラー"},{"id":"D","text":"NULL"}],
         [0], "データ型", "3", 10, "緩い比較（型変換あり）", "==演算子"),
        
        ("'5' === 5 の結果は？",
         [{"id":"A","text":"false"},{"id":"B","text":"true"},{"id":"C","text":"エラー"},{"id":"D","text":"NULL"}],
         [0], "データ型", "3", 10, "厳密な比較（型も含む）", "===演算子"),
        
        ("10 / 3 の結果の型は？",
         [{"id":"A","text":"float"},{"id":"B","text":"int"},{"id":"C","text":"string"},{"id":"D","text":"double"}],
         [0], "データ型", "2", 8, "浮動小数点数", "除算"),
        
        ("10 % 3 の結果は？",
         [{"id":"A","text":"1"},{"id":"B","text":"3"},{"id":"C","text":"3.333..."},{"id":"D","text":"0"}],
         [0], "データ型", "2", 8, "剰余演算", "余り"),
        
        ("2 ** 3 の結果は？（PHP 5.6+）",
         [{"id":"A","text":"8"},{"id":"B","text":"6"},{"id":"C","text":"9"},{"id":"D","text":"エラー"}],
         [0], "データ型", "2", 8, "べき乗演算子", "**"),
        
        ("NULL合体演算子 ?? の役割は？（PHP 7+）",
         [{"id":"A","text":"NULLなら右側の値"},{"id":"B","text":"比較"},{"id":"C","text":"代入"},{"id":"D","text":"連結"}],
         [0], "データ型", "3", 10, "NULL判定と代替値", "??演算子"),
        
        ("Spaceship演算子 <=> の役割は？（PHP 7+）",
         [{"id":"A","text":"3方向比較（-1, 0, 1）"},{"id":"B","text":"代入"},{"id":"C","text":"等価比較"},{"id":"D","text":"連結"}],
         [0], "データ型", "4", 12, "比較演算", "<=>"),
        
        ("(int)$var の役割は？",
         [{"id":"A","text":"整数型へのキャスト"},{"id":"B","text":"型チェック"},{"id":"C","text":"比較"},{"id":"D","text":"エラー"}],
         [0], "データ型", "2", 8, "型変換", "キャスト"),
        
        ("empty() と isset() の違いは？",
         [{"id":"A","text":"empty()は空判定、isset()は存在判定"},{"id":"B","text":"同じ"},{"id":"C","text":"empty()が厳密"},{"id":"D","text":"isset()は非推奨"}],
         [0], "データ型", "3", 10, "変数チェック", "empty/isset"),
    ]
    
    questions.extend(datatype_questions)
    print(f"  ✓ データ型と演算子: {len(datatype_questions)}問")
    
    # ==================== 制御構文（10問） ====================
    print("[3/3] 制御構文問題を生成中...")
    
    control_questions = [
        ("if文の書き方は？",
         [{"id":"A","text":"if ($x > 0) { }"},{"id":"B","text":"if $x > 0 { }"},{"id":"C","text":"if x > 0: {}"},{"id":"D","text":"if (x > 0)"}],
         [0], "制御構文", "1", 5, "条件分岐", "if文"),
        
        ("elseif と else if の違いは？",
         [{"id":"A","text":"elseifが推奨"},{"id":"B","text":"else ifが推奨"},{"id":"C","text":"エラー"},{"id":"D","text":"同じ"}],
         [0], "制御構文", "2", 8, "条件分岐", "elseif"),
        
        ("switch文のdefaultの役割は？",
         [{"id":"A","text":"どのcaseにも一致しない時"},{"id":"B","text":"最初に実行"},{"id":"C","text":"必須"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "2", 8, "デフォルト処理", "switch"),
        
        ("for文の書き方は？",
         [{"id":"A","text":"for ($i=0; $i<10; $i++) { }"},{"id":"B","text":"for i in range(10): {}"},{"id":"C","text":"for ($i=0; $i<10) {}"},{"id":"D","text":"for i=0 to 10 {}"}],
         [0], "制御構文", "1", 5, "繰り返し", "for"),
        
        ("foreach文の書き方は？",
         [{"id":"A","text":"foreach ($arr as $val) { }"},{"id":"B","text":"for $val in $arr { }"},{"id":"C","text":"foreach $arr { }"},{"id":"D","text":"for each $arr {}"}],
         [0], "制御構文", "2", 8, "配列ループ", "foreach"),
        
        ("break文の役割は？",
         [{"id":"A","text":"ループを抜ける"},{"id":"B","text":"次の反復へ"},{"id":"C","text":"関数終了"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "1", 5, "ループ中断", "break"),
        
        ("continue文の役割は？",
         [{"id":"A","text":"次の反復へ進む"},{"id":"B","text":"ループを抜ける"},{"id":"C","text":"関数終了"},{"id":"D","text":"待機"}],
         [0], "制御構文", "2", 8, "反復スキップ", "continue"),
        
        ("while文の書き方は？",
         [{"id":"A","text":"while ($x < 10) { }"},{"id":"B","text":"while $x < 10: {}"},{"id":"C","text":"while ($x < 10)"},{"id":"D","text":"loop while $x < 10"}],
         [0], "制御構文", "1", 5, "条件ループ", "while"),
        
        ("do-while文の特徴は？",
         [{"id":"A","text":"最低1回は実行される"},{"id":"B","text":"whileと同じ"},{"id":"C","text":"実行されない場合あり"},{"id":"D","text":"非推奨"}],
         [0], "制御構文", "2", 8, "後判定ループ", "do-while"),
        
        ("三項演算子の書き方は？",
         [{"id":"A","text":"$x > 0 ? 'pos' : 'neg'"},{"id":"B","text":"if $x > 0 then 'pos' else 'neg'"},{"id":"C","text":"$x > 0 : 'pos' ? 'neg'"},{"id":"D","text":"エラー"}],
         [0], "制御構文", "2", 8, "条件式", "三項演算子"),
    ]
    
    questions.extend(control_questions)
    print(f"  ✓ 制御構文: {len(control_questions)}問")
    
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
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ PHP問題追加完了（第1弾）！")
    print("=" * 60)
    print(f"PHP問題数: {php_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標100問まで残り: {max(0, 100 - php_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_php_batch1()