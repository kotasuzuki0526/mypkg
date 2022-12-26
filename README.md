# mypkg
* このリポジトリはROS2のパッケージとなっています。
* このパッケージには、talkerというノードと、listenerというノードがあります。

# talkerとlistener
[![test](https://github.com/kotasuzuki0526/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kotasuzuki0526/mypkg/actions/workflows/test.yml)

## talker
* このノードはパブリッシャを持ち、数字をカウントして、countupというトピックを通じて送信します。
* メッセージの型は16ビット符号つき整数です。

## listener
* このノードはサブスクライバを持ち、countupからメッセージをもらって表示します。
* メッセージの型は16ビット符号つき整数です。

# 実行方法と結果

## 実行方法
* まず、端末を二つ立ち上げます。	
* 一つ目の端末で以下を実行します。
```
$ ros2 run mypkg talker
```
* 二つ目の端末で以下を実行します。
```
$ ros2 run mypkg listener
```

## 結果
* 一つ目（talkerを起動した方）の端末では何も表示されません。
* 二つ目（listenerを起動した方）の端末では以下のように表示されます。
```
[INFO] [1672024654.529754200] [listener]: Listen: 27
[INFO] [1672024655.014093400] [listener]: Listen: 28
[INFO] [1672024655.514029300] [listener]: Listen: 29 
・・・
```
# テストに関して
* テストには以下のコンテナを、GitHub Actionsでダウンロードして使用しています。
	* https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

# 動作確認済み環境
* Ubuntu 20.04
* Python 3.8.10

# ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
	* [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Kota Suzuki
                          
