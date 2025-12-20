from pwn import *
data = "110e02062d392f0807001d49031215470f431a1001081a04091a"
key = "againmissing"

data = bytes.fromhex(data)
flag = xor(data, key)

print(flag)