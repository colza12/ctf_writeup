# PW Crack 5:General Skills

Can you crack the password to get the flag? Download the password checker [here](level5.py) and you'll need the encrypted [flag](level5.flag.txt.enc) and the [hash](level5.hash.bin) in the same directory too. Here's a [dictionary](dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

# Solution

dictionary.txtを見てみると、パスワード候補が各行4桁ずつ書かれていた。PW Crack 4とほぼ同じであるが、dictionary.txtを読み込んでパスワード候補を改行区切りでリストに格納する必要がある。\
以下、実行コード。
```python solve.py
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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()
pw_candidate = open('dictionary.txt', 'r').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check(user_pw):
#    user_pw = input("Please enter correct password for flag: ")
#    user_pw_hash = hash_pw(user_pw)
    
#    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
        print("That password is incorrect")

pw_list = pw_candidate.split()
for i in pw_list:
    if hash_pw(i) == correct_pw_hash:
        a = i


level_5_pw_check(a)
```
flagが得られた。

`picoCTF{h45h_sl1ng1ng_40f26f81}`
