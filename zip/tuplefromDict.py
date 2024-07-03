d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'aaa': 111, 'bbb': 222, 'ccc': 333}
z1 = zip(d1.items(), d2.items())
print(list(z1))

# [(('a', 1), ('aaa', 111)), (('b', 2), ('bbb', 222)), (('c', 3), ('ccc', 333))]
