# Assignment:rev

Assignment is the root of everything in procedural programs.

attachment\
[firectf_ierae-ctf-2024-prod-eh2j3_distfiles_assignment.tar.gz](https://github.com/colza12/ctf_writeup/blob/main/IERAE%20CTF%202024/rev/Assignment/firectf_ierae-ctf-2024-prod-eh2j3_distfiles_assignment.tar.gz)

Difficulty Level : warmup\
Point : 140\
Solved : 127 

# Solution
添付ファイルには、chalというファイルのみ入っていた。\
テキストエディタで確認してみるとELFファイルであることが分かるので、pwngdbを使って解析していく。\
`layout asm`でアセンブリのほぼ全てが表示される程度の短さなので、逆アセンブル作業は必要ない。(ただし、`layout asm`を実行するとコピペができない)\
ざっくりと見ると、明らかにフラグを1文字ずつ格納している部分がある。
```
   0x0000000000001158 <+15>:    mov    BYTE PTR [rip+0x2efd],0x33        # 0x405c <flag+28>
   0x000000000000115f <+22>:    mov    BYTE PTR [rip+0x2edb],0x45        # 0x4041 <flag+1>
   0x0000000000001166 <+29>:    mov    BYTE PTR [rip+0x2ed5],0x52        # 0x4042 <flag+2>
   0x000000000000116d <+36>:    mov    BYTE PTR [rip+0x2ee0],0x72        # 0x4054 <flag+20>
   0x0000000000001174 <+43>:    mov    BYTE PTR [rip+0x2edf],0x61        # 0x405a <flag+26>
   0x000000000000117b <+50>:    mov    BYTE PTR [rip+0x2ec8],0x5f        # 0x404a <flag+10>
   0x0000000000001182 <+57>:    mov    BYTE PTR [rip+0x2ed7],0x7d        # 0x4060 <flag+32>
   0x0000000000001189 <+64>:    mov    BYTE PTR [rip+0x2eb9],0x65        # 0x4049 <flag+9>
   0x0000000000001190 <+71>:    mov    BYTE PTR [rip+0x2ebf],0x6e        # 0x4056 <flag+22>
   0x0000000000001197 <+78>:    mov    BYTE PTR [rip+0x2eb3],0x5f        # 0x4051 <flag+17>
   0x000000000000119e <+85>:    mov    BYTE PTR [rip+0x2ea1],0x73        # 0x4046 <flag+6>
   0x00000000000011a5 <+92>:    mov    BYTE PTR [rip+0x2e9b],0x30        # 0x4047 <flag+7>
   0x00000000000011ac <+99>:    mov    BYTE PTR [rip+0x2e9c],0x30        # 0x404f <flag+15>
   0x00000000000011b3 <+106>:   mov    BYTE PTR [rip+0x2e96],0x6d        # 0x4050 <flag+16>
   0x00000000000011ba <+113>:   mov    BYTE PTR [rip+0x2e94],0x31        # 0x4055 <flag+21>
   0x00000000000011c1 <+120>:   mov    BYTE PTR [rip+0x2e90],0x5f        # 0x4058 <flag+24>
   0x00000000000011c8 <+127>:   mov    BYTE PTR [rip+0x2e7d],0x34        # 0x404c <flag+12>
   0x00000000000011cf <+134>:   mov    BYTE PTR [rip+0x2e83],0x35        # 0x4059 <flag+25>
   0x00000000000011d6 <+141>:   mov    BYTE PTR [rip+0x2e82],0x63        # 0x405f <flag+31>
   0x00000000000011dd <+148>:   mov    BYTE PTR [rip+0x2e5f],0x41        # 0x4043 <flag+3>
   0x00000000000011e4 <+155>:   mov    BYTE PTR [rip+0x2e55],0x49        # 0x4040 <flag>
   0x00000000000011eb <+162>:   mov    BYTE PTR [rip+0x2e6b],0x35        # 0x405d <flag+29>
   0x00000000000011f2 <+169>:   mov    BYTE PTR [rip+0x2e59],0x73        # 0x4052 <flag+18>
   0x00000000000011f9 <+176>:   mov    BYTE PTR [rip+0x2e53],0x74        # 0x4053 <flag+19>
   0x0000000000001200 <+183>:   mov    BYTE PTR [rip+0x2e44],0x72        # 0x404b <flag+11>
   0x0000000000001207 <+190>:   mov    BYTE PTR [rip+0x2e3a],0x6d        # 0x4048 <flag+8>
   0x000000000000120e <+197>:   mov    BYTE PTR [rip+0x2e30],0x7b        # 0x4045 <flag+5>
   0x0000000000001215 <+204>:   mov    BYTE PTR [rip+0x2e28],0x45        # 0x4044 <flag+4>
   0x000000000000121c <+211>:   mov    BYTE PTR [rip+0x2e38],0x39        # 0x405b <flag+27>
   0x0000000000001223 <+218>:   mov    BYTE PTR [rip+0x2e34],0x34        # 0x405e <flag+30>
   0x000000000000122a <+225>:   mov    BYTE PTR [rip+0x2e26],0x67        # 0x4057 <flag+23>
   0x0000000000001231 <+232>:   mov    BYTE PTR [rip+0x2e15],0x6e        # 0x404d <flag+13>
   0x0000000000001238 <+239>:   mov    BYTE PTR [rip+0x2e0f],0x64        # 0x404e <flag+14>
```
フラグがripに格納されていそうなので、フラグの格納が終わった次のアドレス<main+246>にブレイクポイントを設定して、実行し、rip+0x2e0fの文字列を取得する。
```
pwndbg> break *main+246
Breakpoint 1 at 0x123f
pwndbg> r
pwndbg> x/s $rip+0x2e0f
0x55555555804e <flag+14>:       "d0m_str1ng_5a9354c}"
```
フラグの後半だけが出力された。前半部分を探すのは少し手間だったため、ripに格納するasciiコードを手動で並べ替え、cyberchefでfrom Hexしてしまった。(デコンパイラを使うと、フラグがそのまま出力される。)\
flagが得られた。

`IERAE{s0me_r4nd0m_str1ng_5a9354c}`
