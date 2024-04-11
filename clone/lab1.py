import copy

x = [1, 2, 3]
y = copy.copy(x)
print(x)
print(y)
y.append(4)
print(x)
print(y)
print()

i = ['a', 'b', 'c']
j = copy.deepcopy(i)
print(i)
print(j)
j.append('d')
print(i)
print(j)
