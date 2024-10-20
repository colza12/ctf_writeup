# GDB baby step 1:Reverse Engineering

Can you figure out what is in the `eax` register at the end of the main function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Disassemble [this](debugger0_a).

# Solution

debugger0_aはELFファイル。`objdmp`を使っても良いが、タイトルにGDBと入っているので、`gdb`を使う。
```
$ gdb debugger0_a
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64 
   0x000000000000112d <+4>:     push   %rbp
   0x000000000000112e <+5>:     mov    %rsp,%rbp
   0x0000000000001131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:    mov    $0x86342,%eax
   0x000000000000113d <+20>:    pop    %rbp
   0x000000000000113e <+21>:    ret    
End of assembler dump.
```
Intel記法が良ければ`set disassembly-flavor intel`を実行。
```
0x0000000000001129 <+0>:     endbr64 
0x000000000000112d <+4>:     push   rbp
0x000000000000112e <+5>:     mov    rbp,rsp
0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
0x0000000000001138 <+15>:    mov    eax,0x86342
0x000000000000113d <+20>:    pop    rbp
0x000000000000113e <+21>:    ret
```
eaxレジスタに0x86342を格納していることが分かる。

flagが得られた。

`picoCTF{549698}`

