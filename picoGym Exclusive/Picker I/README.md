# Picker I:Reverse Engineering

This service can provide you with a random number, but can it do anything else?\
Connect to the program with netcat: `$ nc saturn.picoctf.net 51123`
The program's source code can be downloaded [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Picker%20I/picker-I.py).

# Solution

とりあえず`nc saturn.picoctf.net 51123`を実行してみる。
```
$ nc saturn.picoctf.net 51123
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber
4
```
指示通りに入力したら4が出てきた。
ソースコードを見てみる。
```python
def getRandomNumber():
  print(4)
```
という部分を見つけた。ユーザ定義関数を入力すると、そのまま実行されるらしい。フラグが出てきそうな関数を探すと、
```python
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```
という部分を見つけた。もう一度実行して`win()`と入力する。
```
$ nc saturn.picoctf.net 51123
Try entering "getRandomNumber" without the double quotes...
==> win()
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d
```
hexが出てきたのでutf-8に変換。\
フラグが得られた。

`picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`

