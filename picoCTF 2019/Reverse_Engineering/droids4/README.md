# droids4 : Reverse Engineering

Reverse the pass, patch the file, get the flag. Check out this [file](four.apk).

Author : Jason

# Solution

As before, open four.apk in the Android Studio emulator.  
![display](image/image1.png)

It says "you got this," and there are no hints.  
Therefore, after decompiling the file with apktool, check FlagstaffHill.smali.
```
$ apktool d four.apk 
I: Using Apktool 2.7.0-dirty on four.apk
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
FlaggstaffHill.smali was as follows:
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

.method public static native cardamom(Ljava/lang/String;)Ljava/lang/String;
.end method

.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 8
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 12
    new-instance v0, Ljava/lang/StringBuilder;

    const-string v1, "aaa"

    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    .line 13
    .local v0, "ace":Ljava/lang/StringBuilder;
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    .line 14
    .local v2, "jack":Ljava/lang/StringBuilder;
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    .line 15
    .local v3, "queen":Ljava/lang/StringBuilder;
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4, v1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    move-object v1, v4

    .line 17
    .local v1, "king":Ljava/lang/StringBuilder;
    const/4 v4, 0x0

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v5

    add-int/lit8 v5, v5, 0x4

    int-to-char v5, v5

    invoke-virtual {v0, v4, v5}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 18
    const/4 v5, 0x1

    invoke-virtual {v0, v5}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v6

    add-int/lit8 v6, v6, 0x13

    int-to-char v6, v6

    invoke-virtual {v0, v5, v6}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 19
    const/4 v6, 0x2

    invoke-virtual {v0, v6}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/lit8 v7, v7, 0x12

    int-to-char v7, v7

    invoke-virtual {v0, v6, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 21
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/lit8 v7, v7, 0x7

    int-to-char v7, v7

    invoke-virtual {v2, v4, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 22
    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/2addr v7, v4

    int-to-char v7, v7

    invoke-virtual {v2, v5, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 23
    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/2addr v7, v5

    int-to-char v7, v7

    invoke-virtual {v2, v6, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 25
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/2addr v7, v4

    int-to-char v7, v7

    invoke-virtual {v3, v4, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 26
    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/lit8 v7, v7, 0xb

    int-to-char v7, v7

    invoke-virtual {v3, v5, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 27
    invoke-virtual {v3, v6}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/lit8 v7, v7, 0xf

    int-to-char v7, v7

    invoke-virtual {v3, v6, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 29
    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v7

    add-int/lit8 v7, v7, 0xe

    int-to-char v7, v7

    invoke-virtual {v1, v4, v7}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 30
    invoke-virtual {v1, v5}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v4

    add-int/lit8 v4, v4, 0x14

    int-to-char v4, v4

    invoke-virtual {v1, v5, v4}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 31
    invoke-virtual {v1, v6}, Ljava/lang/StringBuilder;->charAt(I)C

    move-result v4

    add-int/lit8 v4, v4, 0xf

    int-to-char v4, v4

    invoke-virtual {v1, v6, v4}, Ljava/lang/StringBuilder;->setCharAt(IC)V

    .line 33
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    const-string v5, ""

    invoke-virtual {v5, v4}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v4

    .line 34
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v4

    .line 36
    .local v4, "password":Ljava/lang/String;
    invoke-virtual {p0, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v5

    if-eqz v5, :cond_0

    const-string v5, "call it"

    return-object v5

    .line 37
    :cond_0
    const-string v5, "NOPE"

    return-object v5
.end method
```
The getFlag function checks whether the input string matches the password.

In lines 12 to 17, the string "aaa" is first assigned to the four variables `ace`, `jack`, `queen`, and `king` using a StringBuilder.  
After that, up to line 19, the following processing is performed, resulting in `ace = ets`.
```
ace[0] = ace[0] + 0x4
ace[1] = ace[1] + 0x13
ace[2] = ace[2] + 0x12
```
In lines 21 to 23, the following processing is performed, resulting in `jack = hab`.
```
jack[0] = jack[0] + 0x7
jack[1] = jack[1] + 0x0
jack[2] = jack[2] + 0x1
```
In lines 25 to 27, the following processing is performed, resulting in `queen = alp`.
```
queen[0] = queen[0] + 0x0
queen[1] = queen[1] + 0xb
queen[2] = queen[2] + 0xf
```
In lines 29 to 31, the following processing is performed, resulting in `king = oup`.
```
king[0] = king[0] + 0xe
king[1] = king[1] + 0x14
king[2] = king[2] + 0xf
```
In lines 33 to 36, a string is created by concatenating `queen` + `jack` + `ace` + `king`, and this is assigned to password.
Therefore, `password = alphabetsoup`.

