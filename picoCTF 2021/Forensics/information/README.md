# information:Forensics

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](cat.jpg)

# Solution

とりあえずテキストエディタで開く。
```
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
 </rdf:Description>
```

licenseのところが気になるので、base64デコードしてみる、とflagが得られた。

`picoCTF{the_m3tadata_1s_modified}`

ちなみに、画像ファイル等のメタデータの読み取りなどをするのに、ExifToolが使えそう。
