# caas:Web Exploitation

Now presenting [cowsay as a service](https://caas.mars.picoctf.net/)

attachment
* [index.js]()

# Solution

とりあえず、記載のリンクに飛んでみると、`Make a request to the following URL to cowsay your message: https://caas.mars.picoctf.net/cowsay/{message}`
と書いてあった。そのままURLにアクセスすると以下のメッセージ付き牛が出てきた。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3638553/f211030a-02fc-3995-1665-bc31314c1bb0.png)

`{message}`の部分に入力した文字が牛からのメッセージとして出力されるようだ。
index.jsを見てみる。`const { exec } = require('child_process');`でシェルコマンドを実行できるようにし、`/usr/games/cowsay ${req.params.message}`で、入力した{message}を引数としてシェルコマンドを実行しているようだ。;で区切ることによって任意のコマンドを実行させられる。
/usr/games/cowsayとPATHが指定されているため、`;ls`でディレクトリの内容を出力させようとしたが、;の前に何らかの文字を入れる必要があったため、`a;ls`とした。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3638553/66fc9084-e8da-bcec-1e21-b40c0b81ec45.png)

ディレクトリの中にfalg.txtを発見した。「falg」であって、「flag」ではないことに注意が必要。つい見間違って時間が溶けたので、こういうときはコピペした方が良い。\
で、実行コマンドのことであるが、`a;strings%20falg.txt`で可読文字を抜き出そうとしたが、stringsが使えなかったため、ファイル内容を表示させるcatを使い、`a;cat%20falg.txt`とした。URLで空白文字を扱うために、空白をURLエンコードした%20を用いる(普通に空白文字でも良かったらしい)。実行するとフラグが出てきた。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3638553/7ddf1465-d463-5af8-b11f-c68c4f2430cf.png)

フラグが得られた。

`picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`

ちなみに、これはOSコマンドインジェクションというらしい。

