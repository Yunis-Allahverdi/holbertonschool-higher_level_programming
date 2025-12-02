#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        list_a = list(tuple_a)
        list_a.append([0, 0])
        tuple_a = list(list_a)
        a, b = tuple_a
        a1, b1 = tuple_b
    elif len(tuple_b) == 1:
        list_a = list(tuple_a)
        list_a.append(0)
        tuple_a = list(list_a)
        a, b = tuple_a
        a1, b1 = tuple_b
    else:
        a, b, *c = tuple_a
        a1, b1, *c1 = tuple_b
    new_tuple = ((a + a1), (b + b1))
    return new_tuple


tuple_a = (1, 89)
tuple_b = (88, 11)
