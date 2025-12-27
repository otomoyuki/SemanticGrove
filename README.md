# 🌲 SemanticGrove

**無料で使える！17言語2240問のプログラミング学習アプリ**

60歳からプログラミングを学び、半年で開発した学習サイトです。  
登録不要、完全無料で今すぐ使えます。

🌐 **今すぐ試す** → https://semanticgrove.onrender.com

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎮 使い方（3ステップ）

### 1. サイトにアクセス
[https://semanticgrove.onrender.com](https://semanticgrove.onrender.com) を開く

### 2. 好きなモードと言語を選ぶ
- 学習モード / 初級 / 中級 / 上級 から選択
- Python、JavaScript など17種類の言語から選択

### 3. 問題を解く
- 10/20/30/50問から選べる
- 選択肢はランダム表示（真の理解が試される！）
- 間違えても解説で学べる

**それだけ！** 登録不要、完全無料です。

---

## ✨ 何ができる？

### 📖 学習モード
- 問題と解説を同時に表示
- じっくり理解しながら学習
- 初心者におすすめ

### 🌱 初級モード
- 基礎問題を解説付きで
- 基礎固めに最適
- プログラミング始めたての人向け

### 🌿 中級モード
- 正答率を記録
- 実力テストに
- 基礎を固めた人向け

### 🌲 上級モード
- タイマー付き
- 苦手な問題を自動的に多く出題
- 本格的な実力試し

### 🎁 特典
- 学習でSGポイント獲得
- フィードバック投稿で+10 SG
- 将来のゲーム機能で使えます

---

## 🚀 今後の予定

### 近日実装予定
- ✅ **ゲーム広場** - 遊びながら学べる8種類のゲーム
- ✅ **記憶の巨大樹** - ユーザー投稿＋公式ストーリー
- 🔜 **甲虫戦争ゲーム統合** - SGポイントでバトル！

### 将来の展望
- 📱 スマホアプリ化
- 🏆 ランキング・実績システム
- 👥 ユーザー同士の交流機能
- 🤖 AI学習アシスタント

---

## 💻 対応言語（17種類・2240問）

### フロントエンド（544問）
- **HTML** (80問) - Webページの骨組み
- **CSS** (100問) - デザイン・レイアウト
- **JavaScript** (104問) - Webの動き
- **React** (80問) - 人気のフレームワーク
- **TypeScript** (80問) - 型付きJavaScript

### バックエンド（1231問）
- **Python** (314問) ⭐ 試験対策200問含む
- **PHP** (203問) ⭐ PHP8試験対策100問含む
- **Java** (150問)
- **C#** (150問)
- **Ruby** (80問)
- **Go** (80問)

### その他（465問）
- **IQ問題** (350問) - 数列、論理パズルなど
- **SQL** - データベース
- **VBA** - Excel自動化
- **COBOL** - レガシーシステム
- その他多数

---

## 👨‍💻 作った人について

**60歳からプログラミングを始めました。**

- 📅 2025年5月: プログラミング学習開始
- 🎉 2025年12月: SemanticGrove v1.0 完成
- ⏱️ 学習期間: 約半年
- 🎯 2025年12月: 再就職決定！


---

## 🙏 お願い

### ⭐ GitHubスター
役に立ったら、ぜひスターをお願いします！

### 🐛 バグ報告
- アプリ内の「ご意見」ボタン
- または [GitHub Issues](https://github.com/otomoyuki/SemanticGrove/issues)

**問題が間違っているところが多数あると思います。ご連絡お待ちしています。**

### 💬 フィードバック
アプリ内からフィードバック送信で **+10 SG** 獲得！

---

## 📞 お問い合わせ

- アプリ内「ご意見」ボタン
- GitHub Issues
- Twitter（準備中）

---

## 🌟 スクリーンショット

（後で追加予定）

---

---

## 🔧 技術者向け情報

**↓ ここから下は開発者・技術者向けの情報です ↓**

---

## 📁 プロジェクト構造

```
SemanticGrove/
├── app/
│   └── app_main.py          # メインアプリケーション（Flask）
├── static/
│   ├── style.css            # スタイルシート
│   ├── practice-low.js      # 初級モード
│   ├── practice-middle.js   # 中級モード
│   ├── practice-high.js     # 上級モード（重み付き出題）
│   └── images/              # 画像問題（IQ問題など）
├── templates/
│   ├── main.html            # ホームページ
│   ├── learn.html           # 学習モード
│   ├── practice-*.html      # 各練習モード
│   ├── game-hub.html        # ゲーム広場
│   └── feedback.html        # フィードバックフォーム
├── models.py                # データベースモデル
├── app_config.py            # 設定ファイル
├── SemanticGrove.db         # SQLiteデータベース（問題データ）
├── requirements.txt         # Python依存パッケージ
└── README.md               # このファイル
```

---

## 🛠️ 技術スタック

### Backend
- **Python 3.8+**
- **Flask 3.0.0** - Webフレームワーク
- **SQLAlchemy** - ORM

### Frontend
- **HTML5**
- **CSS3** - レスポンシブデザイン
- **Vanilla JavaScript** - フレームワーク不使用

### Database
- **SQLite** - 問題データ（読み取り専用）
- **PostgreSQL** - ユーザーデータ（本番環境）
  - Renderで自動プロビジョニング
  - ユーザー情報、学習履歴、SGポイント

### Deployment
- **Render** - 本番環境
- **Gunicorn** - WSGIサーバー

---

## 💿 ローカル環境セットアップ

### 前提条件
- Python 3.8以上
- pip

### インストール手順

```bash
# 1. リポジトリをクローン
git clone https://github.com/otomoyuki/SemanticGrove.git
cd SemanticGrove

# 2. 仮想環境を作成（推奨）
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. 依存パッケージをインストール
pip install -r requirements.txt

# 4. 環境変数を設定（.envファイル作成）
# FLASK_APP=app/app_main.py
# FLASK_ENV=development
# SECRET_KEY=your-secret-key
# DATABASE_URL=postgresql://localhost/semanticgrove_users

# 5. データベース初期化（初回のみ）
# 問題データ（SemanticGrove.db）は既に含まれています
# PostgreSQLは自動で初期化されます

# 6. アプリを起動
python app/app_main.py
```

ブラウザで `http://localhost:5000` を開く

---

## 🗄️ データベース設計

### SQLite（問題データ）
```sql
questions テーブル
├─ id: INTEGER PRIMARY KEY
├─ language: TEXT (言語名)
├─ question_json: TEXT (問題・選択肢・正解のJSON)
├─ category: TEXT (カテゴリ)
├─ difficulty: TEXT (難易度 1-10)
├─ meaning: TEXT (解説)
└─ usage: TEXT (学習ポイント)
```

### PostgreSQL（ユーザーデータ）
```sql
users テーブル
├─ id: SERIAL PRIMARY KEY
├─ username: VARCHAR(80)
├─ session_id: VARCHAR(36) UNIQUE
├─ sg_points: INTEGER (SGポイント残高)
└─ created_at: TIMESTAMP

question_history テーブル
├─ id: SERIAL PRIMARY KEY
├─ user_id: INTEGER (外部キー)
├─ question_id: INTEGER
├─ correct_count: INTEGER (正解数)
├─ wrong_count: INTEGER (不正解数)
├─ total_count: INTEGER (回答数)
└─ mode: VARCHAR(20) (モード)

point_history テーブル
├─ id: SERIAL PRIMARY KEY
├─ user_id: INTEGER (外部キー)
├─ points: INTEGER (獲得ポイント)
├─ reason: VARCHAR(100) (獲得理由)
└─ created_at: TIMESTAMP
```

---

## 🎯 主要機能の実装

### 重み付き出題システム
ユーザーの回答履歴から苦手な問題を自動的に多く出題：

```python
def get_weighted_questions(user_id, language, mode, limit=10):
    # 未出題問題: weight=15（最優先）
    # 全問不正解: weight=10
    # 正解率<30%: weight=8
    # 正解率<50%: weight=6
    # ...
```

### SGポイントシステム
学習活動でポイント獲得：

- 学習モード: +1 SG/問
- 初級モード: +2 SG/問
- 中級モード: +3 SG/問
- 上級モード: +5 SG/問
- フィードバック投稿: +10 SG

---

## 🌐 デプロイ（Render）

### 1. requirements.txt
```txt
Flask==3.0.0
gunicorn==21.2.0
SQLAlchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0
Flask-Login==0.6.3
```

### 2. Procfile（不要）
Renderは自動検出します

### 3. 環境変数（Renderダッシュボード）
```
FLASK_ENV=production
SECRET_KEY=ランダムな文字列
DATABASE_URL=（Renderが自動設定）
```

### 4. デプロイ
```bash
git push origin main
```

Renderが自動でビルド・デプロイします

---

## 🧪 テスト

```bash
# ユニットテスト（準備中）
python -m pytest tests/

# 手動テスト
# 各モードで問題を解いて動作確認
```

---

## 🤝 コントリビューション

プルリクエスト、バグ報告、機能要望を歓迎します！

### 貢献方法

1. このリポジトリをフォーク
2. 機能ブランチを作成
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. 変更をコミット
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. ブランチにプッシュ
   ```bash
   git push origin feature/amazing-feature
   ```
5. プルリクエストを作成

### 開発ガイドライン

- コードは読みやすく、コメント付きで
- 新機能にはテストを追加
- READMEを更新（必要な場合）

---

## 📝 ライセンス

MIT License - 自由に使用・改変・配布できます

詳細は [LICENSE](LICENSE) ファイルを参照してください。

---

## 🙏 謝辞

このプロジェクトは多くの方々の支援によって実現しました：

- **Anthropic Claude** - 開発サポート・ペアプログラミング
- **Flask** - 素晴らしいWebフレームワーク
- **Render** - 簡単なデプロイ環境
- **すべてのテスター** - フィードバックと励まし
- **家族** - 理解と応援

---

## 📚 参考資料

- [Flask公式ドキュメント](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)

---

## 🎓 学習リソース

SemanticGroveで学習した後のステップアップ：

- **公式ドキュメント** - 各言語の公式サイト
- **MDN Web Docs** - Web技術のリファレンス
- **GitHub** - オープンソースプロジェクトで実践
- **LeetCode / HackerRank** - コーディング練習

---

⭐ **役に立ったら、GitHubでスターをお願いします！** ⭐

---

**Let's code together! 🌲✨**