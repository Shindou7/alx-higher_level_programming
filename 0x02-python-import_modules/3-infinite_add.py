#!/usr/bin/python3
import sys

if __name__ == '__main__':
    avg = sys.argv
    l_avg = len(avg)
    result = 0

    if l_avg > 1:
        for i in range(1, l_avg):
            result += int(avg[i])
    print(result)
