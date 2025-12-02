#!/usr/bin/python3
def best_score(a_dictionary):
    new_list = list(sorted(a_dictionary))
    best_key = new_list[0]
    if len(a_dictionary) == 0:
        best_key = None
    print("Best: {}".format(best_key))
    exit()

a_dictionary = {}
