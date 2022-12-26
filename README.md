# mypkg
* このリポジトリはROS2のパッケージとなっています。
* このパッケージには、talkerというノードと、listenerというノードがあります。

##talkerとlistener
[![test](https://github.com/kotasuzuki0526/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kotasuzuki0526/mypkg/actions/workflows/test.yml)
# talker
* このノードはパブリッシャを持ち、数字をカウントして、countupというトピックを通じて送信します。
* メッセージの型は16ビット符号つき整数です。

# listener
* このノードはサブスクライバを持ち、countupからメッセージをもらって表示します。
* メッセージの型は16ビット符号つき整数です。
