# Bit-O-Asm-1:Reverse Engineering

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.\
Download the assembly dump [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Bit-O-Asm-1/disassembler-dump0_a.txt).

# Solution

disassembler-dump0_a.txtをテクストエディタで開く。
```
<+15>:    mov    eax,0x30
```
eaxに0x30を移動させている(格納している)ので、eaxレジスタには0x30(48)である。

`picoCTF{48}`

