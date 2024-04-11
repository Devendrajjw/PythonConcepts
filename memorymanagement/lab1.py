import sys

alal = 11
print(sys.getrefcount(alal))
zmzm = alal
print(sys.getrefcount(alal))
lll = [alal, alal, alal]
print(sys.getrefcount(alal))

sss = 'a'
print(sys.getsizeof(sss))
ddd = 1
print(sys.getsizeof(ddd))
fff = 1.1
print(sys.getsizeof(fff))

