# vault-door-8 : Reverse Engineering

Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it.  
The source code for this vault is here: [VaultDoor8.java](VaultDoor8.java)

Author : Mark E. Haase

# Solution

Check the source code.
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*; import javax.crypto.Cipher; import javax.crypto.spec.SecretKeySpec;
import java.security.*; class VaultDoor8 {public static void main(String args[]) {
Scanner b = new Scanner(System.in); System.out.print("Enter vault password: ");
String c = b.next(); String f = c.substring(8,c.length()-1); VaultDoor8 a = new VaultDoor8(); if (a.checkPassword(f)) {System.out.println("Access granted."); }
else {System.out.println("Access denied!"); } } public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
char[] a = password.toCharArray(); for (int b=0; b<a.length; b++) {char c = a[b]; c = switchBits(c,1,2); c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ c = switchBits(c,5,6); c = switchBits(c,4,7);
c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ c = switchBits(c,3,4); c = switchBits(c,2,5); c = switchBits(c,6,7); a[b] = c; } return a;
} public char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit
that was in position p2 to position p1. Precondition: p1 < p2 */ char mask1 = (char)(1 << p1);
char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ char bit1 = (char)(c & mask1); char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ char rest = (char)(c & ~(mask1 | mask2)); char shift = (char)(p2 - p1); char result = (char)((bit1<<shift) | (bit2>>shift) | rest); return result;
} public boolean checkPassword(String password) {char[] scrambled = scramble(password); char[] expected = {
0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 }; return Arrays.equals(scrambled, expected); } }
```
For ease of reading, insert line breaks and so forth.
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;
class VaultDoor8 {public static void main(String args[]) {
    Scanner b = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String c = b.next();
    String f = c.substring(8,c.length()-1);
    VaultDoor8 a = new VaultDoor8();
    if (a.checkPassword(f)) {
        System.out.println("Access granted.");
    }
    else {
        System.out.println("Access denied!");
    }
}

public char[] scramble(String password) {
    /* Scramble a password by transposing pairs of bits. */
    char[] a = password.toCharArray();
    for (int b=0; b<a.length; b++) {
        char c = a[b];
        c = switchBits(c,1,2);
        c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
        c = switchBits(c,5,6);
        c = switchBits(c,4,7);
        c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
        c = switchBits(c,3,4);
        c = switchBits(c,2,5);
        c = switchBits(c,6,7);
        a[b] = c;
    }
    return a;
}

public char switchBits(char c, int p1, int p2) {
    /* Move the bit in position p1 to position p2, and move the bit that was in position p2 to position p1. Precondition: p1 < p2 */
    char mask1 = (char)(1 << p1);
    char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
    char bit1 = (char)(c & mask1);
    char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1)); System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
    char rest = (char)(c & ~(mask1 | mask2));
    char shift = (char)(p2 - p1);
    char result = (char)((bit1<<shift) | (bit2>>shift) | rest);
    return result;
}

public boolean checkPassword(String password) {
    char[] scrambled = scramble(password);
    char[] expected = {
        0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 
        0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 
        0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 
        0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
        };
    return Arrays.equals(scrambled, expected);
}
```
Perform repeated bitwise operations on 32 characters using the switchBits function, yielding `0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0` matches the password.

Assuming c = 10101010, executing switchBits(c, 1, 2) yields the result 10101100, revealing that the first and second bits from the right have been swapped.  
It is thus determined that the switchBits function swaps the p1th and p2th bits from the right of c.  
To trace the processing of the `scramble` function, assuming that the final value is `c = 76543210` and working backward, the result is `32761054`.

Keep the processing of the `switchBits` function unchanged, and reverse the processing of `scramble` to work backward and calculate the inverse of `expected`.

Execution code below:
```python
expected = [
        0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 
        0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 
        0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 
        0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
        ]

def switchBits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = (bit1<<shift) | (bit2>>shift) | rest
    return result

def scramble(expected):
    password = ""
    for c in expected:
        c = switchBits(c,6,7)
        c = switchBits(c,2,5)
        c = switchBits(c,3,4)
        c = switchBits(c,0,1)
        c = switchBits(c,4,7)
        c = switchBits(c,5,6)
        c = switchBits(c,0,3)
        c = switchBits(c,1,2)
        password += chr(c)
    print(password)

scramble(expected)
```
Execute it.
```
$ python3 solve.py
s0m3_m0r3_b1t_sh1fTiNg_91c642112
```
Add `picoCTF{` at the beginning and `}` at the end.

Got the flag!

`picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}`
