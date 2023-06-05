#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    sentence = "arguments."
    if (len(args) > 1):
        sentence = "arguments:"
    elif (len(args) == 1):
        sentence = "argument:"

    print("{:} {:}".format(len(args), sentence))
    for arg in range(len(args)):
        print("{:}: {:}".format(arg + 1, args[arg]))
