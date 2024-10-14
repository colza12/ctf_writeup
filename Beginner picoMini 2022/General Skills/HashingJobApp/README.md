# HashingJobApp:General Skills

If you want to hash with the best, beat this test!  
`nc saturn.picoctf.net 57702`

# Solution

問題文のとおりにプロンプトに`nc saturn.picoctf.net 57702`をコピペして実行する。と、表示された文字列のMD5ハッシュ値を答えろとの指示があるため、MD5ハッシュ値を求めて入力する。３回繰り返すとflagが得られた。
```
$ nc saturn.picoctf.net 59114
Please md5 hash the text between quotes, excluding the quotes: 'log cabins'
Answer: 
0cf9a466703d6f50227a4f85dfc63b58
0cf9a466703d6f50227a4f85dfc63b58
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'local police'
Answer: 
b36e4003adb9138e0c7f0379b9be4d5b
b36e4003adb9138e0c7f0379b9be4d5b
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'Adolf Hitler'
Answer: 
540dea05a35b0fc9a050f36db954a484
540dea05a35b0fc9a050f36db954a484
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}
```

`picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}`

