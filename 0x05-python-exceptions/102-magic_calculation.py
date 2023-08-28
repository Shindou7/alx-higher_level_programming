#!/usr/bin/python3
def magic_calculation(a, b):
    magic = 0
    for n in range(1, 3):
        try:
            if (n > a):
                raise Exception('Too far')
            else:
                magic += a ** b / n
        except Exception:
            magic = b + a
            break
    return magic
