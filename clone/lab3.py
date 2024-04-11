import copy

x = [1, 2, 3]
y = copy.copy(x)
print(x)
print(y)
y[1] = 22
print(x)
print(y)


i = ['a', 'b', 'c']
j = copy.copy(i)
print(i)
print(j)
j[1] = 'bb'
print(i)
print(j)
