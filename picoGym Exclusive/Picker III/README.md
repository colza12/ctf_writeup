# Picker III:Reverse Engineering

Can you figure out how this program works to get the flag?\
Connect to the program with netcat: `$ nc saturn.picoctf.net 53983`\
The program's source code can be downloaded [here]().

# Solution

とりあえず、`nc saturn.picoctf.net 53983`を実行してみる。
```
$ nc saturn.picoctf.net 53983
==> help

This program fixes vulnerabilities in its predecessor by limiting what
functions can be called to a table of predefined functions. This still puts
the user in charge, but prevents them from calling undesirable subroutines.

* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
```
数字を入力するとtableの数字に対応する関数が実行できるらしい。
picker-III.pyを見てみる。
```python
def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value)
    else:
      print('Illegal value')
  else:
    print('Illegal variable name')

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
write_variable関数を見つけた。1つめの入力でtable内の変えたい関数名を入力し、2つめの入力で実行させたい関数名を入力すると`'global '+var_name+'; '+var_name+' = '+value`の部分で、関数名は元のままで、変えたい関数が実行したい関数に置き換わるようになっているようだ。
変えても問題のなさそうなgetRandomNumberをwinに置き換えて、実行してみる。
```
$ nc saturn.picoctf.net 53983
==> 3
Please enter variable name to write: getRandomNumber
Please enter new value of variable: win 
==> 4
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d
```
なんかHexが出てきたのでascii変換するとフラグが得られた。

`picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}`

