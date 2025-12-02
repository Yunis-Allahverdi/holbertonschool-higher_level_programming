#!/usr/bin/python3
def multiple_returns(sentence):
    t = (len(sentence), sentence[0])
    length, first = t
    print("Length: {:d} - First character: {}".format(length, first))
