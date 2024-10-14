# blotting out:Misc

パスワードを答えてください。\
※教訓：中途半端に消すと消えなくなる可能性があります。\
ーーーーーーーーーーーーーーーーーーーーーーーーーー\
Please answer the password.\
※Lesson learned: There is a possibility that it will not disappear if you erase it half-heartedly.

attachment\
[nuritsubuchi.png](https://github.com/colza12/private_ctf_writeup/blob/main/Japan-UkraineCTF/Misc/blotting%20out/nuritsubuchi.png)

Point : 50

# Solution
添付ファイルを見てみる。\
![nuritsubuchi.png](https://github.com/colza12/private_ctf_writeup/blob/main/Japan-UkraineCTF/Misc/blotting%20out/nuritsubuchi.png)
おそらく、塗りつぶされている下にフラグのデータが残っているのだろう。
うさみみハリケーンのAoZoraSiroNeko.exeでステガノグラフィ解析する。赤色ビット0抽出で可読文字列が出てきた。
![image0.png](https://github.com/colza12/private_ctf_writeup/blob/main/Japan-UkraineCTF/Misc/blotting%20out/image/image0.png)

flagが得られた。

`kimetsu`