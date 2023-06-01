#!/usr/bin/python3
def islower(c):
    c_char = ord(c)
    if c_char >= 97 and c_char <= 123:
        return True
    else:
        return False
