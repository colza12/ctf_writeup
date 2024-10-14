# GDB baby step 2:Reverse Engineering

Can you figure out what is in the `eax` register at the end of the main function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Debug [this](debugger0_b).

# Solution

`chmod +x debugger0_b`でdebugger0_bを実行可能にする。gdbを起動して逆アセンブルする。
```
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
   0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
   0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
   0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
   0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
   0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401141 <+59>:    pop    rbp
   0x0000000000401142 <+60>:    ret    
End of assembler dump.
```
movが続いたあと、\<main+48\>にjmpして、何らかの計算をして\<main+38\>にjmpするループがあり、その後eaxに演算結果を格納している。
\<main+56\>の実行後のeaxを確認したいので、\<main+59\>にブレイクポイントを設定して実行したあと、eaxレジスタの情報を確認する。
```
(gdb) break *main+59
Breakpoint 1 at 0x401141
(gdb) r
Breakpoint 1, 0x0000000000401141 in main ()
(gdb) info registers eax
eax            0x4af4b             307019
```
flagが得られた。

`picoCTF{307019}`

