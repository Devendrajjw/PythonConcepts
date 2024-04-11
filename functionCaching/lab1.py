from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print('done for 20')
print(fx(5))
print('done for 5')
print(fx(6))
print('done for 6')

print(fx(20))
print('done for 20')
print(fx(5))
print('done for 5')
print(fx(6))
print('done for 6')


print(fx(33))
print('done for 33')
print(fx(61))
print('done for 61')

