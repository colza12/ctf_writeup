# Weak PRNG:crypto

Do you understand the traits of that famous PRNG?\
`nc 35.185.131.17 19937`

attachment\
[firectf_ierae-ctf-2024-prod-eh2j3_distfiles_weak-prng.tar.gz]()

Difficulty Level : easy\
Point : 185\
Solved : 54

# Solution
とりあえず、`nc 35.185.131.17 19937`を実行する。
```
$ nc 35.185.131.17 19937
Welcome!
Recover the initial output and input them to get the flag.
--------------------
Menu
1. Get next 16 random data
2. Submit your answer
3. Quit
Enter your choice (1-3)
> 1
Here are your random data:
1659148817
3901558449
4094952221
1371553642
3172843904
965584041
257135497
3490907323
4205275486
3129377230
514015747
4066881094
2453943499
1676063874
937528519
561917574
```
16個の乱数が出力されるらしい。
配布されたchallenge.pyを確認する。
```python
#!/usr/bin/env python

from os import getenv
import random
import secrets

FLAG = getenv("FLAG", "TEST{TEST_FLAG}")


def main():
    # Python uses the Mersenne Twister (MT19937) as the core generator.
    # Setup Random Number Generator
    rng = random.Random()
    rng.seed(secrets.randbits(32))

    secret = rng.getrandbits(32)

    print("Welcome!")
    print("Recover the initial output and input them to get the flag.")

    while True:
        print("--------------------")
        print("Menu")
        print("1. Get next 16 random data")
        print("2. Submit your answer")
        print("3. Quit")
        print("Enter your choice (1-3)")
        choice = input("> ").strip()

        if choice == "1":
            print("Here are your random data:")
            for _ in range(16):
                print(rng.getrandbits(32))
        elif choice == "2":
            print("Enter the secret decimal number")
            try:
                num = int(input("> ").strip())

                if num == secret:
                    print("Correct! Here is your flag:")
                    print(FLAG)
                else:
                    print("Incorrect number. Bye!")
                break
            except (ValueError, EOFError):
                print("Invalid input. Exiting.")
                break
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            continue


if __name__ == "__main__":
    main()
```
コードから分かる重要な点は以下の3点。
* 乱数の生成にはMersenne Twister (MT19937)が使われている。
* seedを使って32bitの固定の乱数列を生成し、そこからランダムに1つの数値を取り出してsecretに格納している。
* 出力される16個の乱数は、seedで固定した乱数列からランダムの数値を取り出したもの。

Mersenne Twister (MT19937)は624個の周期で乱数を生成している。\
seedで乱数列が固定されているため、16個の乱数を624個出力させて、そこから逆算することでsecretの数値を求めることができる。secretは624個の乱数の一番最後にあたる。
secretの数値を求める際、[Mersenne Twister (MT19937) で未来と過去の乱数列を予測してみる【Python】](https://zenn.dev/hk_ilohas/articles/mersenne-twister-previous-state)を参考に(script kiddy)した。
以下、実行コード。(乱数取得とsecret推定は別のコード)
```python:solveprng.py
import re
from pwn import *

p = remote("35.185.131.17", 19937)

payload = b"1"

listhint=[]
for i in range(2):
    response = str(p.recvline())
    listhint.append(response)
for i in range(39):
    p.sendline(payload)
    for j in range(23):
        response = str(p.recvline())
        listhint.append(response)

substring = "--"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "random"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Submit"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Quit"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Enter"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Menu"
listhint = list(filter(lambda item: substring not in item, listhint))
listhint = listhint[2:]

for i in range(len(listhint)):
    print(listhint[i])

pyload = b"2"
p.sendline(payload)
p.interactive()
```
```python:solveprng1.py
import random

N = 624
xs1 = ["ここに取得した乱数を格納"]

def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x


def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y


def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y

mt_state = [untemper(x) for x in xs1]
random.setstate((3, tuple(mt_state + [N]), None))

def get_prev_state(state):
    for i in range(623, -1, -1):
        result = 0
        tmp = state[i]
        tmp ^= state[(i + 397) % 624]
        if ((tmp & 0x80000000) == 0x80000000):
            tmp ^= 0x9908b0df
        result = (tmp << 1) & 0x80000000
        tmp = state[(i - 1 + 624) % 624]
        tmp ^= state[(i + 396) % 624]
        if ((tmp & 0x80000000) == 0x80000000):
            tmp ^= 0x9908b0df
            result |= 1
        result |= (tmp << 1) & 0x7fffffff
        state[i] = result
    return state

mt_state = [untemper(x) for x in xs1]
prev_mt_state = get_prev_state(mt_state)
random.setstate((3, tuple(prev_mt_state + [0]), None))

predicted = [random.getrandbits(32) for _ in range(N)]
print(predicted[623])
```
実行してみる。
```
$ python3 solveprng.py
[+] Opening connection to 35.185.131.17 on port 19937: Done
b'2824236561\n'
b'2472915541\n'
b'1813014051\n'
b'2537986373\n'

$ python test.py  #別ウィンドウで実行
4291639202

#元のウインドウに戻って
> 2
Enter the secret decimal number
> 4291639202
Correct! Here is your flag:
IERAE{WhY_4r3_n'7_Y0u_u51n6_4_CSPRNG_3v3n_1n_2024}
```
flagが得られた。

`IERAE{WhY_4r3_n'7_Y0u_u51n6_4_CSPRNG_3v3n_1n_2024}`
