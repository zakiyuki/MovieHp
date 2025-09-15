#映像系ポートフォリオ用ホームページ

自身の映像作品をまとめたポートフォリオホームページです。

## 機能

- 映像作品(Youtubeの映像)の内包
- メール送信による問い合わせフォームの実装

## 必要な環境

- Python
- pip（Pythonパッケージマネージャー）

## インストール

1. リポジトリをクローンまたはダウンロード
```bash
git clone <repository-url>
cd Flask
```

2. 仮想環境を作成（推奨）
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

## 使用方法

1. アプリケーションを起動
```bash
python app.py
```

2. ブラウザで `http://localhost:5000` にアクセス

3. メールの送信
   - 必要事項を記入後送信ボタンをクリック
   - 必要事項の記入がないと送信はできません

## ファイル構造

```
MovieHp/
├── app.py                # メインアプリケーション
├── README.md             # このファイル
├── static/
│   ├── css/
│   │   ├── sanitize.css
│   │   └── style.css     # スタイルシート
│   ├── image/            # ホームページで使用する画像
│   ├── js/
│   │   └── app.js        # スタイルシート 
│   └── videos/           # ホームページで使用する動画
└── templates/
    ├── index.html        # ホームページ
    └── send.html         # メール送信時の確認ページ
```


## ライセンス

このプロジェクトはMITライセンスの下で公開されています。





