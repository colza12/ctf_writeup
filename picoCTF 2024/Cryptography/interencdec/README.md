# interencdec : Cryptography

Can you get the real meaning from this file.  
Download the file [here](enc_flag). 

Author : NGIRIMANA Schadrack

# Solution

enc_flagをメモ帳で開くと、以下の謎文字列が出てきた。  
`YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg==`  
これをcyberchefでbase64 decodeする。  
謎文字列`b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ=='`が出力された。  
`'`で囲まれた部分を取り出して。もう一度base64 decodeする。  
謎文字列`wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}`が出力された。  
rot19する。  
flagが得られた。

`picoCTF{caesar_d3cr9pt3d_a47c6d69}`
