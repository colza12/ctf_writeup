# Wave a flag:General Skills

Can you invoke help flags for a tool or binary? [This program]() has extraordinarily helpful information...

# Solution

添付ファイルに拡張子がついていないので、とりあえずテキストエディタで開くと、ELFファイルであることが分かる。と、同時にflagも得られた。

`picoCTF{b1scu1ts_4nd_gr4vy_d6969390}`

一応、`chmod +x warm`で実行権限を付与して実行してみた。
```
$ ./warm 
Hello user! Pass me a -h to learn what I can do!
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_d6969390}
```

