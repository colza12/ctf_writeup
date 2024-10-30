# endianness : General Skills

Know of little and big endian?  
[Source](flag.c)  
`nc titan.picoctf.net 56896`

Author : Nana Ama Atombo-Sackey

# Solution

とりあえず、`nc titan.picoctf.net 56896`を実行する。
```
$ nc titan.picoctf.net 56896
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: sbppe
Enter the Little Endian representation: 6570706273
Correct Little Endian representation!
Enter the Big Endian representation: 7362707065
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_02999450}
```
word`sbppe`をcberchefでTo Hexする。`73 62 70 70 65`と出力されるので、これを、little endianとbig endianに合わせて、並べ替える。  
人間にとって、little endianは逆順となり、big endianは正順となる。

flagが得られた。

`picoCTF{3ndi4n_sw4p_su33ess_02999450}`
