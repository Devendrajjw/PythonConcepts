import numpy as np

''' create 2 rows 3 column or with shape (2, 3)'''
a = np.array([
                [1, 2, 3],
                [11, 22, 33]
            ])
print(a)

'''use zeros for shape (2,2) '''
zs = (2, 2)
z = np.zeros(zs)
print(z)


'''use ones for shape (2,2) '''
os = (2, 2)
o = np.ones(os)
print(o)

'''use empty for shape (2,2) '''
es = (2, 3)
e = np.empty(es)
print(e)
