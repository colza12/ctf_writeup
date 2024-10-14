# money-ware:General Skills

Flag format: picoCTF{Malwarename} The first letter of the malware name should be capitalized and the rest lowercase. Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

問題文より、マルウェアの名前を答えれば良いらしい。
とりあえず、謎文字列`1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`をgoogle先生になげてみる。
と、ランサムウェアである「Petya」という単語が散見されるので、submitしてみるとflagは「Petya」であっていた。

`picoCTF{Petya}`
