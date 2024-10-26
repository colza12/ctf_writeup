# El Pipo : Pwn

An ancient spirit, El Pipo, has taken control of this place. Face your fears and try to drive it away with your most vicious scream!

Attachment  
[pwn_el_pipo.zip](pwn_el_pipo.zip)  

Difficulty Level : easy  

# Solution

とりあえず、実行してみる。
```
$ nc 94.237.58.171 36283
aaaaaaaa
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 400</p>
        <p>Message: Bad request syntax ('aaaaaaaa').</p>
        <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
    </body>
</html>
```
HTTPSリクエストを送信するようなプログラムになっているらしい。  
試しにflag.txtを取得するリクエストを送ってみる。
```
$ nc 94.237.58.171 36283
GET flag.txt

HTB{3l_p1p0v3rfl0w_a1bee3c4f0268d282d82e4998b99fbae}
```
flagが得られた。

`HTB{3l_p1p0v3rfl0w_a1bee3c4f0268d282d82e4998b99fbae}`
