# Nice netcat... (General Skills)

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

# Solution

問題文に掲載されているコマンドをそのままコピペすると、
```
$ nc mercury.picoctf.net 22342
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
53 
102 
98 
53 
101 
53 
49 
100 
125 
10 
```
10進数のASCIIっぽいので、変換ツールに投げてみるとフラグが得られた。

`picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}`
