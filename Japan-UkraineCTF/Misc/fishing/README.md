# fishing:Misc

添付はAmazonを装ったフィッシングメールである。  
メールの送信元ドメインは実在するドメインを用い、本文は巧みに偽装されている。  
本物だと信じた場合、どのサイトに不正アクセスさせられ、個人情報を入力するように求めてくるか。  
接続先のURLを答えよ。  
ーーーーーーーーーーーーーーーーーーーーーーーーーーー   
The attachment is a phishing email pretending to be from Amazon.  
The sender domain of the email is a real domain, and the body of the email is cleverly disguised.  
If you believe it to be genuine, which site will you be tricked into and will ask you to enter your personal information?  
Please provide the URL to connect to.

attachment  
[Amazon_Pay.eml](Amazon_Pay.eml)

Point : 50

# Solution
とりあえず、添付ファイルを開く。
`amazonログイン`ボタンがあり、謎のリンク先に遷移するようになっていた。

flagが得られた。

`https://www.amazon.co.jp.b312310cc.vwx/`
