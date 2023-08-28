#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        div = fct(*args)
        return (div)
    except Exception as safe:
        print("Exception: {}".format(safe), file=stderr)
        return None
