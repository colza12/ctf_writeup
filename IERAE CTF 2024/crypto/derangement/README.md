# derangement:crypto

I've made a secret magic string, perfectly encrypted!\
`nc 35.221.153.165 55555`

attachment\
[firectf_ierae-ctf-2024-prod-eh2j3_distfiles_derangement.tar.gz](https://github.com/colza12/ctf_writeup/blob/main/IERAE%20CTF%202024/crypto/derangement/firectf_ierae-ctf-2024-prod-eh2j3_distfiles_derangement.tar.gz)

Difficulty Level : warmup\
Point : 149\
Solved : 106 

# Solution
とりあえず、`nc 35.221.153.165 55555`を実行してみる。
```
$ nc 35.221.153.165 55555

/********************************************************\
|                                                        |
|   Abracadabra, let's perfectly rearrange everything!   |
|                                                        |
\********************************************************/

type 1 to show hint
type 2 to submit the magic word
> 1
hint: D~9SG3!W[^rc{Jo
```
配布されたchallenge.pyを確認する。
```python
#!/usr/bin/env python

from os import getenv
import random
import string
import sys

FLAG = getenv("FLAG", "TEST{TEST_FLAG}")

LENGTH = 15
CHAR_SET = string.ascii_letters + string.digits + string.punctuation

def generate_magic_word(length=LENGTH, char_set=CHAR_SET):
    return ''.join(random.sample(char_set, length))

def is_derangement(perm, original):
    return all(p != o for p, o in zip(perm, original))

def output_derangement(magic_word):
    while True:
        deranged = ''.join(random.sample(magic_word, len(magic_word)))
        if is_derangement(deranged, magic_word):
            print('hint:', deranged)
            break

def guess_random(magic_word, flag):
    print('Oops, I spilled the beans! What is the magic word?')
    if input('> ') == magic_word:
        print('Congrats!\n', flag)
        return True
    print('Nope')
    return False

def main():
    magic_word = generate_magic_word()
    banner = """
/********************************************************\\
|                                                        |
|   Abracadabra, let's perfectly rearrange everything!   |
|                                                        |
\\********************************************************/
"""
    print(banner)
    connection_count = 0

    while connection_count < 300:
        print('type 1 to show hint')
        print('type 2 to submit the magic word')
        try:
            connection_count += 1
            user_input = int(input('> '))

            if user_input == 1:
                output_derangement(magic_word)
            elif user_input == 2:
                if guess_random(magic_word, FLAG):
                    break
                sys.exit()
            else:
                print('bye!')
                sys.exit()
        except:
            sys.exit(-1)
    
    print('Connection limit reached. Exiting...')

if __name__ == "__main__":
    main()
```
接続は300秒で切れるようになっている。また、hintで出力される謎文字列は、15文字のmagic wordの文字列をランダムで並べ替えた後、magic wordと1文字ずつ比較して一致しないものとなっていることが分かる。\
出力される文字列を取得して、1度でもn番目に出力された文字は、そのn番目の文字候補から削除していく方式で1度も出力されていない文字を特定し、残った文字を並べて入力することによって、フラグを出力させる。\
以下、実行コード。(1,2文字目の文字候補がうまく出力できなかったため、hint取得とmagic word推定は別のコードにした)
```python:solve2.py
import re
from pwn import *

p = remote("35.221.153.165", 55555)

payload = b"1"

listkey=[]
listhint=[]

for _ in range(9):
    response = str(p.recvline())
    listhint.append(response)

for i in range(100):
    p.sendline(payload)
    for _ in range(3):
        response = str(p.recvline())
        response = response.replace("> hint: ","")
        listhint.append(response)

substring = "type"
listhint = list(filter(lambda item: substring not in item, listhint))
listhint = listhint[9:]

for i in range(15):
    listkey.append(listhint[0])

for i in range(len(listhint)):
    print(listhint[i])

for i in range(len(listhint)):
    for j in range(15):
        listkey[j] = listkey[j].replace(listhint[i][j]," ")

for i in range(len(listkey)):
    print(listkey[i])

pyload = b"2"
p.sendline(payload)
p.interactive()
```
```python:solve.py
import re

list=[]
for i in range(15):
    list.append(".yrq85?RFZ\\octv")

listhint=["ここに取得したhintの文字列を格納"]
for i in range(len(listhint)):
    for j in range(15):
        list[j] = list[j].replace(listhint[i][j]," ")

for i in range(15):
    print(list[i])
```
実行する。
```
$ python3 solve2.py
[+] Opening connection to 35.221.153.165 on port 55555: Done
b'.yrq85?RFZ\\octv\n'
b'.yrq85?RFZ\\octv\n'
b'rtc8vo5R?FyZ.q\\\n'
b'v.\\FoZt8cRry?5q\n'
b'.F8c5tr\\ZyRvq?o\n'

$ python3 solve.py      #別ウインドウで実行
           o
         Z
     5
              v
  r
      ?
.
 y
          \
             t
   q
            c
    8
       R
        F

#元のウィンドウに戻って
type 1 to show hint
type 2 to submit the magic word
> 2
Oops, I spilled the beans! What is the magic word?
> oZ5vr?.y\tqc8RF
Congrats!
IERAE{th3r35_n0_5uch_th!ng_45_p3rf3ct_3ncrypt!0n}
```
flagが得られた。

`IERAE{th3r35_n0_5uch_th!ng_45_p3rf3ct_3ncrypt!0n}`
