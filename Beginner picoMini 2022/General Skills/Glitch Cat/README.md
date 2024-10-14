# Glitch Cat:General Skills

Our flag printing service has started glitching!  
`$ nc saturn.picoctf.net 49649`

# Solution

問題文どおりにプロンプトにコピペする。
```
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```
と出力されるので、cyberchefのfrom Hexで16進数を文字列に直す。

flagが得られた。

`picoCTF{gl17ch_m3_n07_9c42a45d}`
