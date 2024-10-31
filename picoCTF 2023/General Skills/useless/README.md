# useless : General Skills

There's an interesting script in the user's home directory The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

Hostname: saturn.picoctf.net  
Port: 58374  
Username: picoplayer  
Password: password

Author : Loic Shema

# Solution

とりあえず、ssh接続する。
```
$ ssh picoplayer@saturn.picoctf.net -p 58374
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Thu Oct 31 00:01:27 2024 from 3.140.102.47
picoplayer@challenge:~$
```
ログインできた。homeディレクトリにあるスクリプトを探索しろとのことである。
```
$ ls
useless
$ man useless 

useless
     useless, -- This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_5657}
```
`man`コマンドは、コマンド、サブルーチン、ファイルなどのトピックに関する情報を提供するコマンドである。

flagが得られた。

`picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_5657}`
