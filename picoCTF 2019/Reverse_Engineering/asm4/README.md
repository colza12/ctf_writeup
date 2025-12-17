# asm4 : Reverse Engineering

What will asm4("picoCTF_95473") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)

Author : Sanjay C

# Solution

Check the source code.
```S
asm4:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	push   ebx
	<+4>:	sub    esp,0x10
	<+7>:	mov    DWORD PTR [ebp-0x10],0x246
	<+14>:	mov    DWORD PTR [ebp-0xc],0x0
	<+21>:	jmp    0x518 <asm4+27>
	<+23>:	add    DWORD PTR [ebp-0xc],0x1
	<+27>:	mov    edx,DWORD PTR [ebp-0xc]
	<+30>:	mov    eax,DWORD PTR [ebp+0x8]
	<+33>:	add    eax,edx
	<+35>:	movzx  eax,BYTE PTR [eax]
	<+38>:	test   al,al
	<+40>:	jne    0x514 <asm4+23>
	<+42>:	mov    DWORD PTR [ebp-0x8],0x1
	<+49>:	jmp    0x587 <asm4+138>
	<+51>:	mov    edx,DWORD PTR [ebp-0x8]
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,edx
	<+59>:	movzx  eax,BYTE PTR [eax]
	<+62>:	movsx  edx,al
	<+65>:	mov    eax,DWORD PTR [ebp-0x8]
	<+68>:	lea    ecx,[eax-0x1]
	<+71>:	mov    eax,DWORD PTR [ebp+0x8]
	<+74>:	add    eax,ecx
	<+76>:	movzx  eax,BYTE PTR [eax]
	<+79>:	movsx  eax,al
	<+82>:	sub    edx,eax
	<+84>:	mov    eax,edx
	<+86>:	mov    edx,eax
	<+88>:	mov    eax,DWORD PTR [ebp-0x10]
	<+91>:	lea    ebx,[edx+eax*1]
	<+94>:	mov    eax,DWORD PTR [ebp-0x8]
	<+97>:	lea    edx,[eax+0x1]
	<+100>:	mov    eax,DWORD PTR [ebp+0x8]
	<+103>:	add    eax,edx
	<+105>:	movzx  eax,BYTE PTR [eax]
	<+108>:	movsx  edx,al
	<+111>:	mov    ecx,DWORD PTR [ebp-0x8]
	<+114>:	mov    eax,DWORD PTR [ebp+0x8]
	<+117>:	add    eax,ecx
	<+119>:	movzx  eax,BYTE PTR [eax]
	<+122>:	movsx  eax,al
	<+125>:	sub    edx,eax
	<+127>:	mov    eax,edx
	<+129>:	add    eax,ebx
	<+131>:	mov    DWORD PTR [ebp-0x10],eax
	<+134>:	add    DWORD PTR [ebp-0x8],0x1
	<+138>:	mov    eax,DWORD PTR [ebp-0xc]
	<+141>:	sub    eax,0x1
	<+144>:	cmp    DWORD PTR [ebp-0x8],eax
	<+147>:	jl     0x530 <asm4+51>
	<+149>:	mov    eax,DWORD PTR [ebp-0x10]
	<+152>:	add    esp,0x10
	<+155>:	pop    ebx
	<+156>:	pop    ebp
	<+157>:	ret    
```
Pass the string "picoCTF_a3112" as an argument.  
At <+7>, 0x246 is stored at ebp-0x10, and at <+14>, 0x0 is stored at ebp-0xc.  
The unconditional jump at <+21> jumps to <+27>.  
At <+27>, edx is set to 0x0, at <+30>, eax is loaded with ebp+0x8, which is a pointer to "picoCTF_a3112", and at <+33>, eax is incremented by edx, so eax points to the start of "picoCTF_a3112".  
At <+35>, 1 byte is loaded from eax into p with zero-extension.  
The test and jne instructions at <+38> and <+49> meet the condition, so execution jumps to <+23>.  
At <+23>, 0x1 is added to ebp-0xc, making ebp-0xc = 0x1.  
From <+27> onward, the process repeats similarly, and when the test and jne instructions at <+38> and <+40> no longer meet the condition, it means all characters have been processed, with ebp-0xc incremented for each character, reaching 0xd.  

