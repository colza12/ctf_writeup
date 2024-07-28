# PW Crack 2:General Skills

Can you crack the password to get the flag? Download the password checker [here]() and you'll need the encrypted [flag]() in the same directory too.

# Solution

PW Crack 1とほぼ一緒と推察できる。なので、先にlevel2.pyのコードを確認。
```python
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
user_pwがchr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)であればフラグが得られるらしい。
16進数を文字列に直すと、`de76`であるから、level2.pyを実行してパスワードde76を入力する。

フラグが得られた。

`picoCTF{tr45h_51ng1ng_489dea9a}`
