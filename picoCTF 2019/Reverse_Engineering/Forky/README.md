# Forky : Reverse Engineering

In [this program](vuln), identify the last integer value that is passed as parameter to the function doNothing().

Author : Samuel

# Solution

Set a breakpoint at the point where the doNothing function is called in GDB, and run the program.
```
pwndbg> b *main+129
pwndbg> r
pwndbg> info register edx
edx            0xd4faf720          -721750240
```
By checking the first argument of the doNothing function, we can see the value that is finally passed. The first argument is stored in the edx register, so its value was displayed.

Got the flag!

`picoCTF{-721750240}`
