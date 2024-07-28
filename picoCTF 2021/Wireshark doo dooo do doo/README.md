# Wireshark doo dooo do doo...:Forensics

Can you find the flag? [shark1.pcapng]().

# Solution 

wiresharkで添付ファイルを開くとProtocolのところにTCPとHTTPが並んでいるので、追跡→TCPストリームを見てみる。ストリーム5のところでフラグらしき文字列が見つかった。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3638553/64916d55-2b74-4d3f-8731-8a94ac8c712a.png)
ROT13で暗号化されてそうなので、デコードするとフラグが得られた。

`picoCTF{p33kab00_1_s33_u_deadbeef}`
