# easy:Reverse Engineering

What is the FLAG?

※Flag format: FLAG{ *** }

attachment  
[easy_bin](easy_bin)

Point : 100

# Solution
配布ファイルを`file`で確認するとELFファイルであることが分かる。
`strings`で確認すると、「文字を入力して正しければcorrectと出力される」プログラムだと推測できる。
`readelf -a`で確認すると、`decode_flag`が見つかる。
pwngdbでdecode_flagが呼び出されているところを探す。
```
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000001240 <+0>:     endbr64
   0x0000000000001244 <+4>:     push   rbp
   0x0000000000001245 <+5>:     mov    rbp,rsp
   0x0000000000001248 <+8>:     sub    rsp,0xe0
   0x000000000000124f <+15>:    mov    rax,QWORD PTR fs:0x28
   0x0000000000001258 <+24>:    mov    QWORD PTR [rbp-0x8],rax
   0x000000000000125c <+28>:    xor    eax,eax
   0x000000000000125e <+30>:    lea    rax,[rbp-0x70]
   0x0000000000001262 <+34>:    mov    rdi,rax
   0x0000000000001265 <+37>:    call   0x11e9 <decode_flag>
   0x000000000000126a <+42>:    lea    rax,[rip+0xd93]        # 0x2004
   0x0000000000001271 <+49>:    mov    rdi,rax
   0x0000000000001274 <+52>:    mov    eax,0x0
   0x0000000000001279 <+57>:    call   0x10c0 <printf@plt>
   0x000000000000127e <+62>:    mov    rdx,QWORD PTR [rip+0x2e3b]        # 0x40c0 <stdin@GLIBC_2.2.5>
   0x0000000000001285 <+69>:    lea    rax,[rbp-0xe0]
   0x000000000000128c <+76>:    mov    esi,0x64
   0x0000000000001291 <+81>:    mov    rdi,rax
   0x0000000000001294 <+84>:    call   0x10e0 <fgets@plt>
   0x0000000000001299 <+89>:    lea    rax,[rbp-0xe0]
   0x00000000000012a0 <+96>:    lea    rdx,[rip+0xd6e]        # 0x2015
   0x00000000000012a7 <+103>:   mov    rsi,rdx
   0x00000000000012aa <+106>:   mov    rdi,rax
   0x00000000000012ad <+109>:   call   0x10d0 <strcspn@plt>
   0x00000000000012b2 <+114>:   mov    BYTE PTR [rbp+rax*1-0xe0],0x0
   0x00000000000012ba <+122>:   lea    rdx,[rbp-0x70]
   0x00000000000012be <+126>:   lea    rax,[rbp-0xe0]
   0x00000000000012c5 <+133>:   mov    rsi,rdx
   0x00000000000012c8 <+136>:   mov    rdi,rax
   0x00000000000012cb <+139>:   call   0x10f0 <strcmp@plt>
   0x00000000000012d0 <+144>:   test   eax,eax
   0x00000000000012d2 <+146>:   jne    0x12e5 <main+165>
   0x00000000000012d4 <+148>:   lea    rax,[rip+0xd3c]        # 0x2017
   0x00000000000012db <+155>:   mov    rdi,rax
   0x00000000000012de <+158>:   call   0x10a0 <puts@plt>
   0x00000000000012e3 <+163>:   jmp    0x12f4 <main+180>
   0x00000000000012e5 <+165>:   lea    rax,[rip+0xd34]        # 0x2020
   0x00000000000012ec <+172>:   mov    rdi,rax
   0x00000000000012ef <+175>:   call   0x10a0 <puts@plt>
   0x00000000000012f4 <+180>:   mov    eax,0x0
   0x00000000000012f9 <+185>:   mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000000012fd <+189>:   sub    rdx,QWORD PTR fs:0x28
   0x0000000000001306 <+198>:   je     0x130d <main+205>
   0x0000000000001308 <+200>:   call   0x10b0 <__stack_chk_fail@plt>
   0x000000000000130d <+205>:   leave
   0x000000000000130e <+206>:   ret
```
<main+37>に`decode_flag`の呼び出し部分があったので、<main+42>にブレイクポイントを設定して実行し、レジスタ等を確認する。
```
pwndbg> break *main+42
Breakpoint 1 at 0x126a
pwndbg> r
Breakpoint 1, 0x000055555555526a in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
─────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]─────────────────────────────────
 RAX  0x26
 RBX  0
 RCX  0x7d
 RDX  0x7d
 RDI  0x7fffffffdd70 ◂— 'FLAG{474eb333fc1e45cee08c0621cb0cbc5e}'
 RSI  0x7fffffffdef8 —▸ 0x7fffffffe167 ◂— 'directory'
 R8   0x7ffff7fa3f10 (initial+16) ◂— 4
 R9   0x7ffff7fc9040 (_dl_fini) ◂— endbr64
 R10  0x7ffff7fc3908 ◂— 0xd00120000000e
 R11  0x7ffff7fde660 (_dl_audit_preinit) ◂— endbr64
 R12  0x7fffffffdef8 —▸ 0x7fffffffe167 ◂— 'directory'
 R13  0x555555555240 (main) ◂— endbr64
 R14  0x555555557d98 (__do_global_dtors_aux_fini_array_entry) —▸ 0x5555555551a0 (__do_global_dtors_aux) ◂— endbr64
 R15  0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 —▸ 0x555555554000 ◂— 0x10102464c457f
 RBP  0x7fffffffdde0 ◂— 1
 RSP  0x7fffffffdd00 ◂— 2
 RIP  0x55555555526a (main+42) ◂— lea rax, [rip + 0xd93]
```
RDIの所にフラグが格納されていることが分かる。

flagが得られた。

`FLAG{474eb333fc1e45cee08c0621cb0cbc5e}`
