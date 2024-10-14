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
