# Wireshark doo dooo do doo...:Forensics

Can you find the flag? [shark1.pcapng]().

# Solution 

wiresharkで添付ファイルを開くとProtocolのところにTCPとHTTPが並んでいるので、追跡→TCPストリームを見てみる。ストリーム5のところでフラグらしき文字列が見つかった。
![image.png](https://github.com/colza12/ctf_writeup/blob/main/picoCTF%202021/Wireshark%20doo%20dooo%20do%20doo/tcp_stream.png)
ROT13で暗号化されてそうなので、デコードするとフラグが得られた。

`picoCTF{p33kab00_1_s33_u_deadbeef}`
