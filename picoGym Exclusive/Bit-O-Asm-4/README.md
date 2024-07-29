# Bit-O-Asm-4:Reverse Engineering

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.\
Download the assembly dump [here]().

# Solution

disassembler-dump0_d.txtをテキストエディタで開く。
```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
```
cmpで0x9fe1aと0x2710を比較。jleはless or equalであるから、`0x9fe1a > 0x2710`より、jmpしない。
subで`0x9fe1a - 0x65 = 0x9fdb5`をDWORD PTR [rbp-0x4]に格納。jmpで<+41>に移動してmovで0x9fdb5をeaxに格納。よってeaxレジスタには`0x9fdb5 = 654773`が入っている。

`picoCTF{654773}`

