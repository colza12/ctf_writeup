# Ides-le Talk : Cryptography

We intercepted a file from one of DEADFACE’s more amateur members. They claim that they hid a password in a text file. When we looked at the file, it’s indecipherable jibberish. We believe a common cipher was used to hide the message (and the password). As far as possible keys goes, maybe it can be determined by the author of the original text?

Submit the flag as `flag{flag-text}`

[Download File](Mischiefs-English-HW.txt) (114KB)  
SHA1: `d4239fe9e80cdcad49939edd1bbcf4b811f9286a`

Point : 15  
Author : Shamel

# Solution

添付ファイル`Mischiefs-English-HW.txt`を確認する。
```
Naq ab zna ryfr ungu ubabhe ol uvf qrngu.
YHPVYVHF
Fb Oehghf fubhyq or sbhaq. V gunax gurr, Oehghf,
Gung gubh unfg cebirq Yhpvyvhf' fnlvat gehr.
BPGNIVHF
Nyy gung freirq Oehghf, V jvyy ragregnva gurz.
Sryybj, jvyg gubh orfgbj gul gvzr jvgu zr?
FGENGB
Nl, vs Zrffnyn jvyy cersre zr gb lbh.
BPGNIVHF
Qb fb, tbbq Zrffnyn.
ZRFFNYN
Ubj qvrq zl znfgre, Fgengb?
FGENGB
V uryq gur fjbeq, naq ur qvq eha ba vg.
ZRFFNYN
...
```
文字列の見た目からROTであると推測できる。CyberChefで一番最初の行`Naq ab zna ryfr ungu ubabhe ol uvf qrngu.`をROT13する。  
`And no man else hath honour by his death.`という意味のある文章が出てくる。`flag`をROT13すると`synt`なので、文字列検索で`synt`に該当する箇所を探す。  
該当する箇所が1つ見つかる。`synt: Y3g_Gur#Zv$puvrsf^8361a`  
これをROT13して、flag形式に直す。  
flagが得られた。

`flag{L3t_The#Mi$chiefs^8361n}`
