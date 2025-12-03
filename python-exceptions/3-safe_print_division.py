#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as err:
        result = None
    finally:
        return result
    return "Inside result: {}".format(result)
