import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_javascript_batch2():
    """JavaScript問題追加（第2弾・30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("JavaScript問題追加スクリプト（第2弾・30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== クロージャとスコープ（10問） ====================
    print("[1/3] クロージャとスコープ問題を生成中...")
    
    closure_questions = [
        ("let x = 1; function f() { return x; } f()の結果は？",
         [{"id":"A","text":"1"},{"id":"B","text":"undefined"},{"id":"C","text":"エラー"},{"id":"D","text":"null"}],
         [0], "スコープ", "2", 8, "外側の変数を参照可能", "レキシカルスコープ"),
        
        ("function outer() { let x = 1; return function() { return x; }; } のパターンは？",
         [{"id":"A","text":"クロージャ"},{"id":"B","text":"カリー化"},{"id":"C","text":"再帰"},{"id":"D","text":"高階関数"}],
         [0], "クロージャ", "3", 10, "内部関数が外部変数を保持", "クロージャパターン"),
        
        ("var と let の主な違いは？",
         [{"id":"A","text":"スコープの範囲"},{"id":"B","text":"型"},{"id":"C","text":"速度"},{"id":"D","text":"メモリ使用量"}],
         [0], "スコープ", "2", 8, "varは関数スコープ、letはブロックスコープ", "var vs let"),
        
        ("const で宣言した配列に push() できる？",
         [{"id":"A","text":"できる"},{"id":"B","text":"できない"},{"id":"C","text":"条件次第"},{"id":"D","text":"エラー"}],
         [0], "スコープ", "2", 8, "参照は変更不可だが中身は変更可", "const特性"),
        
        ("for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); } の出力は？",
         [{"id":"A","text":"3,3,3"},{"id":"B","text":"0,1,2"},{"id":"C","text":"エラー"},{"id":"D","text":"undefined"}],
         [0], "スコープ", "4", 15, "varはループ外のスコープを共有", "クロージャの罠"),
        
        ("即時実行関数式(IIFE)の書き方は？",
         [{"id":"A","text":"(function(){})()"},{"id":"B","text":"function(){}()"},{"id":"C","text":"=>(){}"},{"id":"D","text":"async(){}"}],
         [0], "関数", "3", 10, "関数を定義と同時に実行", "IIFE"),
        
        ("アロー関数のthisは何を指す？",
         [{"id":"A","text":"定義時の外側のthis"},{"id":"B","text":"呼び出し元のthis"},{"id":"C","text":"グローバルオブジェクト"},{"id":"D","text":"undefined"}],
         [0], "関数", "3", 12, "レキシカルなthis", "アロー関数のthis"),
        
        ("'use strict' の効果は？",
         [{"id":"A","text":"厳格モード有効化"},{"id":"B","text":"高速化"},{"id":"C","text":"デバッグモード"},{"id":"D","text":"型チェック"}],
         [0], "スコープ", "2", 8, "エラーを厳格にチェック", "strictモード"),
        
        ("let x; console.log(x); の出力は？",
         [{"id":"A","text":"undefined"},{"id":"B","text":"null"},{"id":"C","text":"0"},{"id":"D","text":"エラー"}],
         [0], "スコープ", "1", 5, "宣言されたが初期化されていない", "undefined"),
        
        ("ホイスティングが起こるのは？",
         [{"id":"A","text":"var と function"},{"id":"B","text":"let と const"},{"id":"C","text":"全ての変数"},{"id":"D","text":"起こらない"}],
         [0], "スコープ", "3", 10, "varと関数宣言は巻き上げられる", "ホイスティング"),
    ]
    
    questions.extend(closure_questions)
    print(f"  ✓ クロージャとスコープ: {len(closure_questions)}問")
    
    # ==================== プロトタイプとクラス（10問） ====================
    print("[2/3] プロトタイプとクラス問題を生成中...")
    
    prototype_questions = [
        ("JavaScriptの継承の仕組みは？",
         [{"id":"A","text":"プロトタイプチェーン"},{"id":"B","text":"クラスベース"},{"id":"C","text":"多重継承"},{"id":"D","text":"ミックスイン"}],
         [0], "プロトタイプ", "3", 10, "プロトタイプによる継承", "プロトタイプチェーン"),
        
        ("class は何のシンタックスシュガー？",
         [{"id":"A","text":"プロトタイプ"},{"id":"B","text":"関数"},{"id":"C","text":"オブジェクト"},{"id":"D","text":"新機能"}],
         [0], "クラス", "3", 10, "内部的にはプロトタイプを使用", "classの実態"),
        
        ("new演算子の役割は？",
         [{"id":"A","text":"インスタンス生成"},{"id":"B","text":"コピー"},{"id":"C","text":"型変換"},{"id":"D","text":"メモリ確保のみ"}],
         [0], "クラス", "2", 8, "コンストラクタを呼び出してインスタンス作成", "new演算子"),
        
        ("class内のstaticメソッドの特徴は？",
         [{"id":"A","text":"インスタンス不要で呼べる"},{"id":"B","text":"継承されない"},{"id":"C","text":"private"},{"id":"D","text":"非同期のみ"}],
         [0], "クラス", "2", 8, "クラス自体のメソッド", "staticメソッド"),
        
        ("extends キーワードの役割は？",
         [{"id":"A","text":"継承"},{"id":"B","text":"拡張"},{"id":"C","text":"実装"},{"id":"D","text":"型定義"}],
         [0], "クラス", "2", 8, "クラスを継承", "継承"),
        
        ("super() の役割は？",
         [{"id":"A","text":"親クラスのコンストラクタ呼び出し"},{"id":"B","text":"親クラス削除"},{"id":"C","text":"多重継承"},{"id":"D","text":"静的メソッド"}],
         [0], "クラス", "2", 8, "親のコンストラクタを実行", "super"),
        
        ("Object.create(proto)の役割は？",
         [{"id":"A","text":"protoを持つ新オブジェクト生成"},{"id":"B","text":"protoをコピー"},{"id":"C","text":"protoを削除"},{"id":"D","text":"エラー"}],
         [0], "プロトタイプ", "3", 10, "指定プロトタイプで新オブジェクト", "Object.create"),
        
        ("instanceof 演算子の役割は？",
         [{"id":"A","text":"インスタンス判定"},{"id":"B","text":"型変換"},{"id":"C","text":"比較"},{"id":"D","text":"コピー"}],
         [0], "クラス", "2", 8, "オブジェクトがクラスのインスタンスか判定", "instanceof"),
        
        ("__proto__ と prototype の違いは？",
         [{"id":"A","text":"__proto__はインスタンスのプロパティ"},{"id":"B","text":"同じもの"},{"id":"C","text":"prototypeは非推奨"},{"id":"D","text":"違いはない"}],
         [0], "プロトタイプ", "4", 15, "__proto__は実インスタンス、prototypeは関数のプロパティ", "プロトタイプの仕組み"),
        
        ("constructor プロパティは何を指す？",
         [{"id":"A","text":"生成元の関数"},{"id":"B","text":"親クラス"},{"id":"C","text":"プロトタイプ"},{"id":"D","text":"undefined"}],
         [0], "プロトタイプ", "3", 10, "オブジェクトを生成した関数", "constructor"),
    ]
    
    questions.extend(prototype_questions)
    print(f"  ✓ プロトタイプとクラス: {len(prototype_questions)}問")
    
    # ==================== モジュールと実践パターン（10問） ====================
    print("[3/3] モジュールと実践パターン問題を生成中...")
    
    module_questions = [
        ("ES6モジュールでエクスポートする方法は？",
         [{"id":"A","text":"export または export default"},{"id":"B","text":"module.exports"},{"id":"C","text":"return"},{"id":"D","text":"public"}],
         [0], "モジュール", "2", 8, "ES6モジュール構文", "export"),
        
        ("import文の正しい書き方は？",
         [{"id":"A","text":"import { func } from './file'"},{"id":"B","text":"require('./file')"},{"id":"C","text":"include './file'"},{"id":"D","text":"load('./file')"}],
         [0], "モジュール", "2", 8, "ES6モジュールのimport", "import"),
        
        ("export default の特徴は？",
         [{"id":"A","text":"1ファイル1つのみ"},{"id":"B","text":"複数可能"},{"id":"C","text":"名前必須"},{"id":"D","text":"非推奨"}],
         [0], "モジュール", "2", 8, "デフォルトエクスポート", "default export"),
        
        ("import * as obj from './file' の意味は？",
         [{"id":"A","text":"全てをobjにまとめる"},{"id":"B","text":"objのみインポート"},{"id":"C","text":"エラー"},{"id":"D","text":"非同期読み込み"}],
         [0], "モジュール", "3", 10, "名前空間インポート", "名前空間"),
        
        ("テンプレートリテラルの記号は？",
         [{"id":"A","text":"バッククォート `"},{"id":"B","text":"シングルクォート '"},{"id":"C","text":"ダブルクォート \""},{"id":"D","text":"スラッシュ /"}],
         [0], "ES6", "1", 5, "テンプレート文字列", "テンプレートリテラル"),
        
        ("`Hello ${name}` の ${} の役割は？",
         [{"id":"A","text":"変数埋め込み"},{"id":"B","text":"コメント"},{"id":"C","text":"エスケープ"},{"id":"D","text":"計算"}],
         [0], "ES6", "1", 5, "式の埋め込み", "補間"),
        
        ("スプレッド演算子 ... の使い方は？",
         [{"id":"A","text":"[...arr] や {...obj}"},{"id":"B","text":"arr..."},{"id":"C","text":"...arr()"},{"id":"D","text":"エラー"}],
         [0], "ES6", "2", 8, "配列やオブジェクトの展開", "スプレッド演算子"),
        
        ("レスト引数 ...args の役割は？",
         [{"id":"A","text":"可変長引数を配列化"},{"id":"B","text":"引数を展開"},{"id":"C","text":"引数を削除"},{"id":"D","text":"エラー"}],
         [0], "ES6", "2", 8, "残りの引数を配列にまとめる", "レスト引数"),
        
        ("デフォルト引数の書き方は？",
         [{"id":"A","text":"function f(x = 1){}"},{"id":"B","text":"function f(x := 1){}"},{"id":"C","text":"function f(x: 1){}"},{"id":"D","text":"エラー"}],
         [0], "ES6", "1", 5, "引数にデフォルト値を設定", "デフォルト引数"),
        
        ("Symbolの特徴は？",
         [{"id":"A","text":"一意な値"},{"id":"B","text":"文字列"},{"id":"C","text":"数値"},{"id":"D","text":"オブジェクト"}],
         [0], "ES6", "3", 10, "プリミティブで一意な識別子", "Symbol"),
    ]
    
    questions.extend(module_questions)
    print(f"  ✓ モジュールと実践パターン: {len(module_questions)}問")
    
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
        """, ("JavaScript", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'JavaScript'")
    js_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ JavaScript問題追加完了（第2弾）！")
    print("=" * 60)
    print(f"JavaScript問題数: {js_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標100問まで残り: {max(0, 100 - js_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_javascript_batch2()