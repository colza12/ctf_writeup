# B1ll_Gat35 : Reverse Engineering

Can you reverse this [Windows Binary](win-exec-1.exe)?

Author : Alex Bushkin

# Solution

For now, try executing it.
```
$ ./win-exec-1.exe
Input a number between 1 and 5 digits: 3
Initializing...
Enter the correct key to get the access codes: 39393939
Incorrect key. Try again.
```
Using the strings command, it was confirmed that the flag format is `PICOCTF{...}`.
```
C:\Users\abush\Desktop\pico-win-problems\win-exec-1.pdb
%llu
The key is:
%s%s
%llu
PICOCTF{These are the access codes to the vault:
%s%s%s
Input a number between 1 and 5 digits:
Number too big. Try again.
Initializing...
Enter the correct key to get the access codes:
Incorrect key. Try again.
Correct input. Printing flag:
```
Analyze it using Ollydbg.
```
$ file win-exec-1.exe
win-exec-1.exe: PE32 executable (console) Intel 80386, for MS Windows
```
Set a breakpoint around the point where "Input a number between 1 and 5 digits:" is displayed, and then step through the execution.  
From the results of the strings command, it can be seen that the key is output with "The key is:".  
If we initialize it with 1 and then find and input the key that should be output somewhere, the flag should appear.

![ollydbg](image/image1.png)  
Around the point where the initialization process finished, "The key is: 4253360" appeared on the memory dump screen.  
Enter it at the prompt "Enter the correct key to get the access codes:".  
However, what is needed is the access codes, not the key, so try entering `The key is: 4253360`.  
![flag](image/image2.png)

Got the flag!

`PICOCTF{These are the access codes to the vault: 1063340}`
