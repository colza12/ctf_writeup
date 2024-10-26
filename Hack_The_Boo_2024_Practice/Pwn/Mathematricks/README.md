# Mathematricks : Pwn

How about a magic trick? Or a math trick? Beat me and I will give you an amazing reward!

Attachment  
[pwn_mathematricks.zip](pwn_mathematricks.zip)  

Difficulty Level : very easy  

# Solution

とりあえず、実行してみる。
```
$ nc 94.237.52.166 31297

        🎉 ~~ w3lC0m3 2 tH3 M4th3M4tR1kCs c0nt35t ~~ 🎉

                        ■ ■ ■ ■ ■ ■ ■
                        ■           ■
                        ■ 1. Play   ■
                        ■ 2. Rules  ■
                        ■           ■
                        ■ ■ ■ ■ ■ ■ ■

                        🥸  1

                🎉 ~~ Let the game begin! ~~ 🎉

                Q1: 1 + 1 = ?

                > 2

                [+] THAT WAS AMAZING!

                Q2: 2 - 1 = ?

                > 1

                [+] WE HAVE A MATHEMATICIAN AMONG US!

                Q3: 1337 - 1337 = ?

                > 0

                [+] GOD OF MATHS JUST ENTERED THE CHAT..

                Q4: Enter 2 numbers n1, n2 where n1 > 0 and n2 > 0 and n1 + n2 < 0

                n1: 2147483647

                n2: 2147483647
HTB{m4th3m4tINT_5tuff_c01c10ce0d2f505cae0351b1171e766b}
```
Q1、Q2、Q3は普通に解く。Q4は条件を満たす整数は存在しないので、変数がint型であると推測して、int型の最大値を入力することでn1 + n2がint型の最小値になる。(はずである。C言語の仕様により。)  
flagが得られた。

`HTB{m4th3m4tINT_5tuff_c01c10ce0d2f505cae0351b1171e766b}`
