# droids1 : Reverse Engineering

Find the pass, get the flag. Check out this [file](one.apk).

Author : Jason

# Solution

This time, it seems we just need to find the pass.  
Open one.apk in the Android Studio emulator.  
![display](image/image1.png)

It looks like we can get the flag by entering the password here without using brute force.  
Decompile one.apk using apktool.
```
$ apktool d one.apk
I: Using Apktool 2.7.0-dirty on one.apk
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
When searching the output files for the string "pass", the string "password" is found in `strings.xml`.
```
<string name="password">opossum</string>
```
Enter `opossum` into the app running on the emulator and press the button.  
![opossum](image/image2.png)

Got the flag!

`picoCTF{pining.for.the.fjords}`
