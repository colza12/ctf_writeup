# OMG:Misc

Oh my God!!!My browser history has been hijacked!  
オーマイガー！！！ブラウザの履歴が乗っ取られてしまった！
* Challenge: http://35.221.200.7:80

Difficulty Level : warmup  
Point : 123  
Solved : 191 

# Solution
とりあえず、リンクにアクセスしてみる。  
![site_image0](image/site_image0.png)  
スタートボタンを押して、ブラウザの戻るボタンを33回押せば良いらしい。  
やってみる。  
![site_image1](image/site_image1.png)  
出題されている他の問題の宣伝と、戻るボタンの残り回数が表示された。  
続けて、カウントが0になるまで戻るボタンを押す。押しすぎるとカウントがリセットされる。  
![site_image2](image/site_image2.png)  
flagが得られた。

ちなみに、ierae ctfのスコアサーバを開いているタブでリンクをそのまま開くという失敗をしてしまったため、browserのhistoryをhijackingされてしまい、ブラウザの履歴から探してスコアサーバを開きなおすはめになりました。  
気を付けてください。

`IERAE{Tr3ndy_4ds.LOL}`
