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
