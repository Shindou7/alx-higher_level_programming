#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total_sum = 0
    total_prev = 0

    for i in roman_string[::-1]:
        if i not in val:
            return 0

        if val[i] < total_prev and total_prev:
            total_sum -= val[i]
        else:
            total_sum += val[i]
        total_ prev = val[i]
    return total_sum
