import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\DJHUNJHU\\Downloads\\student.csv")

''' this will give boolean value True or false'''
mask = data['mark'] == 88
# print(mask)
# print(type(mask))
''' mask variable will now only having true values '''
# print(data[mask])
# print(data[mask].shape)
# print(data[mask].shape[0])

mask1 = data['gender'] == 'female'
result = data[mask & mask1]  # using bitwise and & bcz we are comparing two boolean value
count = data[mask & mask1].shape[0]  # using bitwise and & bcz we are comparing two boolean value
print(result)
print(count)
