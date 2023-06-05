#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    num = 0

    for arg in args:
        num += int(arg)

    print(num)