At <+42>, 0x1 is stored in ebp-0x8, and the unconditional jump at <+49> jumps to <+138>.
At <+138>, ebp-0xc is moved into eax, so eax = 0xd.
At <+141>, 0x1 is subtracted from eax, resulting in eax = 0xc.
At <+144>, ebp-0x8 is compared with eax, and since the jl at <+147> condition is met, execution jumps to <+51>.

At <+51>, edx is loaded with ebp-0x8, at <+54>, eax is loaded with ebp+0x8 (pointer to "picoCTF_a3112"), and at <+57>, eax is incremented by edx, so eax points to the second character, 'i', of "picoCTF_a3112".  
At <+59>, 1 byte is loaded from eax into i with zero-extension, and at <+62>, al is sign-extended into edx, so edx = 0x00000069.  
At <+65>, ebp-0x8 is loaded into eax, and at <+68>, eax - 0x1 is stored in ecx, so ecx = 0x0.  
At <+71>, <+74>, and <+76>, the first character 'p' (0x70) of "picoCTF_a3112" is zero-extended into eax, and at <+79>, al is sign-extended into eax, so eax = 0x00000070.  
At <+82>, eax is subtracted from edx, giving 0x69 - 0x70 = -0x7.  
At <+84> and <+86>, edx and eax both contain -0x7.  
At <+88>, eax is loaded with ebp-0x10, so eax = 0x246.  
At <+91>, ebx is set to edx + eax1, so ebx = -0x7 + 0x246 = 0x23f.  
At <+94>, eax is loaded with ebp-0x8, so eax = 0x1.  
At <+97>, edx is set to eax + 0x1, so edx = 0x2.  
At <+100>, <+103>, and <+105>, the third character 'c' (0x63) of "picoCTF_a3112" is zero-extended into eax, and at <+108>, al is sign-extended into edx, so edx = 0x00000063.  
At <+111>, ecx is set to ebp-0x8 - 0x1, and at <+114>, eax is loaded with ebp+0x8 (pointer to "picoCTF_a3112"), then at <+117>, eax is incremented by ecx, so eax points to the second character 'i'.  
At <+119>, 1 byte is loaded from eax into i with zero-extension, and at <+122>, al is sign-extended into eax, so eax = 0x00000069.  
At <+125>, edx - eax is calculated, giving 0x63 - 0x69 = -0x6.  
At <+127>, eax is set to edx = -0x6.  
At <+129>, eax is added to ebx, giving -0x6 + 0x23f = 0x239.  
At <+131>, ebp-0x10 is updated with eax = 0x239.  
At <+134>, 0x1 is added to ebp-0x8, so ebp-0x8 = 0x2.  
At <+138>, ebp-0xc is loaded into eax = 0xd.  
At <+141>, 0x1 is subtracted, giving eax = 0xc.  
At <+144>, ebp-0x8 is compared with eax, and the jl at <+147> is still true, so execution jumps back to <+51>.  
This process repeats, and eventually the cmp at <+144> and jl at <+147> no longer meet the condition, meaning the loop has iterated (number of characters - 2) times.

The operation here is: `(ebp-0x10) = (arg1[i] - arg1[i-1]) + (arg1[i+1] - arg1[i]) + (ebp-0x10)`,
which simplifies to `(ebp-0x10) = (arg1[i+1] - arg1[i-1]) + (ebp-0x10)`, repeated for i = 1 to 11.

The initial value of ebp-0x10 is 0x246, and iterating i from 1 to 11 gives:
```
(ebp-0x10) + arg1[2] - arg1[0] + arg1[3] - arg1[1] + arg1[4] - arg1[2] + arg1[5] - arg1[3] … 
= (ebp-0x10) - arg1[0] - arg1[1] + arg1[11] + arg1[12]
```
Thus, the final value of ebp-0x10 is:
```
0x246 - 0x70 - 0x69 + 0x31 + 0x32 = 0x1d0
```

Got the flag!

`0x1d0`
