import functools

arr2 = [1, 2, 3, 4, 50, 6, 7, 8, 9, 10]

m5 = functools.reduce(lambda a,b:a if a>b else b, arr2)
print(m5)
