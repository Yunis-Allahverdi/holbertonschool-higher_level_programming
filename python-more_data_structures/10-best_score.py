#!/usr/bin/python3
def best_score(a_dictionary):
    new_list = list(a_dictionary)
    best_key = new_list[0]
    if len(a_dictionary) == 0:
        best_key = None
    else:
        for i in list(sorted(a_dictionary)):
            if i > best_key:
                best_key = i
    print("Best score: {}".format(best_key))
    exit()

a_dictionary = {}
