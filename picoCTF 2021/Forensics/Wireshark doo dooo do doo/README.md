# Wireshark doo dooo do doo...:Forensics

Can you find the flag? [shark1.pcapng](shark1.pcapng).

# Solution 

wiresharkで添付ファイルを開くとProtocolのところにTCPとHTTPが並んでいるので、追跡→TCPストリームを見てみる。ストリーム5のところでフラグらしき文字列が見つかった。
![image.png](image/tcp_stream.png)
ROT13で暗号化されてそうなので、デコードするとフラグが得られた。

`picoCTF{p33kab00_1_s33_u_deadbeef}`
