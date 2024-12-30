# 最悪エディター1 : Misc

[プログラマに寄せすぎた粗品「最悪やEmacsや」](https://youtu.be/LguxePqBcCY)

うわ、最悪やEmacsや！

終了できたらフラグあげるで〜

sshしてサーバーに接続してください。 （参考までにソースコードを添付しましたが、問題を解くためには必ずしも読む必要はありません。）  
`ssh ctf@35.189.153.223 -p 8003 (パスワード ctf) `

Attachment  
[saiaku_editor_1.zip](saiaku_editor_1.zip)  

Difficulty Level : easy  
Point : 356  
Solves : 79  

# Solution

Emacsの終了ショートカットは`Ctrl+X+C`である。記載のサーバにssh接続して終了ショートカットを入力する。
```
$ ssh ctf@35.189.153.223 -p 8003
ctf@35.189.153.223's password:
asusn{Em4c5_n0_k070_D4r364_Suk1n4n?}Connection to 35.189.153.223 closed.
```
flagが得られた。

`asusn{Em4c5_n0_k070_D4r364_Suk1n4n?}`
