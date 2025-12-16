#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(file=""):
    try:
        with open(file, mode='r') as r_file:
            csv_file = list(csv.DictReader(r_file))
        
        with open("data.json", 'w') as w_file:
            json.dump(csv_file, w_file)

    except OSError:
        print('file not found')
        return False

    else:
        return True
