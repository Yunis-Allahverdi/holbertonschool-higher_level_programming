#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        a, b = tuple_a
        a1, b1 = tuple_b
    elif len(tuple_a) > 2 and len(tuple_b) > 2:
        a, b, *c = tuple_a
        a1, b1, *c1 = tuple_b
    elif len(tuple_a) > 2 and len(tuple_b) == 2:
        a, b, *c = tuple_a
        a1, b1 = tuple_b
    elif len(tuple_a) == 2 and len(tuple_b) > 2:
        a, b = tuple_a
        a1, b1, *c1 = tuple_b
    else:
        list_a = list(tuple_a)
        list_b = list(tuple_b)
        while (len(list_a) < 2):
            list_a.append(0)

        while (len(list_b) < 2):
            list_b.append(0)

        tuple_a = tuple(list_a)
        tuple_b = tuple(list_b)
        a, b = tuple_a
        a1, b1 = tuple_b

    new_tuple = ((a + a1), (b + b1))
    return new_tuple


tuple_a = (1, 89)
tuple_b = (88, 11)
