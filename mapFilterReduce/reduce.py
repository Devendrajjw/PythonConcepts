import functools

list1 = [1, 2, 3, 4, 5]
# print(sum(list1))
res = functools.reduce(lambda x,y:x+y, list1)
print(res)
