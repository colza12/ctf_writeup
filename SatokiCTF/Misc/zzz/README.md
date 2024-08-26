# zzz:Misc

朝起きて 歯を磨いて あっという間 午後10時

`sshpass -p ctf ssh ctf@160.251.183.149 -p 22222`
Attachment\
[zzz.zip](https://github.com/colza12/ctf_writeup/new/main/SatokiCTF/Misc/zzz/zzz.zip)

Difficulty Level : warmup\
Point : 100

Hint\
SFTPやSCP, ポートフォワーディングといったSSHならではの機能は、解くためには必要ありません。
なにかシンプルな方法で無理やり `sleep infinity` だけを終了させられないでしょうか。

# Solution

なんかがちゃがちゃしてたらフラグが出てきた。\
SIGQUITをすることによってsleep infinityだけを終了させられるらしい。\
ちなみにがちゃがちゃしたというのは`Ctrl+\`。

`flag{eternal_spring_dream_27ff12ce}`
