# fixme1.py:General Skills

Fix the syntax error in this Python script to print the flag.  
[Download Python script](fixme1.py)

# Solution

とりあえず実行してエラー確認。
```
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```
インデントエラーであることが分かった。printの前に謎のインデントがあるので、そこを削除してもう一度実行すると、flagが得られた。

`picoCTF{1nd3nt1ty_cr1515_09ee727a}`
