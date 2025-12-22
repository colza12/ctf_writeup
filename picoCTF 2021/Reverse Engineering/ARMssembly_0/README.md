# ARMssembly 0 : Reverse Engineering

What integer does this program print?  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})  
Use arguments a and b: 2593949075 and 2233560849  
File: [chall.S](chall.S)

Author : Dylan McGuire

# Solution

Check the file.
```S
	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
First, there is the prologue of the main function.  
The instructions `str w0, [x29, 44]` and `str x1, [x29, 32]` store the arguments on the stack.  
`w0 = 3854998744 = 44 bytes from x29` and `x1 = 915131509 = 32 bytes from x29`.

The ldr instruction loads the pointer to 915131509 into x0. The subsequent add and ldr instructions retrieve the eighth byte from 915131509, which is then converted from character to number using `bl atoi`. In other words, it converts the character "9" to a number. The result of this conversion is stored in w19.  
Next, the 16th digit of 915131509, that is, the seventh 7 in 3854998744, is converted to a number and stored in w1.  
`bl func1` calls func1.  
In func1, w0 is stored at `[sp, 12]` and w1 at `[sp, 8]`.  
Furthermore, swap the values of w0 and w1 and compare them; if w1 is smaller or equal, return the value of w0. Otherwise, return the value of w1.  
In the main function, the returned value is stored in w1, so w1 = 3854998744.  
Furthermore, the value of w19 is stored in w0, and func1 is called again.  
The returned value is stored in w1, so w1 = 3854998744.  
Finally, it outputs the larger of the two values.

From the above, it can be understood that the programme outputs the larger value from the arguments passed to it.

Got the flag!

`picoCTF{e5c69cd8}`
