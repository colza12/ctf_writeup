# droids3 : Reverse Engineering

Find the pass, get the flag. Check out this [file](three.apk).

Author : Jason

# Solution

Open three.apk in the Android Studio emulator.  
![display](image/image1.png)

It says "Make this app your own," and there are almost no hints.  
Following the same procedure as before, locate the FlagstaffHill.smali file and check its contents.  
```
$ apktool d three.apk 
I: Using Apktool 2.7.0-dirty on three.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /home/colza/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
Open the file located at `three/smali/com/hellocmu/FlagstaffHill.smali`.
```smali FlagstaffHill.smali
.class public Lcom/hellocmu/picoctf/FlagstaffHill;
.super Ljava/lang/Object;
.source "FlagstaffHill.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static native cilantro(Ljava/lang/String;)Ljava/lang/String;
.end method

.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 19
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->nope(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    .line 20
    .local v0, "flag":Ljava/lang/String;
    return-object v0
.end method

.method public static nope(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 11
    const-string v0, "don\'t wanna"

    return-object v0
.end method

.method public static yep(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 15
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cilantro(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method
```
Among the functions being called, the one of interest is `cilantro`, which is implemented in native code as part of an external library.
```smali
.method public static native cilantro(Ljava/lang/String;)Ljava/lang/String;
.end method
```
Search for the file where the `cilantro` function is implemented.
```
$ grep -R "cilantro" three/
grep: three/lib/arm64-v8a/libhellojni.so: binary file matches
grep: three/lib/armeabi-v7a/libhellojni.so: binary file matches
grep: three/lib/x86/libhellojni.so: binary file matches
grep: three/lib/x86_64/libhellojni.so: binary file matches
three/smali/com/hellocmu/picoctf/FlagstaffHill.smali:.method public static native cilantro(Ljava/lang/String;)Ljava/lang/String;
three/smali/com/hellocmu/picoctf/FlagstaffHill.smali:    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cilantro(Ljava/lang/String;)Ljava/lang/String;
```
It seems that it is likely implemented in the `libhellojni.so` file, so I will check it using Ghidra.  
This time, I used `three/lib/x86_64/libhellojni.so`.

Search for a function name containing the string `cilantro` in the Symbol Tree.
```c
undefined8
Java_com_hellocmu_picoctf_FlagstaffHill_cilantro
          (long *param_1,undefined8 param_2,undefined8 param_3)

{
  byte bVar1;
  undefined8 uVar2;
  char *local_50;
  
  uVar2 = (**(code **)(*param_1 + 0x548))(param_1,param_3,0);
  bVar1 = dill(uVar2);
  (**(code **)(*param_1 + 0x550))(param_1,param_3,uVar2);
  if ((bVar1 & 1) == 0) {
    local_50 = "try again";
  }
  else {
    local_50 = (char *)sumac();
  }
  uVar2 = (**(code **)(*param_1 + 0x538))(param_1,local_50);
  free(local_50);
  return uVar2;
}
```
param_3 is likely a String argument passed from Java, and in the following part, the string from param3 is retrieved and the pointer is assigned to uVar2.
```c
uVar2 = (**(code **)(*param_1 + 0x548))(param_1,param_3,0);
```
The dill function checks whether the input characters match the reference.  
Subsequently, it can be seen that the sumac function is being called.
```c
void sumac(void)

{
  char *pcVar1;
  size_t sVar2;
  
  pcVar1 = strdup("againmissing");
  sVar2 = strlen("againmissing");
  unscramble(&DAT_00101a85,0x1a,pcVar1,sVar2 & 0xffffffff);
  return;
}
```
DAT_00101a85 was as follows:
```
        00101a85 11              ??         11h
        00101a86 0e              ??         0Eh
        00101a87 02              ??         02h
        00101a88 06              ??         06h
        00101a89 2d              ??         2Dh    -
        00101a8a 39              ??         39h    9
        00101a8b 2f              ??         2Fh    /
        00101a8c 08              ??         08h
        00101a8d 07              ??         07h
        00101a8e 00              ??         00h
        00101a8f 1d              ??         1Dh
        00101a90 49              ??         49h    I
        00101a91 03              ??         03h
        00101a92 12              ??         12h
        00101a93 15              ??         15h
        00101a94 47              ??         47h    G
        00101a95 0f              ??         0Fh
        00101a96 43              ??         43h    C
        00101a97 1a              ??         1Ah
        00101a98 10              ??         10h
        00101a99 01              ??         01h
        00101a9a 08              ??         08h
        00101a9b 1a              ??         1Ah
        00101a9c 04              ??         04h
        00101a9d 09              ??         09h
        00101a9e 1a              ??         1Ah
        00101a9f 00              ??         00h
```
The main operations seem to be written in the unscramble function.
```c
void * unscramble(long param_1,int param_2,long param_3,int param_4)

{
  void *pvVar1;
  int local_38;
  int local_34;
  
  pvVar1 = calloc((long)param_2,1);
  local_38 = 0;
  for (local_34 = 0; local_34 < param_2; local_34 = local_34 + 1) {
    *(byte *)((long)pvVar1 + (long)local_34) =
         *(byte *)(param_1 + local_34) ^ *(byte *)(param_3 + local_38 % param_4);
    local_38 = local_38 + 1;
  }
  return pvVar1;
}
```
A memory area of 0x1a bytes is allocated using calloc, and a for loop is used to store the calculation results from index 0.  
The calculation involves XORing the 0th element of param1 with the remainder of the 0th element of param3 divided by the 12 characters of "againmissing".  
In other words, the values in DAT_00101a85 are being XORed sequentially with "againmissing".

Since XORing with the same value twice restores the original value, the 26-byte data in DAT_00101a85 is XORed using the unscramble function.

Execution code below:
```python solve.py
from pwn import *
data = "110e02062d392f0807001d49031215470f431a1001081a04091a"
key = "againmissing"

data = bytes.fromhex(data)
flag = xor(data, key)

print(flag)
```
Execute it.
```
$ python3 solve.py 
/home/colza/.local/lib/python3.12/site-packages/pwnlib/util/fiddling.py:340: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  strs = [packing.flat(s, word_size = 8, sign = False, endianness = 'little') for s in args]
b'picoCTF{tis.but.a.scratch}'
```

Got the flag!

`picoCTF{tis.but.a.scratch}`
