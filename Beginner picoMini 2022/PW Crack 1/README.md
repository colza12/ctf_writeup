# PW Crack 1:General Skills

Can you crack the password to get the flag? Download the password checker [here](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/PW%20Crack%201/level1.py) and you'll need the encrypted [flag](https://github.com/colza12/ctf_writeup/blob/main/Beginner%20picoMini%202022/PW%20Crack%201/level1.flag.txt.enc) in the same directory too.

# Solution

とりあえず、level1.pyを実行してみると、パスワードの入力を求められた。
level1.pyのコードを確認すると、
```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "1e1a"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
とある。user_pwが1e1aであればフラグが得られるらしいので、もう一度level1.pyを実行してパスワード1e1aを入力する。

フラグが得られた。

`picoCTF{545h_r1ng1ng_fa343060}`

