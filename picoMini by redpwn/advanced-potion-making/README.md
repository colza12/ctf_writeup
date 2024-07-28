# advanced-potion-making:Forensics

Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

attachment
* [advanced-potion-making](https://github.com/colza12/ctf_writeup/blob/main/picoMini%20by%20redpwn/advanced-potion-making/advanced-potion-making)

# Solution

とりあえずテキストエディタで開く。と拡張子の部分が`臼B`となっていた。これはPBファイルの拡張しであるが、他の部分に画像ファイルっぽさを感じる。問題文より、ファイルの中身を見てどこかをいじれば良いらしい。おそらく、ファイルヘッダをPBからPNGに変更すれば良いはず。
PNGファイルシグネチャは`89 50 4E 47 0D 0A 1A 0A`であるから、バイナリエディタで変更。ついでに、その先も見たら、IHDRチャンクが必須チャンクで、ここも変更する必要があるらしい。シグネチャの次の8バイトを`00 00 00 0D 49 48 44 52`に変更。
すると、真っ赤な画像が出てきたのでうさ耳ハリケーンでステガノグラフィ解析する。赤色0ビット抽出でフラグが出てきたが、LSB(最下位ビット)を強調の方が見やすい？気がする。
![image.png](https://github.com/colza12/ctf_writeup/blob/main/picoMini%20by%20redpwn/advanced-potion-making/image/flag.png)

`picoCTF{w1z4rdry}`
