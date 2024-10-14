# XtraORdinary:Cryptography

Check out my new, never-before-seen method of encryption! I totally invented it myself. I added so many for loops that I don't even know what it does. It's extraordinarily secure!

attachment
* [output.txt](output.txt)
* [encrypt.py](encrypt.py)

# Solution

タイトルがXtraORdinaryでXORを強調しているので、XORで復号するのではないか。XORで暗号化されたものは同じ鍵を使ってもう一度XORすると元に戻る。\
実際にencrypt.pyを見てみるとxorで暗号化されていた。
```python
for random_str in random_strs:
    for i in range(randint(0, pow(2, 8))):
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str)
```
xorを繰り返している部分があるが、暗号化と復号を繰り返しているだけなので、見た目より単純である。\
暗号化の鍵も以下のようになっているが、everがいくつもあるだけで結果は変わらないので、実質5個だけである。よって、xorの試行回数も2^5=32回である。
```python
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]
```
暗号化の手順は、flagをkeyでxorしたものを、random_strsで繰り返しxorしているらしい。keyの正体は不明であるが、flagの最初の文字列が「picoCTF{」であることは確実なので、keyの部分に`picoCTF{`を当てることで、暗号化に使われたkeyの正体を探る。\
以下、実行コード。
```python
from Crypto.Util.number import long_to_bytes, bytes_to_long

ctxt=long_to_bytes(0x57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637)
key=b"picoCTF{"
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

for _ in range(2):
  ctxt = encrypt(ctxt, random_strs[0])
  for _ in range(2):
    ctxt = encrypt(ctxt, random_strs[1])
    for _ in range(2):
      ctxt = encrypt(ctxt, random_strs[2])
      for _ in range(2):
        ctxt = encrypt(ctxt, random_strs[3])
        for _ in range(2):
          ctxt = encrypt(ctxt, random_strs[4])
          a = encrypt(ctxt, key)
          print(a)
```

実行すると、意味のある文字列でかつ同じ文字列が繰り返されていそうなのを探すと、`Africa!`という文字列を発見。これがkeyの正体であろう。上記実行コードの`key=b"picoCTF{"`を`key=b"Africa!"`に変更して再度実行する。  
flagが得られた。

`picoCTF{w41t_s0_1_d1dnt_1nv3nt_x0r???}`

