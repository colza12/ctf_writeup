# asm3 : Reverse Engineering

What does asm3(0xccf13937,0xbf0a24e4,0xf44d6917) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)

Author : Sanjay C

# Solution

Check the source code.
```S
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0x9]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xe]
	<+15>:	add    ah,BYTE PTR [ebp+0xf]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
```
The first argument 0xd2c26416 is stored at ebp+0x8, the second argument 0xe6cf51f0 at ebp+0xc, and the third argument 0xe54409d5 at ebp+0x10.  
At <+5>, ebp+0x9 is a 1-byte offset from ebp+0x8, so 0x64 is loaded into ah, making ax = 0x6400.  
At <+8>, ax is left-shifted by 0x10 bits, so eax = 0x64000000 and ax = 0x0000.  
At <+12>, ebp+0xe is a 2-byte offset from ebp+0xc, and 0xcf is subtracted from al, causing an underflow to 0x0031.  
At <+15>, ebp+0xf is a 3-byte offset from ebp+0xc, and 0xe6 is added to ah, resulting in 0xe631.  
At <+18>, ebp+0x12 is a 2-byte offset from ebp+0x10, and ax is XORed with 0xe544, yielding 0x0375.

Got the flag!

`0x375`
