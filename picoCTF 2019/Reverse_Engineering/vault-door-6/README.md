# vault-door-6 : Reverse Engineering

This vault uses an XOR encryption scheme.  
The source code for this vault is here: [VaultDoor6.java](VaultDoor6.java)

Author : Mark E. Haase

# Solution

Check the source code.
```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
```
It XORs the standard input with `0x55` and checks whether it matches `0x3b 0x65 0x21 0x0a 0x38 0x00 0x36 0x1d 0x0a 0x3d 0x61 0x27 0x11 0x66 0x27 0x0a 0x21 0x1d 0x61 0x3b 0x0a 0x2d 0x65 0x27 0x0a 0x6c 0x61 0x6d 0x37 0x6d 0x6d 0x6d`.

Since XORing with the same value restores the original data, XOR `0x3b 0x65 0x21 0x0a 0x38 0x00 0x36 0x1d 0x0a 0x3d 0x61 0x27 0x11 0x66 0x27 0x0a 0x21 0x1d 0x61 0x3b 0x0a 0x2d 0x65 0x27 0x0a 0x6c 0x61 0x6d 0x37 0x6d 0x6d 0x6d` with `0x55` in CyberChef, then add `picoCTF{` at the beginning and `}` at the end.

Got the flag!

`picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}`
