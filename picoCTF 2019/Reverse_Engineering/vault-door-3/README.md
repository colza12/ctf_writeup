# vault-door-3 : Reverse Engineering

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](VaultDorr3.java)

Author : Mark E. Haase

# Solution

Check the source code.
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}
```
It rearranges the standard input using a for loop and checks whether it matches "jU5t_a_sna_3lpm18g947_u_4_m9r54f".

The reordering process is as follows:
* 0–7: 8 characters starting from the 0th character in order
* 8–15: 8 characters starting from the 15th character in reverse order
* Even indices from 16 onward: 8 characters taken from the 30th character backward, using even positions
* Odd indices from 17 onward: 8 characters taken from the 17th character forward, using odd positions

Following this procedure, find a string that, when reordered, becomes "jU5t_a_sna_3lpm18g947_u_4_m9r54f", and then add `picoCTF{` at the beginning and `}` at the end.

Got the flag!

`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}`
