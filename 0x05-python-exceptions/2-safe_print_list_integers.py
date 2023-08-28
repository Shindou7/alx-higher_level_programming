#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            list += 1
        except (TypeError, ValueError):
            pass
    print()
    return list
