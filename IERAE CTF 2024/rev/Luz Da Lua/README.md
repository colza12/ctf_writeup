# Luz Da Lua:rev

The luac file is compiled and tested on Lua 5.4.7  
`lua LuzDaLua.luac`

attachment  
[firectf_ierae-ctf-2024-prod-eh2j3_distfiles_luz-da-lua.tar.gz](firectf_ierae-ctf-2024-prod-eh2j3_distfiles_luz-da-lua.tar.gz)

Difficulty Level : easy  
Point : 159  
Solved : 86

# Solution
配布ファイルの中にLuzDaLua.luacがあったので、とりあえず、`lua LuzDaLua.luac`を実行してみる。
```
$ lua LuzDaLua.luac
Input > 111111
Wrong
```
LuzDaLua.luacをデコンパイルする。  
luaは互換性が非常に残念なことになっているため、バイナリファイルと同じバージョンのものを使う必要がある。実際、問題文にもコンパイルとテストを行ったのは、version5.4.7との記述がある。  
幸い、バージョンの関係なさそうな非常に便利なwebデコンパイラ([Lua Decompiler](https://luadec.metaworm.site/))を発見したので、これを利用した。
```lua
-- filename: @/mnt/LuzDaLua.lua
-- version: lua54
-- line: [0, 0] id: 0
io.write("Input > ")
input = io.read("*l")
if string.len(input) ~= 28 then
  goto label_301
elseif string.byte(input, 1) ~ 232 ~= 161 then
  goto label_301
elseif string.byte(input, 2) ~ 110 ~= 43 then
  goto label_301
elseif string.byte(input, 3) ~ 178 ~= 224 then
  goto label_301
elseif string.byte(input, 4) ~ 172 ~= 237 then
  goto label_301
elseif string.byte(input, 5) ~ 212 ~= 145 then
  goto label_301
elseif string.byte(input, 6) ~ 25 ~= 98 then
  goto label_301
elseif string.byte(input, 7) ~ 53 ~= 121 then
  goto label_301
elseif string.byte(input, 8) ~ 63 ~= 74 then
  goto label_301
elseif string.byte(input, 9) ~ 135 ~= 230 then
  goto label_301
elseif string.byte(input, 10) ~ 92 ~= 3 then
  goto label_301
elseif string.byte(input, 11) ~ 38 ~= 23 then
  goto label_301
elseif string.byte(input, 12) ~ 250 ~= 137 then
  goto label_301
elseif string.byte(input, 13) ~ 216 ~= 135 then
  goto label_301
elseif string.byte(input, 14) ~ 5 ~= 86 then
  goto label_301
elseif string.byte(input, 15) ~ 69 ~= 117 then
  goto label_301
elseif string.byte(input, 16) ~ 226 ~= 189 then
  goto label_301
elseif string.byte(input, 17) ~ 137 ~= 186 then
  goto label_301
elseif string.byte(input, 18) ~ 148 ~= 240 then
  goto label_301
elseif string.byte(input, 19) ~ 64 ~= 53 then
  goto label_301
elseif string.byte(input, 20) ~ 130 ~= 225 then
  goto label_301
elseif string.byte(input, 21) ~ 241 ~= 197 then
  goto label_301
elseif string.byte(input, 22) ~ 151 ~= 227 then
  goto label_301
elseif string.byte(input, 23) ~ 203 ~= 250 then
  goto label_301
elseif string.byte(input, 24) ~ 179 ~= 220 then
  goto label_301
elseif string.byte(input, 25) ~ 216 ~= 182 then
  goto label_301
elseif string.byte(input, 26) ~ 101 ~= 4 then
  goto label_301
elseif string.byte(input, 27) ~ 238 ~= 130 then
  goto label_301
elseif string.byte(input, 28) ~ 61 ~= 64 then
  goto label_301
else
  print("Correct")
end
-- warn: not visited block [59]
-- block#59:
-- _ENV.print("Wrong")
```
入力文字が28文字である必要があるらしい。さらに、大量のelseif文で各入力文字への条件が定められている。  
```
string.byte(input, 1) ~ 232 ~= 161
```
これは1つ目のelseifを抜き出したものである。`~`は、xorを表し、`string.byte(input, 1)`で入力文字の1文字目をbyte変換して取り出している。1文字目と232をxorして161と一致するかどうかを判断している。
xorの特徴として、`A xor B = C`のとき、`B xor C = A`が成り立つというのがある。これを利用して1文字ずつ条件を満たす文字を明かしていくと、以下の数字を導き出せる。  
```
73 69 82 65 69 123 76 117 97 95 49 115 95 83 48 95 51 100 117 99 28 116 49 111 110 97 108 125
```
cyberchefのfrom Decimalを使うと、
```
IERAE{Lua_1s_S0_3duc t1onal}
```
1つだけ可読文字ではないものが混入していたが、おそらく`Lua is so ecucational`という内容になるはずなので空白の部分には`a`または`4`が入ると推測できる。
試してみると`4`の方であった。  
```
$ lua LuzDaLua.luac
Input > IERAE{Lua_1s_S0_3duc4t1onal}
Correct
```
flagが得られた。

`IERAE{Lua_1s_S0_3duc4t1onal}`
