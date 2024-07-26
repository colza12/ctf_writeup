# Python Wrangling:General Skills

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Python%20Wrangling/ende.py) using [this password](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Python%20Wrangling/pw.txt) to get [the flag](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Python%20Wrangling/flag.txt.en)?

# Solution
問題文にあるように、とりあえず実行してみる。
```
$ python ende.py -d flag.txt.en
Please enter the password:6008014f6008014f6008014f6008014f
picoCTF{4p0110_1n_7h3_h0us3_6008014f}
```
ende.pyに記述されているhelp_msgをヒントに実行した。
フラグが得られた。

`picoCTF{4p0110_1n_7h3_h0us3_6008014f}`
