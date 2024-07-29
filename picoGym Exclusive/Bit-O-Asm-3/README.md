# Bit-O-Asm-3:Reverse Engineering

Description
Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.\
Download the assembly dump [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Bit-O-Asm-3/disassembler-dump0_c.txt).

# Solution

disassembler-dump0_c.txtをテキストエディタで開く。
```
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
```
0x9fe1a\*0x4+0x1f5をして演算結果をeaxに格納している。
654874\*4+501=2619997である。

`picoaCTF{2619997}`

