## Stravaの全データをPython,foliumを使ってHTMLで表示出力
このプロジェクトでは、Stravaからエクスポートしたデータを取得し、Pythonのfoliumパッケージを使用して地図上に表示し、HTMLとして保存します。

### 前提条件
1. Stravaにアカウントを持っていること。
1. Stravaからデータを一括エクスポートし、解凍しておくこと。
   1.[データのエクスポートと一括エクスポート – Strava サポート](https://support.strava.com/hc/ja/articles/216918437-%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%88%E3%81%A8%E4%B8%80%E6%8B%AC%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%88)
2. Python 3.10がインストールされていること。（他は試していない。）

### 手順
1. ダウンロード
```
git clone git@github.com:kotarouhayashi/strava_map.git
cd strava_map
```

2. ストラバからダウンロードしてきたデータの中のactivitiesディレクトリをstrava_map/data/以下に配置
3. 仮想環境を構築
```
poetry add $( cat requirements.txt )
poetry update
poetry install
```
4. 仮想環境にてmakehtml.pyを実行
```
poetry run python makehtml.py
```
### アウトプット
↓のようなHTMLファイルが出来上がるので自分のブログ等に用いることが可能。
<img width="364" alt="strava" src="https://user-images.githubusercontent.com/130144468/235284301-e600fa9f-8bd1-428f-b748-5ba0d5a0e814.png">
