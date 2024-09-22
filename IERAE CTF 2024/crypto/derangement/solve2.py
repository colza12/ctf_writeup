import re
from pwn import *

p = remote("35.221.153.165", 55555)

payload = b"1"

listkey=[]
listhint=[]

for _ in range(9):
    response = str(p.recvline())
    listhint.append(response)

for i in range(100):
    p.sendline(payload)
    for _ in range(3):
        response = str(p.recvline())
        response = response.replace("> hint: ","")
        listhint.append(response)

substring = "type"
listhint = list(filter(lambda item: substring not in item, listhint))
listhint = listhint[9:]

for i in range(15):
    listkey.append(listhint[0])

for i in range(len(listhint)):
    print(listhint[i])

for i in range(len(listhint)):
    for j in range(15):
        listkey[j] = listkey[j].replace(listhint[i][j]," ")

for i in range(len(listkey)):
    print(listkey[i])

pyload = b"2"
p.sendline(payload)
p.interactive()