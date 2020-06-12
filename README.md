# TwiWikiLinker
2020/06/11~ Aso Taisei
***
## 概要
Wikipediaから単語をキーとするハッシュを形成する
それを用いて、TwitterデータとWikipediaデータを紐づける

## 要件
- python3系
- pyyaml
- matplotlib (visualize.pyで使用)

## 準備
- TwiCommon で出力された tweet.txt と tweet-part.txt を ./data/ に置く
- WikiCommon で出力された cleaned.txt と cleaned-part.txt と cleaned.yml を ./data/ に置く
- カレントディレクトリを ./TwiWikiLinker に移動

## 手順
1. Wikipediaから単語をキーとするハッシュを形成する
    ```
    $ python hash.py
    ```
    ./data/ に hash.yml が出力される

2. TwitterデータとWikipediaデータを紐づける
    ```
    $ python link.py
    ```
    ./data/ に link.txt が出力される

3. Twitterデータと紐づいたWikipediaデータの数のヒストグラムを画像として保存する
    ```
    $ python visualize.py
    ```
    ./data/ に visualize.png が出力される

4. 紐づけるWikipediaデータの最小数を増加させることで、必要なくなるWikipediaデータの数のヒストグラムを画像として保存する
    ```
    $ python visualize2.py
    ```
    ./data/ に visualize2.png が出力される

5. 使用しないTwitter/Wikipediaデータをフィルタリングする
    ```
    $ python filter.py
    ```
    ./data/ に filtered-tweet.txt, filtered-tweet-part.txt, filtered-wiki.txt, filtered-wiki-part, filtered-link.txt が出力される

## 備考
- 各種設定の変更は ./config.yml を参照してください
- 各ファイルが必要なくなった場合は ./data/ にあるファイルを削除するだけで大丈夫です
