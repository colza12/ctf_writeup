from Crypto.Cipher import AES

key = bytes.fromhex("9de75c29b50738710d83493973fdeb9c")

with open("waiwai", "rb") as f:
    data = f.read()

iv = data[:16]
ciphertext = data[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# PKCS7パディング除去
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

with open("flag.png", "wb") as f:
    f.write(plaintext)
