#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        t = (len(sentence), sentence[0])
    else:
        t = (0, None)
    length, first = t
    print("Length: {:d} - First character: {}".format(length, first))
