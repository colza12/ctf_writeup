# login:Web Exploitation

My dog-sitter's brother made this website but I can't get in; can you help?\
[login.mars.picoctf.net](https://login.mars.picoctf.net/)

# Solution

とりあえず、記載のリンクに飛ぶと、usernameとpasswardを入力するところがあるので、adminでSQLインジェクションを試みる。
パスワードが違うというアラートが出ること以外は何起きないので、Burp Suiteでresponseを確認する。
と、Base64で暗号化されたusernameとpasswardが出てきた。
usernameは`YWRtaW4`でadmin、passwardは`Gljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ`で、これがフラグだった。

`picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`

ちなみに、usernameがadminでない場合は、usernameが違うというアラートが出るようだ。奇跡的にusernameが合っていたために、usernameエラーが出なかったらしい。usernameとpasswardはデコードしたもののみログインすることができた。ログインすると、ダイアログボックスでフラグが表示された。
