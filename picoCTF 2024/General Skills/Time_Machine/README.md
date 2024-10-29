# Time Machine : General Skills

What was I last working on? I remember writing a note to help me remember...  
You can download the challenge files here:
* [challenge.zip](challenge.zip)

Author : Jeffery John

# Solution

添付ファイルを`unzip`する。  
drop-inディレクトリ配下にファイルが展開されるので、`cd`でディレクトリを移動すると、message.txtが見つかる。`strings`で可読文字列を出力すると、以下のメッセージが出力された。
```
This is what I was working on, but I'd need to look at my commit history to know why...
```
commit historyを見ろということらしい。drop-in配下には`.git/COMMIT_EDITMSG`があることを`find`または`unzip`した結果から探すことができる。このファイルは名前からしてcommit messageが書き込まれていると推測できる。`strings`で`COMMIT_EDITMSG`の可読文字列を出力する。
```
$ strings .git/COMMIT_EDITMSG 
picoCTF{t1m3m@ch1n3_8defe16a}
```
flagが得られた。

`picoCTF{t1m3m@ch1n3_8defe16a}`
