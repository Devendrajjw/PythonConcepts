import copy

x = [1, 2, [11, 12], 3]
y = copy.copy(x)
print(x)
print(y)
y[2][1] = 13
print(x)
print(y)

i = ['a', 'b', ['aa', 'bb'], 'c']
j = copy.deepcopy(i)
print(i)
print(j)
j[2][1] = 'cc'
print(i)
print(j)

