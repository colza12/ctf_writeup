# PW Crack 3:General Skills

Can you crack the password to get the flag? Download the password checker [here](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/PW%20Crack%203/level3.py) and you'll need the encrypted [flag](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/PW%20Crack%203/level3.flag.txt.enc) and the [hash](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/PW%20Crack%203/level3.hash.bin) in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# Solution

level3.pyの中身を見ると、入力したパスワードをMD5ハッシュ値に直して比較してることが分かる。
```python
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
```
パスワードの候補は７個しかないので、順番に試しても時間はかからない。パスワードは`87ab`であった。\
level3.pyを実行して、パスワード87abを入力するとパスワードが得られた。

`picoCTF{m45h_fl1ng1ng_cd6ed2eb}`

level3.pyの中身を少しいじってフラグを取得する方法もある。(パスワード候補が多い場合は効率的)
以下、実行コード。
```python
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check(user_pw):
#    user_pw = input("Please enter correct password for flag: ")
#    user_pw_hash = hash_pw(user_pw)
    
#    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
        print("That password is incorrect")

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

for i  in  pos_pw_list:
    if hash_pw(i) == correct_pw_hash:
        a = i

level_3_pw_check(a)
```

