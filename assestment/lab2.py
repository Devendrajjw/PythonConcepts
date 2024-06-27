# 3. Python multiprocessing
#
# a. Write a multiprocessing program to read the vehicle data based on the car name and return the color
# of the car in one list and print the list.

import json

def vechile_data():

    with open('file.json', 'r') as fh:
            get_data = json.load(fh)
    return dict_process(get_data)

def dict_process(gtd):
    color_list = []
    for k1, v1 in gtd.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                if k2 == 'COLOR':
                    color_list.append(v2)
    return color_list


print(vechile_data())
