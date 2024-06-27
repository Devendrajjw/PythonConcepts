# 1. Python app development
#
# a. Design a class to store a data of the vehicle available
# in the json file and design a class to implement
# below public interface to display on std output and manipulate data.
#
# 1. show_vehicle_data
#
# 2. update vehicle data for field vehicle cost

import json
from flask import request

class Store:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def store_vechile_data(self):
        data_given = {self.name: self.color}
        with open('file2.json', 'w') as fh:
            json.dump(data_given, fh)

    def load_data(self):
        pass



if __name__ == "__main__":
    st = Store('toyota', 'white')
    st.store_vechile_data()

