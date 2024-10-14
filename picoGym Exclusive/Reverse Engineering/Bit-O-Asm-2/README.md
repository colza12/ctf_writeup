# Bit-O-Asm-2:Reverse Engineering

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Download the assembly dump [here](disassembler-dump0_b.txt).

# Solution

disassembler-dump0_b.txtをテキストエディタで開く。
```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
```
rbp-0x4のところに0x9fe1aがあって、さらにそれをeaxに格納している。よって、eaxレジスタには0x9fe1a(654874)が入っている。

flagが得られた。

`picoCTF{654874}`

