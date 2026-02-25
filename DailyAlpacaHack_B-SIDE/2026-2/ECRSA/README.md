# ECRSA : Crypto

Elliptic Curve x RSA = ECRSA

Attachment  
[ret2basics.tar.gz](ret2basics.tar.gz)  

Difficulty Level : Very Hard  
Tags : Elliptic Curve, RSA  
Author : theoremoon

# Solution

**問題概要**  
以下の手順でRSA風の暗号を生成している。ポイントは、RSAの因数 $q, r$ が楕円曲線の2倍公式 $R = 2Q$ と関連していること。
1.  楕円曲線 secp521r1 上でランダムな点 $Q$ を生成
2.  $R = 2Q$ を計算
3.  $q = x(Q), r = x(R)$ が共に素数になるまで繰り返す
4.  RSAのmodulus $n = q \cdot r$ 、公開指数 $e = 65537$ を作る
5.  メッセージ $m < n$ を暗号化して $c = m^e \bmod n$ を出力

**観察**  
```sage
import os

# secp521r1 patemeter
p = 0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
K = GF(p)
a = K(0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc)
b = K(0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00)
EC = EllipticCurve(K, (a, b))

while True:
    Q = EC.random_point()
    q = int(Q.xy()[0])
    R = 2*Q
    r = int(R.xy()[0])
    if is_prime(q) and is_prime(r):
        break

n = q*r
e = 65537
m = int.from_bytes(os.environ.get("FLAG", "Alpaca{dummy}").encode(), "big")
assert m < n
c = pow(m, e, n)

print("n = {}".format(n))
print("e = {}".format(e))
print("c = {}".format(c))
```
通常のRSAは $q, r$ に関係性はないため因数分解できない。  
2倍公式を考えると、

$$
x(2Q) = \frac{(3x(Q)^2 + a)^2}{4y^2} - 2x(Q), \quad y^2 = x(Q)^3 + a x(Q) + b
$$

$$
\Rightarrow r = x(2Q) = \frac{(3q^2 + a)^2}{4(q^3 + a q + b)} - 2q
$$

となり、 $q, r$ の関係式を書ける。  
また、楕円曲線は $\bmod p$ 上で定義されているため、２倍公式も $\bmod p$ でしか成立しない。

$$
r \equiv f(q) \bmod p
$$

**方針**  
$n = qr (q, r < p)$ より、

$$
n \bmod p = q r \bmod p
$$

となる。  
2倍公式を代入すると、

$$
x(Q) \cdot x(2Q) \equiv q \cdot f(q) \equiv n \bmod p
$$

pが既知であることを利用して、 $\bmod p$ 上で方程式を立てて多項式の根を探すことにより、 $q$ を特定できる。

**手順**  
1. $N_p = n \bmod p$ を計算
2. 有理式 $f(q)$ の分母を払って、多項式 $F(q)$ を作る
3. $Fp$ 上で多項式の根 $q$ を求める
4. r = n / q
5. $φ(n)$ を計算し、秘密鍵dを求めて復号

**Solver**
```sage solve.sage
n = 24489807923160829853331858278295353076882496748356437425136070159565438013983472411573830861255379509744527059864107405391335396070661875605498494586447825822788450364814932266675738776136998383491576779465083731669643596152181500936763824489148317369367655622357267302603914593581625372679508643581386912033877057
e = 65537
c = 2878521000528279319502304373550176174118970956553760958198895851295578685557304197481600194317208136193632870619822554981703968844914526643614371981441816886658546070361109613762488893788055957762778868012759138069722552457665235326670564609161988943959614368453819936924812599400584406309008222724731151234689436

# secp521r1
p = 0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
a = 0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc
b = 0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00

Fp = GF(p)
PR.<x> = PolynomialRing(Fp)

Np = Fp(n % p)

# 4(x^3+ax+b)*(x*f - Np)
lhs = x*((3*x^2 + a)^2 - 8*x*(x^3 + a*x + b))
rhs = 4*Np*(x^3 + a*x + b)

F = lhs - rhs

F = F.monic()

print("[*] degree =", F.degree())
print("[*] factoring over Fp...")

roots = F.roots()

print("[*] roots found:", len(roots))

for root, mult in roots:
    q = Integer(root)
    if q > 0 and n % q == 0:
        r = n // q
        print("[+] factor found!")
        print("q =", q)
        print("r =", r)

        phi = (q-1)*(r-1)
        d = inverse_mod(e, phi)
        m = pow(c, d, n)

        print("[+] FLAG:", Integer(m).to_bytes((m.bit_length()+7)//8,'big'))
        break
```

**Exploitation**  
```
[*] degree = 5
[*] factoring over Fp...
[*] roots found: 3
[+] factor found!
q = 5331886564089034574158460157636112130288696911329986749369729899519368477020323947965850005198183379428534220831032669306233898361673563514779169202705350157
r = 4593084948225070020618129217191209585444095634238239522921574706843335059675871197896150058328530879795294515182442563481049153380663801868209811391065181701
[+] FLAG: b'Alpaca{easier_cracked_ruined_suboptimal_algorithm}'
```

Got the flag.

`Alpaca{easier_cracked_ruined_suboptimal_algorithm}`

# References
