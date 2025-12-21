# 🌲 SemanticGrove

**60歳からプログラミングを学び、半年で開発した無料学習アプリ**

17言語、2240問の実践的なプログラミング問題で、あなたのスキルを磨きましょう！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)

---

## 🎯 特徴

### 📚 豊富な問題数
- **2240問**の実践的な問題
- **17のプログラミング言語**に対応
- 基礎から応用まで幅広くカバー

### 🎮 4つの学習モード

#### 📖 学習モード
- 問題と解説を同時に表示
- じっくり理解しながら学習
- 初心者におすすめ

#### 🌱 初級モード
- 選択肢あり
- 解説を最初から表示
- 基礎固めに最適

#### 🌿 中級モード
- 選択肢あり
- 正答率を記録
- 実力テストに

#### 🌲 上級モード
- 選択肢あり
- タイマー付き
- 誤答率で出題頻度を調整
- 本格的な実力試し

### ✨ 独自機能

- **選択肢ランダム表示**: ラベル（A, B, C, D）なしで真の理解度をチェック
- **問題数カスタマイズ**: 10/20/30/50問から選択可能
- **画像問題対応**: 図形パターンなど視覚的な問題
- **SGポイントシステム**: 学習でポイントを獲得（将来の機能拡張に使用）

---

## 💻 対応言語

### フロントエンド
- HTML (80問)
- CSS (100問)
- JavaScript (104問)
- React (80問)
- TypeScript (80問)

### バックエンド
- Python (314問) - 試験対策200問含む
- PHP (203問) - PHP8試験対策100問含む
- Java (150問)
- C# (150問)
- Ruby (80問)
- Go (80問)

### その他
- IQ問題 (350問) - 数列、論理パズルなど
- SQL
- VBA
- COBOL
- その他多数

---

## 🚀 クイックスタート

### 前提条件
- Python 3.8以上
- pip

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/SemanticGrove.git
cd SemanticGrove

# 仮想環境を作成（推奨）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存パッケージをインストール
pip install -r requirements.txt

# データベース初期化（初回のみ）
python init_database.py

# アプリを起動
python run.py
```

ブラウザで `http://localhost:5000` を開く

---

## 📁 プロジェクト構造

```
SemanticGrove/
├── app/
│   └── app_main.py          # メインアプリケーション
├── static/
│   ├── style.css            # スタイルシート
│   ├── practice-low.js      # 初級モード
│   ├── practice-middle.js   # 中級モード
│   ├── practice-high.js     # 上級モード
│   └── images/              # 画像問題
├── templates/
│   ├── main.html            # ホームページ
│   ├── learn.html           # 学習モード
│   ├── practice-*.html      # 各練習モード
│   └── ...
├── SemanticGrove.db         # SQLiteデータベース
├── requirements.txt         # Python依存パッケージ
└── README.md               # このファイル
```

---

## 🎨 使い方

### 1. ホーム画面からモードを選択

### 2. 言語を選択
17種類のプログラミング言語から選択

### 3. 問題数を選択
10/20/30/50問から選択（上級モードは100問も可能）

### 4. 学習開始！
- 選択肢はランダム表示（ラベルなし）
- 真の理解が求められる
- 間違えても解説で学べる

---

## 🗄️ データベース

### 問題データ
- **SQLite**: 問題データ（読み取り専用）
- スマホアプリ化を見据えた設計
- オフラインでも動作可能

### ユーザーデータ（予定）
- **PostgreSQL**: ユーザー情報、学習履歴
- Renderデプロイ時に自動で使用
- 複数デバイスで同期

---

## 🌐 デプロイ

### Render（推奨）

```bash
# requirements.txtに記載
Flask==3.0.0
gunicorn==21.2.0

# Procfile作成
web: gunicorn app.app_main:app

# Renderにプッシュ
git push origin main
```

### Heroku

```bash
# Procfile作成
web: gunicorn app.app_main:app

# デプロイ
git push heroku main
```

---

## 🛠️ 技術スタック

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (開発), PostgreSQL (本番)
- **Deployment**: Render / Heroku

---

## 📊 今後の予定

### 近日実装予定
- ✅ フィードバック機能（投稿で10 SG獲得）
- ✅ ランキング機能
- ✅ IQ問題の画像選択肢（150問追加）

### 将来の展望
- 🎮 甲虫戦争ゲーム統合（SGポイント活用）
- 📱 スマホアプリ化
- 🏆 実績システム
- 👥 ソーシャル機能
- 🤖 AI学習アシスタント

---

## 🎓 開発者について

**60歳からプログラミングを始めました。**

- 2024年5月: プログラミング学習開始
- 2024年12月: SemanticGrove v1.0 完成
- 学習期間: 約半年

「年齢は関係ない。始めるのに遅すぎることはない」

---

## 📝 ライセンス

MIT License - 自由に使用・改変・配布できます

---

## 🤝 コントリビューション

プルリクエスト、バグ報告、機能要望を歓迎します！

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

---

## 📞 お問い合わせ

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- アプリ内「ご意見・ご要望」フォームからも受付中

---

## 🙏 謝辞

このプロジェクトは多くの方々の支援と、オープンソースコミュニティの助けによって実現しました。

特に：
- Anthropic Claude - 開発サポート
- Flask - Webフレームワーク
- すべてのテスターとフィードバック提供者

---

⭐ **役に立ったら、GitHubでスターをお願いします！** ⭐

---

**Let's code together! 🌲✨**