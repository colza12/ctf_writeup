# fixme2.py:General Skills

Fix the syntax error in the Python script to print the flag.\
[Download Python script](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/fixme2.py/fixme2.py)

# Solution

とりあえず実行してエラー確認。
```
if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```
記述形式が違うらしいので`=`を`==`にしてもう一度実行すると、フラグが得られた。

`picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}`
