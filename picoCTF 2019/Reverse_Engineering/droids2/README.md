# droids2 : Reverse Engineering

Find the pass, get the flag. Check out this [file](two.apk).

Author : Jason

# Solution

Since it is the same challenge statement as droids1, find the flag using the same procedure.  
Open two.apk in the Android Studio emulator.  
![display](image/image1.png)

Since it says "smali sounds like an IKEA bookcase," check the smali files.  
```
$ apktool d two.apk 
I: Using Apktool 2.7.0-dirty on two.apk
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
Search for files in the smali folder that contain the string "pass".
```
$ grep -R "pass" two/smali/
two/smali/androidx/constraintlayout/solver/Metrics.smali:    const-string v1, "\nresolutions passes: "
two/smali/androidx/constraintlayout/widget/ConstraintLayout.smali:    const-string v3, "First pass"
two/smali/androidx/constraintlayout/widget/ConstraintLayout.smali:    const-string v1, "2nd pass"
two/smali/androidx/constraintlayout/widget/ConstraintLayout.smali:    const-string v1, "3rd pass"
two/smali/androidx/core/text/util/FindAddress.smali:    const-string v0, "(?:alley|annex|arcade|ave[.]?|avenue|alameda|bayou|beach|bend|bluffs?|bottom|boulevard|branch|bridge|brooks?|burgs?|bypass|broadway|camino|camp|canyon|cape|causeway|centers?|circles?|cliffs?|club|common|corners?|course|courts?|coves?|creek|crescent|crest|crossing|crossroad|curve|circulo|dale|dam|divide|drives?|estates?|expressway|extensions?|falls?|ferry|fields?|flats?|fords?|forest|forges?|forks?|fort|freeway|gardens?|gateway|glens?|greens?|groves?|harbors?|haven|heights|highway|hills?|hollow|inlet|islands?|isle|junctions?|keys?|knolls?|lakes?|land|landing|lane|lights?|loaf|locks?|lodge|loop|mall|manors?|meadows?|mews|mills?|mission|motorway|mount|mountains?|neck|orchard|oval|overpass|parks?|parkways?|pass|passage|path|pike|pines?|plains?|plaza|points?|ports?|prairie|privada|radial|ramp|ranch|rapids?|rd[.]?|rest|ridges?|river|roads?|route|row|rue|run|shoals?|shores?|skyway|springs?|spurs?|squares?|station|stravenue|stream|st[.]?|streets?|summit|speedway|terrace|throughway|trace|track|trafficway|trail|tunnel|turnpike|underpass|unions?|valleys?|viaduct|views?|villages?|ville|vista|walks?|wall|ways?|wells?|xing|xrd)(?=[,*\u2022\t \u00a0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000\n\u000b\u000c\r\u0085\u2028\u2029]|$)"
two/smali/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.smali:    .param p1, "password"    # Z
two/smali/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.smali:    const-string v2, "; password: "
two/smali/com/hellocmu/picoctf/FlagstaffHill.smali:    .local v7, "password":Ljava/lang/String;
```
`"password":Ljava/lang/String` in `two/smali/com/hellocmu/picoctf/FlagstaffHill.smali` looks suspicious, so check the contents of the file.
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

.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 10
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 11
    const/4 v0, 0x6

    new-array v0, v0, [Ljava/lang/String;

    .line 12
    .local v0, "witches":[Ljava/lang/String;
    const/4 v1, 0x0

    const-string v2, "weatherwax"

    aput-object v2, v0, v1

    .line 13
    const/4 v1, 0x1

    const-string v2, "ogg"

    aput-object v2, v0, v1

    .line 14
    const/4 v1, 0x2

    const-string v2, "garlick"

    aput-object v2, v0, v1

    .line 15
    const/4 v1, 0x3

    const-string v2, "nitt"

    aput-object v2, v0, v1

    .line 16
    const/4 v1, 0x4

    const-string v2, "aching"

    aput-object v2, v0, v1

    .line 17
    const/4 v1, 0x5

    const-string v2, "dismass"

    aput-object v2, v0, v1

    .line 19
    const/4 v1, 0x3

    .line 20
    .local v1, "first":I
    sub-int v2, v1, v1

    .line 21
    .local v2, "second":I
    div-int v3, v1, v1

    add-int/2addr v3, v2

    .line 22
    .local v3, "third":I
    add-int v4, v3, v3

    sub-int/2addr v4, v2

    .line 23
    .local v4, "fourth":I
    add-int v5, v1, v4

    .line 24
    .local v5, "fifth":I
    add-int v6, v5, v2

    sub-int/2addr v6, v3

    .line 26
    .local v6, "sixth":I
    aget-object v7, v0, v5

    .line 27
    const-string v8, ""

    invoke-virtual {v8, v7}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    const-string v8, "."

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v3

    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v2

    .line 28
    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v6

    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v9, v0, v1

    .line 29
    invoke-virtual {v7, v9}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    aget-object v8, v0, v4

    invoke-virtual {v7, v8}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    .line 32
    .local v7, "password":Ljava/lang/String;
    invoke-virtual {p0, v7}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v8

    if-eqz v8, :cond_0

    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->sesame(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v8

    return-object v8

    .line 33
    :cond_0
    const-string v8, "NOPE"

    return-object v8
.end method

.method public static native sesame(Ljava/lang/String;)Ljava/lang/String;
.end method
```
From line 32 onward, the input is compared with the password, and if they match, the `sesame` method is called and the flag is returned.
In lines 11–17, the `witches` array is created and six strings are stored in it.
```python
witches = {
  "weatherwax",
  "ogg",
  "garlick",
  "nitt",
  "aching",
  "dismass"
}
```
In lines 19–26, the index for the `witches` array is calculated.
```python
first  = 3
second = first - first = 0
third  = first / first + second = 1
fourth = third + third - second = 2
fifth  = first + fourth = 3 + 2 = 5
sixth  = fifth + second - third = 5 + 0 - 1 = 4
```
From line 26 onward, the elements of the `witches` array corresponding to the calculated indices are concatenated using `.` with `aget-object`.
```python
witches[fifth]
witches[third]
withces[second]
witches[sixth]
witches[first]
witches[forth]
```
Rearrange the strings in the `witches` array in this order to construct the pass.  
`dismass.ogg.weatherwax.aching.nitt.garlick`

Enter `dismass.ogg.weatherwax.aching.nitt.garlick` into the app running on the emulator and press the button.  
![pass](image/image2.png)

Got the flag!

`picoCTF{what.is.your.favourite.colour}`
