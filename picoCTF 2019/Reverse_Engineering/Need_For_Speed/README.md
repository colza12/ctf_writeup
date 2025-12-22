# Need For Speed : Reverse Engineering

The name of the game is speed. Are you quick enough to solve this problem and keep it above 50 mph?  
[need-for-speed](need-for-speed)

Author : Alexander Bushkin

# Solution

Decompile the file using Ghidra.
```c
undefined4 calculate_key(void)

{
  int local_c;
  
  local_c = -0x42e78026;
  do {
    local_c = local_c + -1;
  } while (local_c != -0x2173c013);
  return 0xde8c3fed;
}


void decrypt_flag(int param_1)

{
  int local_1c;
  uint local_c;
  
  local_1c = param_1;
  for (local_c = 0; local_c < 0x37; local_c = local_c + 1) {
    flag[(int)local_c] = flag[(int)local_c] ^ *(byte *)((long)&local_1c + (long)((int)local_c % 2) );
    if ((int)local_c % 3 == 2) {
      local_1c = local_1c + 1;
    }
  }
  return;
}
```
key = 0xde8c3fed
flag = 0xbd76ae70ad6ba944a8509f5bd1559e5dd254965a83569a58d55d804cd61cc75e9108cf06cd0ed94c8a5a9e5b92519b1f9c539251991e8200

When the counter is even, the flag is XORed with the least significant byte of the key, and when it is odd, it is XORed with the second least significant byte of the key. Additionally, the key is incremented every time three bytes are processed.

Executing this should yield the flag.

Execution code below:
```python solve.py
key = 0xde8c3fed
flag = [0xbd, 0x76, 0xae, 0x70, 0xad, 0x6b, 0xa9, 0x44, 0xa8, 0x50, 0x9f, 0x5b, 0xd1, 0x55, 0x9e, 0x5d, 0xd2, 0x54, 0x96, 0x5a, 0x83, 0x56, 0x9a, 0x58, 0xd5, 0x5d, 0x80, 0x4c, 0xd6, 0x1c, 0xc7, 0x5e, 0x91, 0x08, 0xcf, 0x06, 0xcd, 0x0e, 0xd9, 0x4c, 0x8a, 0x5a, 0x9e, 0x5b, 0x92, 0x51, 0x9b, 0x1f, 0x9c, 0x53, 0x92, 0x51, 0x99, 0x1e, 0x82, 0x00]

for i in range(55):
    key_list = [(key >> (8 * j)) & 0xFF for j in range(4)]
    flag[i] = flag[i] ^ key_list[i % 2]
    if (i % 3) == 2:
        key = key + 1
flag_decrypted = ''.join(chr(b) for b in flag)
print(flag_decrypted)
```
Execute it.
```
$ python3 need-solve.py
PICOCTF{Good job keeping bus #0af77941 speeding along!}
```

Got the flag!

`PICOCTF{Good job keeping bus #0af77941 speeding along!}`
