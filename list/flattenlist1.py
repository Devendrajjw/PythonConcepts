from pandas.core.common import flatten

'''
# way 1
lis1 = [[1, 2, 3], [4, 5], [6]] # won't work for [[1, 2, 3], [4, 5], 6]
fl = sum(lis1, [])
print(fl) # [1, 2, 3, 4, 5, 6]
'''

# way 2 using pandas
lis1 = [[1, 2, 3], [4, 5], 6]
print(list(flatten(lis1)))