Enter `alphabetsoup` into the app running on the emulator, and press the button.  
![password](image/image2.png)

"Call it" was displayed, confirming that the password was correct.  
The part of the code that displays "call it" needs to be modified to call the flag output function instead.  
Since `cardamom` is the only mysterious function besides getFlag, the next step is to analyze the cardamom function.

Search for the file where the cardamom function is implemented.
```
$ grep -R "cardamom" four/
grep: four/lib/arm64-v8a/libhellojni.so: binary file matches
grep: four/lib/armeabi-v7a/libhellojni.so: binary file matches
grep: four/lib/x86/libhellojni.so: binary file matches
grep: four/lib/x86_64/libhellojni.so: binary file matches
four/smali/com/hellocmu/picoctf/FlagstaffHill.smali:.method public static native cardamom(Ljava/lang/String;)Ljava/lang/String;
```
It seems that it is likely implemented in the `libhellojni.so` file, so I will check it using Ghidra.  
This time, I used `four/lib/x86_64/libhellojni.so`.

Search for a function name containing the string `cardamom` in the Symbol Tree.
```c
undefined8
Java_com_hellocmu_picoctf_FlagstaffHill_cardamom
          (long *param_1,undefined8 param_2,undefined8 param_3)

{
  byte bVar1;
  undefined8 uVar2;
  char *local_50;
  
  uVar2 = (**(code **)(*param_1 + 0x548))(param_1,param_3,0);
  bVar1 = chervil(uVar2);
  (**(code **)(*param_1 + 0x550))(param_1,param_3,uVar2);
  if ((bVar1 & 1) == 0) {
    local_50 = "try again";
  }
  else {
    local_50 = (char *)pepper(uVar2);
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
The chervil function checks whether the input characters match the reference.  
Subsequently, it can be seen that the pepper function is being called.
```c
void pepper(char *param_1)

{
  char *pcVar1;
  size_t sVar2;
  
  pcVar1 = strdup(param_1);
  sVar2 = strlen(param_1);
  unscramble(&DAT_00101aa0,0x1f,pcVar1,sVar2 & 0xffffffff);
  return;
}
```
It can be seen that some operation is performed using the input string. It is likely that `DAT_00101aa0` is being decrypted using the input string.  
The unscramble function is the same as in droids3, so the decryption code could be reused as is. However, this time, the flag will be output by modifying FlagstaffHill.smali.  
The modifications are as follows:
```smali
# Before rewriting
# const-string v5, "call it"

# return-object v5

# After rewriting
invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;

move-result-object v0

return-object v0
```
Rebuild this and launch it on the emulator.  
An error occurred during the build, so `$ic_launcher_foreground__0.xml` and the code referencing it were deleted.
```
$ apktool b four_edited --use-aapt2 -o four_edited.apk
I: Using Apktool 2.7.0-dirty
I: Checking whether sources has changed...
I: Checking whether resources has changed...
I: Building resources...
W: aapt: brut.common.BrutException: brut.common.BrutException: Could not extract resource: /prebuilt/linux/aapt2_64 (defaulting to $PATH binary)
I: Copying libs... (/lib)
I: Building apk file...
I: Copying unknown files/dir...
I: Built apk into: four_edited.apk
```
The file built with apktool is unsigned, so it needs to be signed.
```
$ wget https://github.com/patrickfav/uber-apk-signer/releases/download/v1.3.0/uber-apk-signer-1.3.0.jar
$ java -jar uber-apk-signer-1.3.0.jar --apk four_edited.apk
```
Install the rebuilt apk file on the emulator and launch the app.  
Enter `alphabetsoup` and press the button.  
![flag](image/image3.png)

Got the flag!

`picoCTF{not.particularly.silly}`
