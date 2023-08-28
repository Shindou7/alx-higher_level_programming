#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list = 0
    try:
        for n in my_list[:x]:
            print("{}".format(n), end="")
            list += 1
        print()
        return list
    except IndexError:
        print()
        return list
