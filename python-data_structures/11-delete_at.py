#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx:idx+1]
        new_list = my_list
        return new_list


my_list = []
idx = 0
