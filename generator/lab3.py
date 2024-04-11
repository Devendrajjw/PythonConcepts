'''
iterable -
iterator -
iteration -

'''

def gen1(n):
    for i in range(n):
        yield i


#
# print(gen1(10000000))
# for i in gen1(100000000):
#     print(i)

obj1 = gen1(3)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
