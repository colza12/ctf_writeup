# two-sum:Binary Exploitation

Can you solve this? What two positive numbers can make this possible: `n1 > n1 + n2 OR n2 > n1 + n2`\
Enter them here `nc saturn.picoctf.net 55489`. [Source]()

# Solution

普通に考えて「n1 > n1 + n2 OR n2 > n1 + n2」が成り立つ正数は存在しない。ソースコードがcであることを考慮して、intの最大値を狙う。
とりあえず、`nc saturn.picoctf.net 55489`を実行してみる。
```
$ nc saturn.picoctf.net 55489
n1 > n1 + n2 OR n2 > n1 + n2 
What two positive numbers can make this possible: 
2147483647 2147483647
You entered 2147483647 and 2147483647
You have an integer overflow
YOUR FLAG IS: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_482d8fc4}
```
フラグが得られた。

`picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_482d8fc4}`

