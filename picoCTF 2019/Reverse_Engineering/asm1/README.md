# asm1 : Reverse Engineering

What does asm1(0x36e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)

Author : Sanjay C

# Solution

Check the source code.
```S
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x71c
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x6cf
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x3
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x3
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x8be
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0x3
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x3
	<+60>:	pop    ebp
	<+61>:	ret    
```
Assume that `0x8be` is passed as an argument.  
At <+3>, it is compared with 0x71c, and since the condition is met, the jg at <+10> causes a jump to <+37>.  
At <+37>, it is compared with 0x8be, and since the condition is not met, the jne at <+44> does not trigger, so execution proceeds to the next instruction.  
At <+46>, 0x8be is stored in eax, and at <+49>, 0x3 is subtracted from eax, so eax becomes 0x8bb.  
Then, the unconditional jump at <+52> jumps to <+60>, where the final ret instruction is executed, so the return value is 0x8bb.

Got the flag!

`0x8bb`
