# hash:Misc

フラグが簡単に特定できないようハッシュ化したけど、分かるかな？フラグの候補はファイルを確認してください。

(フラグのハッシュ値)
3390a5081ea4d44e3173eaf3e9695d9216d60cfcb617027355c95b3b7275e8e3
ーーーーーーーーーーーーーーーーーーーーーーーーーーー
I've hashed the flag so it can't be easily identified, but you get the idea? Check the file for flag candidates.

(hash value of flag)
3390a5081ea4d44e3173eaf3e9695d9216d60cfcb617027355c95b3b7275e8e3

attachment\
[flag-options.csv](https://github.com/colza12/private_ctf_writeup/blob/main/Japan-UkraineCTF/Misc/hash/flag-options.csv)

Point : 50

# Solution
添付ファイルを見てみると、100個のフラグ候補が存在する。\
問題文に掲載されているハッシュ値は、おそらくSHA-256であると推測できる。\
フラグ候補を順番にSHA256でハッシュ化し、`3390a5081ea4d44e3173eaf3e9695d9216d60cfcb617027355c95b3b7275e8e3`に一致するものを探す。\
以下、実行コード。
```python
import hashlib

with open("flag-options.csv", 'r') as f:
    flag_list = [line.strip() for line in f.readlines()]

for flag in flag_list:
    candidate = hashlib.sha256(flag.encode()).hexdigest()
    if candidate == "3390a5081ea4d44e3173eaf3e9695d9216d60cfcb617027355c95b3b7275e8e3":
        print(flag)
```
実行する。
```
$ python solve_hash.py
FLAG{Matsuyama Castle_Ehime}
```

flagが得られた。

`FLAG{Matsuyama Castle_Ehime}`
