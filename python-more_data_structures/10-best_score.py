#!/usr/bin/python3
def best_score(a_dictionary):
    if (len(a_dictionary) == 0):
        return None
    else:
        best = None
        max_val = 0
        for key, value in a_dictionary.items():
            if value > max_val:
                max_val = value
                best = key

        print("Best score: {}".format(best_key))


a_dictionary = {}
