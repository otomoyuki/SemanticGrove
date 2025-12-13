import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_javascript_batch1():
    """JavaScript問題追加（第1弾・30問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("JavaScript問題追加スクリプト（第1弾・30問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== オブジェクト操作（10問） ====================
    print("[1/3] オブジェクト操作問題を生成中...")
    
    object_questions = [
        ("オブジェクトのプロパティにアクセスする方法は？",
         [{"id":"A","text":"obj.key または obj['key']"},{"id":"B","text":"obj->key"},{"id":"C","text":"obj::key"},{"id":"D","text":"obj@key"}],
         [0], "オブジェクト", "1", 5, "ドット記法とブラケット記法", "基本操作"),
        
        ("const obj = {a: 1, b: 2}; Object.keys(obj)の結果は？",
         [{"id":"A","text":"['a', 'b']"},{"id":"B","text":"[1, 2]"},{"id":"C","text":"['a', 1, 'b', 2]"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "2", 8, "キーの配列を返す", "Object.keys()"),
        
        ("const obj = {a: 1}; delete obj.a; の後のobj.aは？",
         [{"id":"A","text":"undefined"},{"id":"B","text":"null"},{"id":"C","text":"0"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "2", 8, "プロパティが削除される", "delete演算子"),
        
        ("Object.assign({a: 1}, {b: 2})の結果は？",
         [{"id":"A","text":"{a: 1, b: 2}"},{"id":"B","text":"{b: 2}"},{"id":"C","text":"[1, 2]"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "2", 8, "オブジェクトをマージ", "Object.assign()"),
        
        ("const {a, b} = {a: 1, b: 2}; の後のaの値は？",
         [{"id":"A","text":"1"},{"id":"B","text":"2"},{"id":"C","text":"undefined"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "2", 8, "分割代入", "Destructuring"),
        
        ("'key' in {key: 1}の結果は？",
         [{"id":"A","text":"true"},{"id":"B","text":"false"},{"id":"C","text":"1"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "2", 8, "プロパティの存在確認", "in演算子"),
        
        ("Object.values({a: 1, b: 2})の結果は？",
         [{"id":"A","text":"[1, 2]"},{"id":"B","text":"['a', 'b']"},{"id":"C","text":"{a: 1, b: 2}"},{"id":"D","text":"3"}],
         [0], "オブジェクト", "2", 8, "値の配列を返す", "Object.values()"),
        
        ("const obj = {}; obj.x = 10; obj.xの値は？",
         [{"id":"A","text":"10"},{"id":"B","text":"undefined"},{"id":"C","text":"null"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "1", 5, "動的にプロパティを追加", "プロパティ追加"),
        
        ("Object.freeze()したオブジェクトは？",
         [{"id":"A","text":"変更不可"},{"id":"B","text":"読み取り不可"},{"id":"C","text":"削除不可のみ"},{"id":"D","text":"影響なし"}],
         [0], "オブジェクト", "3", 10, "イミュータブルにする", "Object.freeze()"),
        
        ("...演算子でオブジェクトをコピー：{...obj}",
         [{"id":"A","text":"シャローコピー"},{"id":"B","text":"ディープコピー"},{"id":"C","text":"参照コピー"},{"id":"D","text":"エラー"}],
         [0], "オブジェクト", "3", 10, "スプレッド構文", "シャローコピー"),
    ]
    
    questions.extend(object_questions)
    print(f"  ✓ オブジェクト操作: {len(object_questions)}問")
    
    # ==================== 配列の高度な操作（10問） ====================
    print("[2/3] 配列の高度な操作問題を生成中...")
    
    array_advanced = [
        ("[1, 2, 3].reduce((a, b) => a + b, 0)の結果は？",
         [{"id":"A","text":"6"},{"id":"B","text":"123"},{"id":"C","text":"[1,2,3]"},{"id":"D","text":"エラー"}],
         [0], "配列メソッド", "3", 10, "配列の合計を計算", "reduce()"),
        
        ("[1, 2, 3].find(x => x > 1)の結果は？",
         [{"id":"A","text":"2"},{"id":"B","text":"[2, 3]"},{"id":"C","text":"true"},{"id":"D","text":"1"}],
         [0], "配列メソッド", "2", 8, "条件に合う最初の要素", "find()"),
        
        ("[1, 2, 3].every(x => x > 0)の結果は？",
         [{"id":"A","text":"true"},{"id":"B","text":"false"},{"id":"C","text":"3"},{"id":"D","text":"[1,2,3]"}],
         [0], "配列メソッド", "2", 8, "全要素が条件を満たすか", "every()"),
        
        ("[1, 2, 3].some(x => x > 2)の結果は？",
         [{"id":"A","text":"true"},{"id":"B","text":"false"},{"id":"C","text":"3"},{"id":"D","text":"[3]"}],
         [0], "配列メソッド", "2", 8, "いずれかが条件を満たすか", "some()"),
        
        ("[[1, 2], [3, 4]].flat()の結果は？",
         [{"id":"A","text":"[1, 2, 3, 4]"},{"id":"B","text":"[[1,2],[3,4]]"},{"id":"C","text":"10"},{"id":"D","text":"エラー"}],
         [0], "配列メソッド", "2", 8, "配列を平坦化", "flat()"),
        
        ("[1, 2].flatMap(x => [x, x * 2])の結果は？",
         [{"id":"A","text":"[1, 2, 2, 4]"},{"id":"B","text":"[1, 2]"},{"id":"C","text":"[[1,2],[2,4]]"},{"id":"D","text":"エラー"}],
         [0], "配列メソッド", "3", 10, "mapしてflat", "flatMap()"),
        
        ("[...new Set([1, 1, 2, 2, 3])]の結果は？",
         [{"id":"A","text":"[1, 2, 3]"},{"id":"B","text":"[1, 1, 2, 2, 3]"},{"id":"C","text":"6"},{"id":"D","text":"エラー"}],
         [0], "配列", "3", 10, "重複を削除", "Set + スプレッド"),
        
        ("[1, 2, 3].findIndex(x => x === 2)の結果は？",
         [{"id":"A","text":"1"},{"id":"B","text":"2"},{"id":"C","text":"0"},{"id":"D","text":"-1"}],
         [0], "配列メソッド", "2", 8, "条件に合う要素のインデックス", "findIndex()"),
        
        ("Array.from('abc')の結果は？",
         [{"id":"A","text":"['a','b','c']"},{"id":"B","text":"'abc'"},{"id":"C","text":"3"},{"id":"D","text":"エラー"}],
         [0], "配列", "2", 8, "文字列を配列に変換", "Array.from()"),
        
        ("[1, 2, 3].fill(0)の結果は？",
         [{"id":"A","text":"[0, 0, 0]"},{"id":"B","text":"[1, 2, 3, 0]"},{"id":"C","text":"0"},{"id":"D","text":"エラー"}],
         [0], "配列メソッド", "2", 8, "配列を指定値で埋める", "fill()"),
    ]
    
    questions.extend(array_advanced)
    print(f"  ✓ 配列の高度な操作: {len(array_advanced)}問")
    
    # ==================== 非同期処理（10問） ====================
    print("[3/3] 非同期処理問題を生成中...")
    
    async_questions = [
        ("Promise.resolve(1).then(x => x + 1)の最終結果は？",
         [{"id":"A","text":"2"},{"id":"B","text":"1"},{"id":"C","text":"Promise"},{"id":"D","text":"エラー"}],
         [0], "非同期処理", "3", 10, "Promiseのthen", "Promise"),
        
        ("async function f() { return 1; } の返り値の型は？",
         [{"id":"A","text":"Promise"},{"id":"B","text":"Number"},{"id":"C","text":"Function"},{"id":"D","text":"undefined"}],
         [0], "非同期処理", "3", 10, "async関数は常にPromiseを返す", "async/await"),
        
        ("await式が使えるのは？",
         [{"id":"A","text":"async関数内"},{"id":"B","text":"どこでも"},{"id":"C","text":"Promiseの中"},{"id":"D","text":"関数外"}],
         [0], "非同期処理", "2", 8, "async関数内でのみ使用可能", "await"),
        
        ("Promise.all([p1, p2])の動作は？",
         [{"id":"A","text":"全て成功で解決"},{"id":"B","text":"最初の1つ成功で解決"},{"id":"C","text":"最後の1つ成功で解決"},{"id":"D","text":"並列実行しない"}],
         [0], "非同期処理", "3", 12, "全てのPromiseが解決するまで待つ", "Promise.all()"),
        
        ("Promise.race([p1, p2])の動作は？",
         [{"id":"A","text":"最初に解決した結果を返す"},{"id":"B","text":"全て解決するまで待つ"},{"id":"C","text":"最後の結果を返す"},{"id":"D","text":"エラー"}],
         [0], "非同期処理", "3", 12, "最初に完了したPromiseの結果", "Promise.race()"),
        
        ("try-catchでPromiseのエラーを捕捉するには？",
         [{"id":"A","text":"awaitと一緒に使う"},{"id":"B","text":"thenの中で"},{"id":"C","text":"不可能"},{"id":"D","text":"finallyで"}],
         [0], "非同期処理", "3", 12, "async/awaitでのエラーハンドリング", "try-catch"),
        
        (".catch()メソッドの役割は？",
         [{"id":"A","text":"エラーハンドリング"},{"id":"B","text":"成功処理"},{"id":"C","text":"遅延実行"},{"id":"D","text":"キャンセル"}],
         [0], "非同期処理", "2", 8, "Promiseのエラーを捕捉", "catch()"),
        
        (".finally()は何時実行される？",
         [{"id":"A","text":"成功・失敗に関わらず"},{"id":"B","text":"成功時のみ"},{"id":"C","text":"失敗時のみ"},{"id":"D","text":"実行されない"}],
         [0], "非同期処理", "2", 8, "Promiseの最終処理", "finally()"),
        
        ("setTimeout(() => console.log('a'), 0)の実行タイミングは？",
         [{"id":"A","text":"非同期（後回し）"},{"id":"B","text":"即座に"},{"id":"C","text":"1秒後"},{"id":"D","text":"実行されない"}],
         [0], "非同期処理", "3", 12, "イベントループで後回し", "イベントループ"),
        
        ("Promise.reject('err').catch(e => e)の結果は？",
         [{"id":"A","text":"'err'で解決されたPromise"},{"id":"B","text":"エラー"},{"id":"C","text":"undefined"},{"id":"D","text":"null"}],
         [0], "非同期処理", "4", 15, "catchは新しいPromiseを返す", "エラーハンドリング"),
    ]
    
    questions.extend(async_questions)
    print(f"  ✓ 非同期処理: {len(async_questions)}問")
    
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
    print("✓ JavaScript問題追加完了（第1弾）！")
    print("=" * 60)
    print(f"JavaScript問題数: {js_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標100問まで残り: {max(0, 100 - js_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_javascript_batch1()