# Big Zip:General Skills

Unzip this archive and find the flag.
[Download zip file](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Big%20Zip/big-zip-files.zip)

# Solution

big-zip-files.zipの中をざっと見てみると大量のテキストファイルがある。おそらく、このどれかにflagが書かれているはず。\
まず、`unzip`して`grep`で「pico」の文字列のあるファイル名を特定する。
```
$ grep -rl pico ./big-zip-files/*
./big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
```
whzxrpivpqld.txtに記述されている文字列を取得すると、
```
$ strings whzxrpivpqld.txt
information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```
flagが得られた。

`picoCTF{gr3p_15_m4g1c_ef8790dc}`
