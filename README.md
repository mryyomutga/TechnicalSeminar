# TechnicalSeminar
専門ゼミの活動記録

## Day1 2017/10/19 (Thu)
Pythonを触ってみる
### 活動内容
- python3のprint()を使えるようにする
- importを使って三角関数を使えるようにする
- リスト・タプルの操作
- 関数を定義し，使用してみる
- 変数の型を調べる
- range()を使ったリストの作成
- for文・if文とインデント
- time.sleep()を使って遅延を発生させてみる

### 自由記述
Python2よりもPython3でやってほしいと感じた

## Day2 2017/10/26(Thu)
turtul，pygameのインストールと今後の方針
### 活動内容
- 教科書の受け取り
- turtul,pygameモジュールのインストール
- 辞書型の操作
- リスト内包表記
- Turtle Graphicsを触ってみる
- pygameを使ったプログラムを動かしてみる
- inputを使ったユーザー入力プログラムの作成
- formatの復習

### 自由記述
IPythonの使い方がようやく理解できた

Turtle Graphicsは子供向けらしい

pygameは簡単にゲーム開発できるらしいが、難しい

教科書が届いたため、本格的に勉強を開始する

## Day3 2017/11/09(Thu)
学生の作成したプログラムの発表、自習、仮テーマについて
### 活動内容
- プログラムの発表(買い物かご)
- リストの操作(chapter3-1)

### 自由記述
あまり進まなかった

windowsで暗号化ライブラリのpycryptoをインストールする際にpipではインストールできなかったため以下の手順でインストールした

1. 既存のpythonをアンインストール
2. Anacondaをインストール

 	デフォルトでは`conda env list`を実行すると環境が`root`しかないはず

3. PowerShellではactivateができない?ためコマンドプロンプトから`activate`コマンドを実行
4. `root`環境に入ったら`conda install pycrypto`でpycryptoをインストール
5. `deactivate`コマンドで環境から抜けてもpycryptoのインポートでエラーが発生しなくなる

Anacondaインストール直後はpipが入っていないため、pipを使いたい場合はその環境下で`conda install pip`でpipをインストール

仮想環境の確認は`conda env list`または`conda info -e`

仮想環境の作成、削除は`conda create -n 環境名`、`conda remove -n 環境名 --all`
