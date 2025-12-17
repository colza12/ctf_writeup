# asm2 : Reverse Engineering

What does asm2(0xf,0x17) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)

Author : Sanjay C

# Solution

Check the source code.
```S
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    
```
Pass 0x4 as the first argument and 0x2d as the second argument.  
At <+6> and <+9>, 0x2d is stored at ebp-0x4, and at <+12> and <+15>, 0x4 is stored at ebp-0x8.  
The unconditional jump at <+18> jumps to <+31>.  
At <+31>, 0x5fa1 is compared with 0x4, and since the condition is met, execution jumps to <+20> at <+38>.  
At <+20>, 0x2d + 0x1 = 0x2e.  
At <+24>, 0x4 + 0xd1 = 0xd5.  
Then, at <+31>, 0x5fa1 is compared with 0xd5.

From the above, this process returns the number of iterations required to add 0xd1 to 0x4 until it exceeds 0x5fa1.  
Since 0x5fa1 / 0xd1 = 0x75 (with a remainder), 0x76 is added to the initial value 0x2d, resulting in 0xa3 as the final value in eax.

Got the flag!

`0xa3`
