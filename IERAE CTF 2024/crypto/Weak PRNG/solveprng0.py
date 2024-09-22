import re
from pwn import *

p = remote("35.201.137.32", 19937)

payload = b"1"


listhint=[]
for i in range(2):
    response = str(p.recvline())
    listhint.append(response)
for i in range(39):
    p.sendline(payload)
    for j in range(23):
        response = str(p.recvline())
        listhint.append(response)

substring = "--"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "random"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Submit"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Quit"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Enter"
listhint = list(filter(lambda item: substring not in item, listhint))
substring = "Menu"
listhint = list(filter(lambda item: substring not in item, listhint))
listhint = listhint[2:]

for i in range(len(listhint)):
    print(listhint[i])


pyload = b"2"
p.sendline(payload)
p.interactive()
