import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_java_50_questions_part2():
    """Java問題50問追加（第2弾：65問→115問）OOP編"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Java問題追加スクリプト（第2弾：OOP編50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== クラスとオブジェクト（12問） ====================
    print("[1/5] クラスとオブジェクト問題を生成中...")
    
    class_object = [
        ("クラスの定義キーワードは？",
         [{"id":"A","text":"class"},{"id":"B","text":"Class"},{"id":"C","text":"def"},{"id":"D","text":"object"}],
         [0], "クラス", "1", 5, "クラス定義", "class"),
        
        ("インスタンスの生成方法は？",
         [{"id":"A","text":"new クラス名()"},{"id":"B","text":"クラス名()"},{"id":"C","text":"create クラス名()"},{"id":"D","text":"instance クラス名()"}],
         [0], "クラス", "1", 5, "オブジェクト生成", "new"),
        
        ("コンストラクタの特徴は？",
         [{"id":"A","text":"クラス名と同じで戻り値なし"},{"id":"B","text":"任意の名前"},{"id":"C","text":"必ず戻り値あり"},{"id":"D","text":"staticメソッド"}],
         [0], "クラス", "2", 8, "初期化メソッド", "コンストラクタ"),
        
        ("デフォルトコンストラクタとは？",
         [{"id":"A","text":"引数なしで自動生成されるコンストラクタ"},{"id":"B","text":"必須コンストラクタ"},{"id":"C","text":"staticコンストラクタ"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "2", 8, "暗黙的生成", "デフォルト"),
        
        ("thisキーワードの役割は？",
         [{"id":"A","text":"現在のインスタンスを参照"},{"id":"B","text":"親クラス参照"},{"id":"C","text":"staticメンバー参照"},{"id":"D","text":"使用不可"}],
         [0], "クラス", "2", 8, "自己参照", "this"),
        
        ("this()の用途は？",
         [{"id":"A","text":"同じクラスの別コンストラクタ呼び出し"},{"id":"B","text":"親コンストラクタ呼び出し"},{"id":"C","text":"メソッド呼び出し"},{"id":"D","text":"使用不可"}],
         [0], "クラス", "3", 10, "コンストラクタチェーン", "this()"),
        
        ("インスタンス変数とクラス変数の違いは？",
         [{"id":"A","text":"インスタンスごと vs 全インスタンス共有"},{"id":"B","text":"同じ"},{"id":"C","text":"速度が違う"},{"id":"D","text":"不明"}],
         [0], "クラス", "2", 8, "変数のスコープ", "static変数"),
        
        ("ゲッター（getter）の役割は？",
         [{"id":"A","text":"privateフィールドの値を取得"},{"id":"B","text":"値を設定"},{"id":"C","text":"値を削除"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "2", 8, "アクセサメソッド", "getter"),
        
        ("セッター（setter）の役割は？",
         [{"id":"A","text":"privateフィールドに値を設定"},{"id":"B","text":"値を取得"},{"id":"C","text":"値を削除"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "2", 8, "ミューテータ", "setter"),
        
        ("メソッドのオーバーライドとは？",
         [{"id":"A","text":"親クラスのメソッドを子クラスで再定義"},{"id":"B","text":"同名で異なる引数"},{"id":"C","text":"メソッド削除"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "3", 10, "メソッド上書き", "override"),
        
        ("@Overrideアノテーションの役割は？",
         [{"id":"A","text":"オーバーライドの意図を明示・コンパイルチェック"},{"id":"B","text":"必須"},{"id":"C","text":"パフォーマンス向上"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "3", 10, "アノテーション", "@Override"),
        
        ("staticブロックの用途は？",
         [{"id":"A","text":"クラスロード時の初期化処理"},{"id":"B","text":"インスタンス生成時"},{"id":"C","text":"メソッド実行時"},{"id":"D","text":"非推奨"}],
         [0], "クラス", "4", 12, "クラス初期化", "static初期化子"),
    ]
    
    questions.extend(class_object)
    print(f"  ✓ クラスとオブジェクト: {len(class_object)}問")
    
    # ==================== 継承（10問） ====================
    print("[2/5] 継承問題を生成中...")
    
    inheritance = [
        ("継承のキーワードは？",
         [{"id":"A","text":"extends"},{"id":"B","text":"inherits"},{"id":"C","text":"inherit"},{"id":"D","text":"super"}],
         [0], "継承", "1", 5, "継承宣言", "extends"),
        
        ("Javaの継承は？",
         [{"id":"A","text":"単一継承（1つの親クラスのみ）"},{"id":"B","text":"多重継承可能"},{"id":"C","text":"継承不可"},{"id":"D","text":"不明"}],
         [0], "継承", "2", 8, "継承制約", "単一継承"),
        
        ("superキーワードの役割は？",
         [{"id":"A","text":"親クラスのメンバー参照"},{"id":"B","text":"現在のインスタンス参照"},{"id":"C","text":"staticメンバー参照"},{"id":"D","text":"使用不可"}],
         [0], "継承", "2", 8, "親クラス参照", "super"),
        
        ("super()の用途は？",
         [{"id":"A","text":"親クラスのコンストラクタ呼び出し"},{"id":"B","text":"自クラスのコンストラクタ"},{"id":"C","text":"メソッド呼び出し"},{"id":"D","text":"使用不可"}],
         [0], "継承", "3", 10, "親コンストラクタ", "super()"),
        
        ("子クラスのコンストラクタで最初に実行されるのは？",
         [{"id":"A","text":"親クラスのコンストラクタ（暗黙的super()）"},{"id":"B","text":"子クラスのフィールド初期化"},{"id":"C","text":"子クラスのメソッド"},{"id":"D","text":"不明"}],
         [0], "継承", "3", 10, "初期化順序", "コンストラクタチェーン"),
        
        ("finalクラスの特徴は？",
         [{"id":"A","text":"継承不可"},{"id":"B","text":"インスタンス化不可"},{"id":"C","text":"変更不可"},{"id":"D","text":"非推奨"}],
         [0], "継承", "3", 10, "継承禁止", "final class"),
        
        ("finalメソッドの特徴は？",
         [{"id":"A","text":"オーバーライド不可"},{"id":"B","text":"呼び出し不可"},{"id":"C","text":"削除不可"},{"id":"D","text":"非推奨"}],
         [0], "継承", "3", 10, "上書き禁止", "final method"),
        
        ("Object クラスの位置付けは？",
         [{"id":"A","text":"全クラスの最上位親クラス"},{"id":"B","text":"特定のクラス"},{"id":"C","text":"インターフェース"},{"id":"D","text":"使用不可"}],
         [0], "継承", "2", 8, "ルートクラス", "Object"),
        
        ("toString()メソッドの役割は？",
         [{"id":"A","text":"オブジェクトの文字列表現"},{"id":"B","text":"型変換"},{"id":"C","text":"比較"},{"id":"D","text":"削除"}],
         [0], "継承", "2", 8, "文字列化", "toString"),
        
        ("equals()メソッドの役割は？",
         [{"id":"A","text":"オブジェクトの内容比較"},{"id":"B","text":"参照比較"},{"id":"C","text":"型比較"},{"id":"D","text":"削除"}],
         [0], "継承", "3", 10, "等価判定", "equals"),
    ]
    
    questions.extend(inheritance)
    print(f"  ✓ 継承: {len(inheritance)}問")
    
    # ==================== インターフェース（10問） ====================
    print("[3/5] インターフェース問題を生成中...")
    
    interfaces = [
        ("インターフェースの定義キーワードは？",
         [{"id":"A","text":"interface"},{"id":"B","text":"Interface"},{"id":"C","text":"implements"},{"id":"D","text":"abstract"}],
         [0], "インターフェース", "1", 5, "インターフェース宣言", "interface"),
        
        ("インターフェースの実装キーワードは？",
         [{"id":"A","text":"implements"},{"id":"B","text":"extends"},{"id":"C","text":"inherit"},{"id":"D","text":"uses"}],
         [0], "インターフェース", "2", 8, "実装宣言", "implements"),
        
        ("インターフェースのメソッドは？",
         [{"id":"A","text":"デフォルトで public abstract"},{"id":"B","text":"private"},{"id":"C","text":"protected"},{"id":"D","text":"static"}],
         [0], "インターフェース", "3", 10, "メソッド修飾子", "public abstract"),
        
        ("インターフェースの変数は？",
         [{"id":"A","text":"デフォルトで public static final（定数）"},{"id":"B","text":"インスタンス変数"},{"id":"C","text":"private変数"},{"id":"D","text":"変数不可"}],
         [0], "インターフェース", "3", 10, "定数宣言", "public static final"),
        
        ("クラスは複数のインターフェースを実装できる？",
         [{"id":"A","text":"はい（カンマ区切り）"},{"id":"B","text":"いいえ（1つのみ）"},{"id":"C","text":"2つまで"},{"id":"D","text":"不可"}],
         [0], "インターフェース", "2", 8, "多重実装", "複数実装"),
        
        ("デフォルトメソッド（Java 8+）とは？",
         [{"id":"A","text":"インターフェースに実装を持つメソッド"},{"id":"B","text":"抽象メソッド"},{"id":"C","text":"staticメソッド"},{"id":"D","text":"非推奨"}],
         [0], "インターフェース", "4", 12, "default実装", "default method"),
        
        ("インターフェースにstaticメソッドを定義できる？",
         [{"id":"A","text":"はい（Java 8+）"},{"id":"B","text":"いいえ"},{"id":"C","text":"Java 11+"},{"id":"D","text":"非推奨"}],
         [0], "インターフェース", "3", 10, "static実装", "static method"),
        
        ("関数型インターフェースとは？",
         [{"id":"A","text":"抽象メソッドが1つだけのインターフェース"},{"id":"B","text":"複数メソッド"},{"id":"C","text":"メソッドなし"},{"id":"D","text":"非推奨"}],
         [0], "インターフェース", "4", 12, "ラムダ式用", "functional interface"),
        
        ("@FunctionalInterfaceアノテーションの役割は？",
         [{"id":"A","text":"関数型インターフェースであることを明示"},{"id":"B","text":"必須"},{"id":"C","text":"パフォーマンス向上"},{"id":"D","text":"非推奨"}],
         [0], "インターフェース", "4", 12, "関数型チェック", "@FunctionalInterface"),
        
        ("インターフェースは他のインターフェースを？",
         [{"id":"A","text":"extendsできる（複数可）"},{"id":"B","text":"implementsする"},{"id":"C","text":"継承不可"},{"id":"D","text":"不明"}],
         [0], "インターフェース", "3", 10, "インターフェース継承", "extends"),
    ]
    
    questions.extend(interfaces)
    print(f"  ✓ インターフェース: {len(interfaces)}問")
    
    # ==================== 抽象クラス・ポリモーフィズム（10問） ====================
    print("[4/5] 抽象クラス・ポリモーフィズム問題を生成中...")
    
    abstract_poly = [
        ("抽象クラスの定義キーワードは？",
         [{"id":"A","text":"abstract class"},{"id":"B","text":"abstract"},{"id":"C","text":"interface"},{"id":"D","text":"virtual"}],
         [0], "抽象クラス", "2", 8, "抽象クラス宣言", "abstract"),
        
        ("抽象クラスの特徴は？",
         [{"id":"A","text":"インスタンス化不可"},{"id":"B","text":"インスタンス化必須"},{"id":"C","text":"継承不可"},{"id":"D","text":"メソッドなし"}],
         [0], "抽象クラス", "2", 8, "インスタンス生成禁止", "abstract特性"),
        
        ("抽象メソッドの特徴は？",
         [{"id":"A","text":"実装を持たない（子クラスで実装）"},{"id":"B","text":"実装必須"},{"id":"C","text":"staticメソッド"},{"id":"D","text":"非推奨"}],
         [0], "抽象クラス", "2", 8, "実装強制", "abstract method"),
        
        ("抽象クラスはコンストラクタを持てる？",
         [{"id":"A","text":"はい（子クラスから呼ばれる）"},{"id":"B","text":"いいえ"},{"id":"C","text":"場合による"},{"id":"D","text":"不明"}],
         [0], "抽象クラス", "3", 10, "コンストラクタ保持", "abstract constructor"),
        
        ("抽象クラスとインターフェースの主な違いは？",
         [{"id":"A","text":"抽象クラスは実装を持てる"},{"id":"B","text":"同じ"},{"id":"C","text":"インターフェースが実装可"},{"id":"D","text":"不明"}],
         [0], "抽象クラス", "3", 10, "実装保持", "abstract vs interface"),
        
        ("ポリモーフィズム（多態性）とは？",
         [{"id":"A","text":"同じインターフェースで異なる実装"},{"id":"B","text":"多重継承"},{"id":"C","text":"オーバーロード"},{"id":"D","text":"非推奨"}],
         [0], "ポリモーフィズム", "3", 10, "多様性", "polymorphism"),
        
        ("アップキャストとは？",
         [{"id":"A","text":"子クラス型を親クラス型に変換"},{"id":"B","text":"親を子に変換"},{"id":"C","text":"型変換不可"},{"id":"D","text":"非推奨"}],
         [0], "ポリモーフィズム", "3", 10, "上位型変換", "upcast"),
        
        ("ダウンキャストとは？",
         [{"id":"A","text":"親クラス型を子クラス型に変換"},{"id":"B","text":"子を親に変換"},{"id":"C","text":"自動変換"},{"id":"D","text":"非推奨"}],
         [0], "ポリモーフィズム", "3", 10, "下位型変換", "downcast"),
        
        ("instanceof演算子の役割は？",
         [{"id":"A","text":"オブジェクトの型チェック"},{"id":"B","text":"インスタンス生成"},{"id":"C","text":"型変換"},{"id":"D","text":"削除"}],
         [0], "ポリモーフィズム", "2", 8, "型判定", "instanceof"),
        
        ("カプセル化とは？",
         [{"id":"A","text":"データと処理を1つにまとめ外部から隠蔽"},{"id":"B","text":"継承"},{"id":"C","text":"多態性"},{"id":"D","text":"非推奨"}],
         [0], "カプセル化", "3", 10, "情報隠蔽", "encapsulation"),
    ]
    
    questions.extend(abstract_poly)
    print(f"  ✓ 抽象クラス・ポリモーフィズム: {len(abstract_poly)}問")
    
    # ==================== アクセス修飾子・内部クラス・enum（8問） ====================
    print("[5/5] アクセス修飾子・内部クラス・enum問題を生成中...")
    
    modifiers_inner = [
        ("publicの意味は？",
         [{"id":"A","text":"どこからでもアクセス可能"},{"id":"B","text":"同じクラスのみ"},{"id":"C","text":"同じパッケージのみ"},{"id":"D","text":"子クラスのみ"}],
         [0], "アクセス修飾子", "1", 5, "公開", "public"),
        
        ("privateの意味は？",
         [{"id":"A","text":"同じクラス内のみアクセス可能"},{"id":"B","text":"どこでも可"},{"id":"C","text":"同じパッケージのみ"},{"id":"D","text":"子クラスのみ"}],
         [0], "アクセス修飾子", "1", 5, "非公開", "private"),
        
        ("protectedの意味は？",
         [{"id":"A","text":"同じパッケージ + 子クラス"},{"id":"B","text":"どこでも可"},{"id":"C","text":"同じクラスのみ"},{"id":"D","text":"同じパッケージのみ"}],
         [0], "アクセス修飾子", "2", 8, "限定公開", "protected"),
        
        ("修飾子なし（デフォルト）の意味は？",
         [{"id":"A","text":"同じパッケージ内のみ"},{"id":"B","text":"どこでも可"},{"id":"C","text":"同じクラスのみ"},{"id":"D","text":"子クラスのみ"}],
         [0], "アクセス修飾子", "2", 8, "パッケージプライベート", "default"),
        
        ("内部クラス（Inner Class）とは？",
         [{"id":"A","text":"クラス内に定義されたクラス"},{"id":"B","text":"継承クラス"},{"id":"C","text":"抽象クラス"},{"id":"D","text":"非推奨"}],
         [0], "内部クラス", "3", 10, "ネストクラス", "inner class"),
        
        ("static内部クラスの特徴は？",
         [{"id":"A","text":"外部クラスのインスタンスなしで生成可能"},{"id":"B","text":"インスタンス必須"},{"id":"C","text":"非推奨"},{"id":"D","text":"使用不可"}],
         [0], "内部クラス", "4", 12, "静的ネスト", "static nested"),
        
        ("enumの用途は？",
         [{"id":"A","text":"定数のグループ定義"},{"id":"B","text":"配列"},{"id":"C","text":"リスト"},{"id":"D","text":"非推奨"}],
         [0], "enum", "2", 8, "列挙型", "enumeration"),
        
        ("enumの定義例は？",
         [{"id":"A","text":"enum Day { MONDAY, TUESDAY, ... }"},{"id":"B","text":"class Day { ... }"},{"id":"C","text":"interface Day { ... }"},{"id":"D","text":"使用不可"}],
         [0], "enum", "2", 8, "列挙定義", "enum定義"),
    ]
    
    questions.extend(modifiers_inner)
    print(f"  ✓ アクセス修飾子・内部クラス・enum: {len(modifiers_inner)}問")
    
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
        """, ("Java", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'Java'")
    java_count = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'Java' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊 Java第2弾完了！ 🎊")
    print("=" * 60)
    print(f"Java問題数: {java_count}問 (65問 → {java_count}問)")
    print(f"全体問題数: {total_count}問")
    
    print("\n【Javaカテゴリ別内訳】")
    for cat, count in categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("✅ Phase 2 - バックエンド主要言語（進行中）")
    print("\n【Java進捗】")
    print(f"  🔄 Java: {java_count}問 / 150問（あと{150-java_count}問）")
    print("\n完了:")
    print("  ✅ 第1弾（基礎編）: データ型、演算子、配列、メソッド、文字列")
    print("  ✅ 第2弾（OOP編）: クラス、継承、インターフェース、抽象クラス、enum")
    print("\n次のステップ:")
    print("  → Java第3弾（応用編：+35問）で150問達成！")
    print("     コレクション、例外処理、ジェネリクス、ラムダ式、Stream API")
    print("=" * 60)

if __name__ == "__main__":
    add_java_50_questions_part2()