# Python Wrangling:General Skills

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script]() using [this password] to get [the flag]?

# Solution
問題文にあるように、とりあえず実行してみる。
```
> python ende.py -d flag.txt.en
Please enter the password:6008014f6008014f6008014f6008014f
picoCTF{4p0110_1n_7h3_h0us3_6008014f}
```
ende.pyに記述されているhelp_msgをヒントに実行した。
フラグが得られた。

`picoCTF{4p0110_1n_7h3_h0us3_6008014f}`
