# HellCouple : Crypto

脆弱なカップル！

Attachment  
[hellcouple.tar.gz](hellcouple.tar.gz)  

Difficulty Level : Very Hard  
Tags : Discrete Logarithm  
Author : chocorusk

# Solution

**問題概要**  

1536-bit MODP Group (RFC3526)を用いたDiffie-Hellman鍵共有が行われており、公開鍵`alice_public`、`bob_public`、Aliceの秘密鍵`alice_private`の下位1500bit、AES-CTRで暗号化されたflagが与えられる。  
Diffie-Hellman共通鍵でAES復号することでflagが得られる。

**観察**  

与えられる情報
* 素数 p : 1536-bit MODP prime
* 生成元 g = 2 
* Alice公開鍵 $A = g^a \bmod p$
* Bob公開鍵 $B = g^b \bmod p$
* Alice秘密鍵の下位1500bit $a_0 = a \bmod 2^{1500}$
* AES-CTR で暗号化された `encrypted_flag`

Allice秘密鍵は以下のように表せる。

$$
a = a_0 + k \cdot 2^{1500}
$$

* a_0 : 下位1500bit（既知）
* k : 上位36bit（未知、($0 \le k < 2^{36}$)）

この式をAlice公開鍵 $A = g^a \bmod p$ に代入すると、

$$
\begin{array}{l}
A = g^{a_0 + k \cdot 2^{1500}} \bmod p  \\ 
A = g^{a_0} \cdot \left(g^{2^{1500}}\right)^k \bmod p
\end{array}
$$

両辺を整理すると、

$$
A \cdot g^{-a_0} \equiv \left(g^{2^{1500}}\right)^k \bmod p
$$

ここで、

$$
\begin{array}{l}
T = A \cdot g^{-a_0} \bmod p  \\
h = g^{2^{1500}} \bmod p
\end{array}
$$

と置くと、以下のように表せる。

$$
h^k \equiv T \bmod p
$$

**方針**  
これは既知の底 $h = g^{2^{1500}}$ に対する離散対数問題

$$
h^k = T \bmod p
$$

Diffie-Hellmanは秘密指数が完全に秘匿されていることが前提のため、指数が線形に分解できるとBaby-step Giant-step (BSGS)が刺さる。  
$k < 2^{36}$と範囲が小さいため、BSGSの計算量は $O(2^{18}) \approx 260{,}000$ であり、実用時間で解ける。

**手順**  
1. 定数を用意する
2. BSGSでkを解く  
    探索範囲 $N = 2^{36}$  
    $m = \lceil \sqrt{N} \rceil \approx 2^{18}$
    * Baby step  
       $h^j \quad (0 \le j < m)$ をハッシュテーブルに保存。
    * Giant step  
       $T \cdot h^{-im}$ を計算し、baby step と一致するものを探す。

    一致すれば $k = im + j$

3. Alice秘密鍵を復元  
    $a = a_0 + k \cdot 2^{1500}$
4. 共通鍵とflagを復号
    * Diffie-Hellman共通鍵
        $K = B^a \bmod p$
    * セッション鍵
        ```python
        session_key = SHA256(K)
        ```
    * AES-CTRの仕様
        * nonceは8bytes
        * `encrypted_flag = nonce || ciphertext`

    これを用いて復号する。

**Solver**
```python solve.py
import math
import hashlib
from Crypto.Cipher import AES

A = 1599718256377804952101531599498863772568230618694466120580310027783856775419774715324430490009702307955575844601185230178048816258775546297605599320433889688149788702236901234905522868569967416567225850806042222083340147485157993071805547560375509693951764934940304995906394917881355417525918023021173242172441340007873982292615475287840119272527822675409016385400712544820436845576792437659620501263257558269716031694407258972273378598219915938064730248662540644
bob_public = 1601509205497326911166665651407955633086809897508704527950455620720477838507803621126588237807460352033730891991811162559292107072226732941342412621198125808491110851607803610326932944231441277178997305795098725764729855265846212191447644979975042348063533857732774890088844866567954281331492269751048224888559719840307800593782696008426362668779570407212587612644451479819243906619852333855883749307751229874778873609891502901892234753096522217233589204630723331
a0 = 18745015684416423248238358819116531099692322854758287583875043555248837262023679930415710097187512975438125769318401939978478358430852785607010460104247921522906629910012576819904488213243619895103769135299549586169221570769473234206574921382434244366730718275494665736161014808538417501350114510192342412033471326519013144824828968703748628325803878118375663318670612020895929494354336570752213975226257200515892803889402746161532447603042987169336605
encrypted_flag = bytes.fromhex("fb2f1136cea7c67b1edba34d3741eeac8442e70924b03202352422a28237ee6f3fb6d493")
g = 2
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

g_inv_a0 = pow(g, -a0, p)
T = (A * g_inv_a0) % p

h = pow(g, 2**1500, p)

N = 2**36
m = int(math.isqrt(N)) + 1

# baby steps
table = {}
cur = 1
for j in range(m):
    table[cur] = j
    cur = (cur * h) % p

# giant step factor
h_inv_m = pow(h, -m, p)

cur = T
for i in range(m):
    if cur in table:
        k = i*m + table[cur]
        break
    cur = (cur * h_inv_m) % p

alice_private = a0 + k * (2**1500)

shared_key = pow(bob_public, alice_private, p)
session_key = hashlib.sha256(
    shared_key.to_bytes(p.bit_length() // 8, "big")
).digest()

nonce = encrypted_flag[:8]
ct = encrypted_flag[8:]

cipher = AES.new(session_key, AES.MODE_CTR, nonce=nonce)
flag = cipher.decrypt(ct)
print(flag)
```

**Exploitation**  
```
$ python3 solve.py
b'Alpaca{1_hat3_c0u913s:fire:}'
```

Got the flag.

`Alpaca{1_hat3_c0u913s:fire:}`

# References
