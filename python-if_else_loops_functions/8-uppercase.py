#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        if char >= 97 and char <= 122:
            char = char - 32
        print("{0:c}".format(char), end="")
    print()
