#!/usr/bin/python3
def roman_to_int(roman_string):
    int_list = []
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        for i in roman_string:
            if i == "X":
                int_list.append(10)
            elif i == "I":
                int_list.append(1)
            elif i == "V":
                int_list.append(5)
            elif i == "L":
                int_list.append(50)
            elif i == "C":
                int_list.append(100)
            elif i == "D":
                int_list.append(500)
            else:
                return 0
        result = 0
        for i in range(len(int_list)):
            if i == len(int_list) - 1:
                result += int_list[i]
                break
            else:
                if int_list[i] >= int_list[i+1]:
                    result += int_list[i]
                else:
                    result -= int_list[i]

        return result
