import numpy as np

''' create 3D array with shape (2, 3, 4) '''
nested_list = [
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
              ]
a = np.array(nested_list)
print(a)

zs = (4, 2, 2)
z = np.zeros(zs)
print(z)

'''
[[[0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]]]
'''
