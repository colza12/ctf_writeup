# GDB baby step 4:Reverse Engineering

`main` calls a function that multiplies `eax` by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be `picoCTF{4096}`.\
Debug [this]().

# Solution

とりあえずgdbでアセンブリを確認。
```
0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
0x0000000000401140 <+36>:    mov    edi,eax
0x0000000000401142 <+38>:    call   0x401106 <func1>
0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
```
<func1>を呼び出している。func1のアセンブリを確認。
```
0x0000000000401106 <+0>:     endbr64 
0x000000000040110a <+4>:     push   rbp
0x000000000040110b <+5>:     mov    rbp,rsp
0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
0x0000000000401114 <+14>:    imul   eax,eax,0x3269
0x000000000040111a <+20>:    pop    rbp
0x000000000040111b <+21>:    ret
```
`imal eax,eax,0x3269`とあるので、フラグは0x3269を10進数にしたもの。

`picoCTF{12905}`

