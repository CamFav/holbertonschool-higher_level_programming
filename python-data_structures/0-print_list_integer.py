#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        my_list = [1, 2, 3, 4, 5]

    for num in my_list:
        print("{}".format(num))