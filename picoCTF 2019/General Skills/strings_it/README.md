# strings it : General Skills

Can you find the flag in [file](strings) without running it?

Author : Sanjay C, Danny Tunitis

# Solution

タイトルからも分かる通り、stringsコマンドで可読文字列を出力させる。と大量の文字列が流れていった。
おそらく、stringsコマンドでフラグが出力されるようになっていて、探せということだろう。
grepを使う。
```
$ strings strings | grep pico
picoCTF{5tRIng5_1T_d66c7bb7}
```

flagが得られた。

`picoCTF{5tRIng5_1T_d66c7bb7}`