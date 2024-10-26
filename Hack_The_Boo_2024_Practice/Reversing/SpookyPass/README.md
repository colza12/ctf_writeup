# SpookyPass : Reveersing

All the coolest ghosts in town are going to a Haunted Houseparty - can you prove you deserve to get in?

Attachment  
[rev_spookypass.zip](rev_spookypass.zip)  

Difficulty Level : very easy  

# Solution

添付ファイルに含まれているpassを確認する。
```
$ strings pass
...
Welcome to the
[1;3mSPOOKIEST
[0m party of the year.
Before we let you in, you'll need to give us the password:
s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
Welcome inside!
You're not a real ghost; clear off!
...
```
passwordを求められたとき、`s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5`を入力するとフラグが得られそうだ。  
実行する。
```
$ ./pass
Welcome to the SPOOKIEST party of the year.
Before we let you in, you'll need to give us the password: s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
Welcome inside!
HTB{un0bfu5c4t3d_5tr1ng5}
```
flagが得られた。

`HTB{un0bfu5c4t3d_5tr1ng5}`
