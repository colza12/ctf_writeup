# caesar:Cryptography

Decrypt this [message](https://github.com/colza12/ctf_writeup/new/main/picoCTF%202019/ciphertext).

# Solution

ciphertextをテキストエディタで開くと
```
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
```
括弧内の文字列がシーザー暗号でエンコードされているので、cyberchefで文字をずらしていくと、４文字目でうまくいった。

`picoCTF{crossingtherubiconvfhsjkou}`
