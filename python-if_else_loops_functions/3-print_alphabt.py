#!/usr/bin/python3
alphabet = range(97, 123)
for letter in alphabet:
    if letter == 113 or letter  == 101:
        continue
    else:
        print('{0:c}'.format(letter), end='')
