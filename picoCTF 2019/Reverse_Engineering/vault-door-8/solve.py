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
