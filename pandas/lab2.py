import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\DJHUNJHU\\Downloads\\student.csv")

""" selecting single column """
# print(type(data['name']))
# print(data['name'])

""" selecting multiple column """
# print(data[['name', 'gender']])
# print(data[['name', 'gender']].shape)
# print(type((data[['name', 'gender']])))

""" selecting single row """
# print(data.iloc[1])

""" selecting multiple row using iloc"""
# print(data.iloc[1:3]) # iloc[start:stop:step]
# print(data.iloc[1:10:2])

'''fancy indexing concept of numpy we can fetch any index'''
# print(data.iloc[[1, 5, 7]])


""" selecting multiple coloum using iloc
# inside iloc before comma : is row and after comma is coloum, and colon: will select all row
# here using fancy indexing to fetch coloum 1 and 4
"""
# print(data.iloc[:, [1, 4]])
