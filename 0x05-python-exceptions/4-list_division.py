#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for n in range(list_length):
        division = 0
        try:
            division = my_list_1[n] / my_list_2[n]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            list.append(division)
    return list
