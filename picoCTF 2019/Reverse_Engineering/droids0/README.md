# droids0 : Reverse Engineering

Where do droid logs go. Check out this [file](zero.apk).

Author : Jason

# Solution

For now, try running it on the Android Studio's emulator.  
The version used was Medium Phone API 36.1.  
After starting the emulator, drag and drop zero.apk to install it.  
When opening the installed app, the following screen is displayed.  
![display](image/image1.png)

Since it says "where else can output go?", display the log.  
Open Logcat in Android Studio and apply a filter for `picoCTF`.

Press the obviously suspicious button.  
![Logcat](image/image2.png)

Got the flag!

`picoCTF{a.moose.once.bit.my.sister}`
