# Let Me In : TrendyTrove

DEADFACE is running an e-commerce site in an attempt to scam victims and steal their data and their money! See if you can find a way to access the site. Submit the flag found on the main page.

Submit the flag as `flag{flag-text}`

[TrendyTrove](https://trendytrove.deadface.io/)

Point : 15  
Solved : 444  
Author : syyntax

# Solution

[TrendyTrove](https://trendytrove.deadface.io/)にアクセスする。  
![site-image](image/image0.png)  
問題文からも分かる通り、典型的なSQLiである。`Username`と`Password`両方に`' or 1=1--`を入力してLoginボタンを押す。  
adminアカウントへのログインに成功する。  
![admin-site](image/image1.png)  
問題文より、このmain pageからflagを探す。見た目にはflagがありそうには見えないのでDevToolsでscriptを確認する。
![html-image](image/image2.png)  
flagが得られた。

`flag{Tr3ndy_Tr0v3_$QL_1nj3ct10n}`
