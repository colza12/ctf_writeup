# GDB baby step 3:Reverse Engineering

Now for something a little different. `0x2262c96b` is loaded into memory in the `main` function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb addr`. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.  
Debug [this](debugger0_c).

# Solution

```
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
```
0x2262c96bがロードされた後のところにブレイクポイントを設定。
メモリの格納されている場所はrbp-0x4で、`x/4xb addr`これを使えとのことである。
```
break *main+22
Breakpoint 1 at 0x40111c
(gdb) r
Breakpoint 1, 0x000000000040111c in main ()
(gdb) x/4xb $rbp-0x4   
0x7fffa216877c: 0x6b    0xc9    0x62    0x22
```
`0x6b    0xc9    0x62    0x22`が出てきたのでflag形式に直す。

`picoCTF{0x6bc96222}`

