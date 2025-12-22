# Shop : Reverse Engineering

Best Stuff - Cheap Stuff, Buy Buy Buy...  
Store Instance: [source](source). The shop is open for business at `nc mercury.picoctf.net 10337`.

Author : Dylan McGuire

# Solution

For now, try executing it.
```
$ nc mercury.picoctf.net 10337
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
0
How many do you want to buy?
-128
You have 1320 coins
        Item            Price   Count
(0) Quiet Quiches       10      140
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125]
```
Targeted the negative boundary of 1 byte.

Convert `112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 9 7 56 102 125` using from decimal in CyberChef.

Got the flag!

`picoCTF{b4d_brogrammer_3da34a8f}`
