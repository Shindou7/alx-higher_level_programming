#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for n, m in a_dictionary.items():
        if m == value:
            keys.append(n)
    for n in keys:
        del a_dictionary[n]
    return a_dictionary
