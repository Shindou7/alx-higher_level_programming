#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = 0
    denomi = 0
    for mylist in my_list:
        numb += mylist[0] * mylist[1]
        denomi += mylist[1]
    return (numb / denomi)
