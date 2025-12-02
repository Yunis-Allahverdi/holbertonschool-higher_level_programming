#!/usr/bin/python3
def best_score(a_dictionary):
    if not in a_dictionary:
        return None
        exit()
    else:
     best_key = None
     max_val = 0
     for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            best_key = key

    print("Best: {}".format(best_key))
    exit()

a_dictionary = {}
