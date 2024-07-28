# fixme1.py:General Skills

Fix the syntax error in this Python script to print the flag.\
[Download Python script]()

# Solution

とりあえず実行してエラー確認。
```
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```
インデントエラーであることが分かった。printの前に謎のインデントがあるので、そこを削除してもう一度実行すると、フラグが得られた。

`picoCTF{1nd3nt1ty_cr1515_09ee727a}`
