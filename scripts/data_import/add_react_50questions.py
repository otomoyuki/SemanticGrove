import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def add_react_50_questions():
    """React問題50問追加（30問→80問）"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("React問題追加スクリプト（50問）")
    print("=" * 60)
    
    questions = []
    
    # ==================== Hooks基礎（15問） ====================
    print("[1/5] Hooks基礎問題を生成中...")
    
    hooks_basic = [
        ("useStateで状態を更新する正しい方法は？",
         [{"id":"A","text":"setState(newValue)"},{"id":"B","text":"state = newValue"},{"id":"C","text":"this.setState(newValue)"},{"id":"D","text":"updateState(newValue)"}],
         [0], "Hooks", "2", 8, "状態更新", "useState"),
        
        ("useStateの初期値を関数で設定する利点は？",
         [{"id":"A","text":"初回レンダリング時のみ実行される"},{"id":"B","text":"毎回実行される"},{"id":"C","text":"高速化される"},{"id":"D","text":"利点はない"}],
         [0], "Hooks", "3", 10, "遅延初期化", "パフォーマンス"),
        
        ("useEffectの第2引数（依存配列）を空にすると？",
         [{"id":"A","text":"マウント時のみ実行"},{"id":"B","text":"毎回実行"},{"id":"C","text":"実行されない"},{"id":"D","text":"エラーになる"}],
         [0], "Hooks", "3", 10, "副作用制御", "useEffect"),
        
        ("useEffectのクリーンアップ関数の用途は？",
         [{"id":"A","text":"アンマウント時の処理"},{"id":"B","text":"マウント時の処理"},{"id":"C","text":"レンダリング時の処理"},{"id":"D","text":"不要"}],
         [0], "Hooks", "3", 12, "メモリリーク防止", "cleanup"),
        
        ("useEffectで依存配列を省略すると？",
         [{"id":"A","text":"毎回実行される"},{"id":"B","text":"一度だけ実行"},{"id":"C","text":"実行されない"},{"id":"D","text":"エラー"}],
         [0], "Hooks", "2", 8, "依存配列の役割", "レンダリング"),
        
        ("useContextの役割は？",
         [{"id":"A","text":"コンテキストの値を取得"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"メモ化"}],
         [0], "Hooks", "3", 10, "グローバル状態", "Context API"),
        
        ("useReducerが有用なケースは？",
         [{"id":"A","text":"複雑な状態ロジック"},{"id":"B","text":"単純な状態"},{"id":"C","text":"副作用処理"},{"id":"D","text":"常に使うべき"}],
         [0], "Hooks", "4", 12, "状態管理パターン", "useReducer"),
        
        ("useReducerのreducer関数の引数は？",
         [{"id":"A","text":"(state, action)"},{"id":"B","text":"(action, state)"},{"id":"C","text":"(props, state)"},{"id":"D","text":"(state)"}],
         [0], "Hooks", "3", 10, "Reducer関数", "引数順序"),
        
        ("useRefの主な用途は？",
         [{"id":"A","text":"DOM要素への参照"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"メモ化"}],
         [0], "Hooks", "2", 8, "参照保持", "useRef"),
        
        ("useRefで保持した値を変更しても再レンダリングは？",
         [{"id":"A","text":"発生しない"},{"id":"B","text":"発生する"},{"id":"C","text":"場合による"},{"id":"D","text":"エラー"}],
         [0], "Hooks", "3", 10, "再レンダリング制御", "currentプロパティ"),
        
        ("useLayoutEffectとuseEffectの違いは？",
         [{"id":"A","text":"実行タイミングが同期的"},{"id":"B","text":"機能が違う"},{"id":"C","text":"違いはない"},{"id":"D","text":"useLayoutEffectは非推奨"}],
         [0], "Hooks", "4", 12, "同期的副作用", "useLayoutEffect"),
        
        ("useImperativeHandleの用途は？",
         [{"id":"A","text":"親コンポーネントに公開する値をカスタマイズ"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"メモ化"}],
         [0], "Hooks", "5", 15, "Ref公開制御", "forwardRef"),
        
        ("useDebugValueの用途は？",
         [{"id":"A","text":"カスタムフックのデバッグ情報表示"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"必須機能"}],
         [0], "Hooks", "4", 12, "開発ツール連携", "useDebugValue"),
        
        ("Hooksのルール：呼び出し位置は？",
         [{"id":"A","text":"トップレベルのみ"},{"id":"B","text":"どこでも可"},{"id":"C","text":"関数内のみ"},{"id":"D","text":"条件分岐内のみ"}],
         [0], "Hooks", "3", 10, "Hooksルール", "呼び出し制約"),
        
        ("カスタムフックの命名規則は？",
         [{"id":"A","text":"useで始める"},{"id":"B","text":"handleで始める"},{"id":"C","text":"自由"},{"id":"D","text":"大文字で始める"}],
         [0], "Hooks", "2", 8, "命名規則", "カスタムフック"),
    ]
    
    questions.extend(hooks_basic)
    print(f"  ✓ Hooks基礎: {len(hooks_basic)}問")
    
    # ==================== パフォーマンス最適化（10問） ====================
    print("[2/5] パフォーマンス最適化問題を生成中...")
    
    performance = [
        ("useMemoの用途は？",
         [{"id":"A","text":"計算結果のメモ化"},{"id":"B","text":"関数のメモ化"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "パフォーマンス", "3", 10, "値のメモ化", "useMemo"),
        
        ("useCallbackの用途は？",
         [{"id":"A","text":"関数のメモ化"},{"id":"B","text":"計算結果のメモ化"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "パフォーマンス", "3", 10, "関数のメモ化", "useCallback"),
        
        ("React.memoの役割は？",
         [{"id":"A","text":"コンポーネントのメモ化"},{"id":"B","text":"値のメモ化"},{"id":"C","text":"関数のメモ化"},{"id":"D","text":"状態管理"}],
         [0], "パフォーマンス", "3", 12, "再レンダリング防止", "React.memo"),
        
        ("React.memoの比較関数（第2引数）の戻り値は？",
         [{"id":"A","text":"trueで再レンダリングスキップ"},{"id":"B","text":"falseで再レンダリングスキップ"},{"id":"C","text":"どちらでも同じ"},{"id":"D","text":"使用不可"}],
         [0], "パフォーマンス", "4", 12, "比較ロジック", "カスタム比較"),
        
        ("useTransitionの用途は？",
         [{"id":"A","text":"低優先度の状態更新"},{"id":"B","text":"高優先度の状態更新"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "パフォーマンス", "4", 15, "並行レンダリング", "useTransition"),
        
        ("useDeferredValueの用途は？",
         [{"id":"A","text":"値の更新を遅延"},{"id":"B","text":"値の更新を優先"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "パフォーマンス", "4", 15, "遅延更新", "useDeferredValue"),
        
        ("key属性の役割は？",
         [{"id":"A","text":"要素の識別"},{"id":"B","text":"スタイル指定"},{"id":"C","text":"イベント処理"},{"id":"D","text":"不要"}],
         [0], "パフォーマンス", "2", 8, "リスト最適化", "key"),
        
        ("keyにindexを使うべきでない理由は？",
         [{"id":"A","text":"順序変更時に問題が起きる"},{"id":"B","text":"エラーになる"},{"id":"C","text":"遅くなる"},{"id":"D","text":"問題ない"}],
         [0], "パフォーマンス", "3", 10, "Key選択", "アンチパターン"),
        
        ("Lazy Loadingの実装方法は？",
         [{"id":"A","text":"React.lazy()とSuspense"},{"id":"B","text":"import文のみ"},{"id":"C","text":"useEffect"},{"id":"D","text":"useState"}],
         [0], "パフォーマンス", "4", 12, "コード分割", "動的import"),
        
        ("Suspenseのfallback propsの役割は？",
         [{"id":"A","text":"ローディング中の表示"},{"id":"B","text":"エラー表示"},{"id":"C","text":"成功時の表示"},{"id":"D","text":"不要"}],
         [0], "パフォーマンス", "3", 10, "ローディング制御", "Suspense"),
    ]
    
    questions.extend(performance)
    print(f"  ✓ パフォーマンス最適化: {len(performance)}問")
    
    # ==================== コンポーネント設計（10問） ====================
    print("[3/5] コンポーネント設計問題を生成中...")
    
    component_design = [
        ("Propsのデフォルト値の設定方法は？",
         [{"id":"A","text":"関数の引数でデフォルト値を指定"},{"id":"B","text":"state内で指定"},{"id":"C","text":"useEffectで指定"},{"id":"D","text":"設定不可"}],
         [0], "コンポーネント設計", "2", 8, "デフォルトProps", "分割代入"),
        
        ("Propsのバリデーションには何を使う？",
         [{"id":"A","text":"PropTypes またはTypeScript"},{"id":"B","text":"useState"},{"id":"C","text":"useEffect"},{"id":"D","text":"バリデーション不可"}],
         [0], "コンポーネント設計", "3", 10, "型チェック", "PropTypes"),
        
        ("children propsの用途は？",
         [{"id":"A","text":"子要素の受け渡し"},{"id":"B","text":"親要素の受け渡し"},{"id":"C","text":"状態管理"},{"id":"D","text":"副作用処理"}],
         [0], "コンポーネント設計", "2", 8, "コンポーネント合成", "children"),
        
        ("Compound Componentパターンの特徴は？",
         [{"id":"A","text":"複数コンポーネントが協調動作"},{"id":"B","text":"単一コンポーネント"},{"id":"C","text":"状態なし"},{"id":"D","text":"使用非推奨"}],
         [0], "コンポーネント設計", "4", 12, "複合コンポーネント", "設計パターン"),
        
        ("Higher-Order Component (HOC)とは？",
         [{"id":"A","text":"コンポーネントを引数に取りコンポーネントを返す関数"},{"id":"B","text":"高速なコンポーネント"},{"id":"C","text":"大きなコンポーネント"},{"id":"D","text":"非推奨機能"}],
         [0], "コンポーネント設計", "4", 15, "コンポーネント拡張", "HOC"),
        
        ("Render Propsパターンとは？",
         [{"id":"A","text":"関数をpropsとして渡す"},{"id":"B","text":"JSXをpropsとして渡す"},{"id":"C","text":"文字列をpropsとして渡す"},{"id":"D","text":"非推奨"}],
         [0], "コンポーネント設計", "4", 12, "ロジック共有", "RenderProps"),
        
        ("Controlled Componentとは？",
         [{"id":"A","text":"Reactで値を管理するフォーム"},{"id":"B","text":"DOMで値を管理するフォーム"},{"id":"C","text":"読み取り専用フォーム"},{"id":"D","text":"エラーハンドリング"}],
         [0], "コンポーネント設計", "3", 10, "フォーム制御", "制御コンポーネント"),
        
        ("Uncontrolled Componentの特徴は？",
         [{"id":"A","text":"DOMが値を保持"},{"id":"B","text":"Reactが値を保持"},{"id":"C","text":"値を持たない"},{"id":"D","text":"非推奨"}],
         [0], "コンポーネント設計", "3", 10, "非制御コンポーネント", "ref使用"),
        
        ("forwardRefの用途は？",
         [{"id":"A","text":"子コンポーネントへのref転送"},{"id":"B","text":"状態管理"},{"id":"C","text":"副作用処理"},{"id":"D","text":"非推奨"}],
         [0], "コンポーネント設計", "4", 12, "Ref転送", "forwardRef"),
        
        ("Fragment (<>...</>)の用途は？",
         [{"id":"A","text":"余分なDOM要素を追加せずグループ化"},{"id":"B","text":"スタイル適用"},{"id":"C","text":"イベント処理"},{"id":"D","text":"非推奨"}],
         [0], "コンポーネント設計", "2", 8, "不要なDOM削減", "Fragment"),
    ]
    
    questions.extend(component_design)
    print(f"  ✓ コンポーネント設計: {len(component_design)}問")
    
    # ==================== 状態管理・Context（8問） ====================
    print("[4/5] 状態管理・Context問題を生成中...")
    
    state_context = [
        ("createContextの戻り値は？",
         [{"id":"A","text":"Contextオブジェクト"},{"id":"B","text":"状態値"},{"id":"C","text":"コンポーネント"},{"id":"D","text":"関数"}],
         [0], "状態管理", "3", 10, "Context作成", "createContext"),
        
        ("Context.Providerのvalue propsの役割は？",
         [{"id":"A","text":"配下に渡す値を指定"},{"id":"B","text":"初期値を指定"},{"id":"C","text":"型を指定"},{"id":"D","text":"不要"}],
         [0], "状態管理", "2", 8, "値の提供", "Provider"),
        
        ("useContextを使う際の注意点は？",
         [{"id":"A","text":"Provider内で使用する必要がある"},{"id":"B","text":"どこでも使える"},{"id":"C","text":"useStateと併用不可"},{"id":"D","text":"非推奨"}],
         [0], "状態管理", "3", 10, "Context消費", "スコープ"),
        
        ("Context値が変更されると？",
         [{"id":"A","text":"useContextを使う全コンポーネントが再レンダリング"},{"id":"B","text":"Provider直下のみ再レンダリング"},{"id":"C","text":"再レンダリングされない"},{"id":"D","text":"エラー"}],
         [0], "状態管理", "3", 12, "再レンダリング", "パフォーマンス影響"),
        
        ("状態のリフトアップとは？",
         [{"id":"A","text":"共通の親に状態を移動"},{"id":"B","text":"子に状態を移動"},{"id":"C","text":"削除"},{"id":"D","text":"複製"}],
         [0], "状態管理", "3", 10, "状態共有", "リフトアップ"),
        
        ("Prop Drillingの問題は？",
         [{"id":"A","text":"中間コンポーネントに不要なpropsを渡す"},{"id":"B","text":"パフォーマンスが良い"},{"id":"C","text":"問題ない"},{"id":"D","text":"エラー"}],
         [0], "状態管理", "3", 10, "Props伝播", "アンチパターン"),
        
        ("useReducerのdispatch関数の特徴は？",
         [{"id":"A","text":"再レンダリング間で同一"},{"id":"B","text":"毎回変わる"},{"id":"C","text":"使用不可"},{"id":"D","text":"非推奨"}],
         [0], "状態管理", "3", 10, "dispatch安定性", "useReducer"),
        
        ("複数のContextを使う場合の注意点は？",
         [{"id":"A","text":"Provider階層が深くなりすぎない工夫"},{"id":"B","text":"使用不可"},{"id":"C","text":"1つまで"},{"id":"D","text":"制限なし"}],
         [0], "状態管理", "4", 12, "Context組み合わせ", "Provider階層"),
    ]
    
    questions.extend(state_context)
    print(f"  ✓ 状態管理・Context: {len(state_context)}問")
    
    # ==================== エラーハンドリング・その他（7問） ====================
    print("[5/5] エラーハンドリング・その他問題を生成中...")
    
    error_others = [
        ("Error Boundaryの実装方法は？",
         [{"id":"A","text":"クラスコンポーネントで実装"},{"id":"B","text":"関数コンポーネントで実装"},{"id":"C","text":"Hooks使用"},{"id":"D","text":"実装不可"}],
         [0], "エラーハンドリング", "4", 12, "エラー捕捉", "ErrorBoundary"),
        
        ("componentDidCatchの役割は？",
         [{"id":"A","text":"子のエラーを捕捉"},{"id":"B","text":"自身のエラー捕捉"},{"id":"C","text":"親のエラー捕捉"},{"id":"D","text":"非推奨"}],
         [0], "エラーハンドリング", "4", 12, "エラーログ", "ライフサイクル"),
        
        ("StrictModeの役割は？",
         [{"id":"A","text":"開発時の問題検出"},{"id":"B","text":"本番最適化"},{"id":"C","text":"エラー修正"},{"id":"D","text":"非推奨"}],
         [0], "デバッグ", "3", 10, "開発モード", "StrictMode"),
        
        ("Portalの用途は？",
         [{"id":"A","text":"親のDOM階層外にレンダリング"},{"id":"B","text":"高速レンダリング"},{"id":"C","text":"状態管理"},{"id":"D","text":"非推奨"}],
         [0], "応用", "4", 12, "DOM操作", "createPortal"),
        
        ("React.PureComponentの特徴は？",
         [{"id":"A","text":"浅い比較でshouldComponentUpdateを実装"},{"id":"B","text":"深い比較"},{"id":"C","text":"比較なし"},{"id":"D","text":"非推奨"}],
         [0], "パフォーマンス", "4", 12, "最適化", "PureComponent"),
        
        ("React Developer Toolsで確認できることは？",
         [{"id":"A","text":"コンポーネント階層と状態"},{"id":"B","text":"ソースコードのみ"},{"id":"C","text":"使用不可"},{"id":"D","text":"HTML要素のみ"}],
         [0], "デバッグ", "2", 8, "開発ツール", "DevTools"),
        
        ("React 18のConcurrent Renderingの特徴は？",
         [{"id":"A","text":"レンダリングを中断・再開可能"},{"id":"B","text":"同期的レンダリング"},{"id":"C","text":"非推奨"},{"id":"D","text":"変更なし"}],
         [0], "応用", "5", 15, "並行モード", "React18"),
    ]
    
    questions.extend(error_others)
    print(f"  ✓ エラーハンドリング・その他: {len(error_others)}問")
    
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
        """, ("React", json.dumps(question_json, ensure_ascii=False), 
              q[3], q[4], q[5], q[6], q[7]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'React'")
    react_count = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'React' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊 React 80問達成！ 🎊")
    print("=" * 60)
    print(f"React問題数: {react_count}問 (30問 → {react_count}問)")
    print(f"全体問題数: {total_count}問")
    
    print("\n【Reactカテゴリ別内訳】")
    for cat, count in categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("✅ Phase 1 - フロントエンド基礎（進行中）")
    print("\n【達成状況】")
    print(f"  ✅ React: {react_count}問 / 80問 ← 完了！")
    print("  🎯 CSS: 20問 / 100問（+80問必要）")
    print("  🎯 HTML: 20問 / 80問（+60問必要）")
    print("\n次のステップ:")
    print("  → CSS 80問追加でフロントエンド強化！")
    print("=" * 60)

if __name__ == "__main__":
    add_react_50_questions()