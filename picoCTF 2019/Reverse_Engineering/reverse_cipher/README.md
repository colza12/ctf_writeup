# reverse_cipher : Reverse Engineering

We have recovered a [binary](rev) and a [text file](rev_this). Can you reverse the flag.

Author : Danny Tunitis

# Solution

Decompile rev.
```c
void main(void)

{
  size_t sVar1;
  char local_58 [23];
  char local_41;
  int local_2c;
  FILE *local_28;
  FILE *local_20;
  uint local_14;
  int local_10;
  char local_9;
  
  local_20 = fopen("flag.txt","r");
  local_28 = fopen("rev_this","a");
  if (local_20 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (local_28 == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(local_58,0x18,1,local_20);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (local_10 = 0; local_10 < 8; local_10 = local_10 + 1) {
    local_9 = local_58[local_10];
    fputc((int)local_9,local_28);
  }
  for (local_14 = 8; (int)local_14 < 0x17; local_14 = local_14 + 1) {
    if ((local_14 & 1) == 0) {
      local_9 = local_58[(int)local_14] + '\x05';
    }
    else {
      local_9 = local_58[(int)local_14] + -2;
    }
    fputc((int)local_9,local_28);
  }
  local_9 = local_41;
  fputc((int)local_41,local_28);
  fclose(local_28);
  fclose(local_20);
  return;
}
```
The program reads a string from flag.txt. The first 8 characters are left unchanged, while the remaining characters are modified: even-indexed characters are incremented by 0x5, and odd-indexed characters are decremented by 0x2.  The last character is obtained from a different source.  
After these operations, the string written into rev_this is `picoCTF{w1{1wq85jc=2i0<}`.

To recover the original characters from flag.txt, reverse the transformation.  
For characters from the 9th onward, subtract 0x5 from even-indexed characters and add 0x2 to odd-indexed characters.

Got the flag!

`picoCTF{r3v3rs37ee84d27}`
