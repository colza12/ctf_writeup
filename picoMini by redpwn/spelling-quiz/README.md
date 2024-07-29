# spelling-quiz:Cryptography

I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.

attachment
* [public.zip]()

# Solution

zipファイルの中に暗号化スクリプト、暗号化されたフラグ、ディクショナリが入っていた。\
とりあえず、暗号化されたフラグをROT13でデコードするが、意味のある文字列が出てこなかった。\
おそらく、ホームズに出てくる、文字やパターンの出現頻度・傾向から解読するタイプの暗号(換字式暗号)であろう。\
暗号化スクリプトを見ても換字式暗号で間違いないようだ。
```python
alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))
```
ディクショナリがあるため、文字の出現頻度解析をしてくれるツールを使う。[Substitution cipher decoder](https://planetcalc.com/8047/)\
出現頻度分析から以下のようになった。

|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|S|P|R|G|W|H|K|J|O|Q|Z|L|D|C|U|V|Y|E|M|N|B|T|I|A|F|X|

表の通りに暗号化されたフラグの文字列を変換すると意味のある文字列が出てきた。[単一換字式暗号解読機](http://www.net.c.dendai.ac.jp/crypto/histogram2.html)\
これをフラグの形式になおす。

`picoCTF{perhaps_the_dog_jumped_over_was_just_tired}`

