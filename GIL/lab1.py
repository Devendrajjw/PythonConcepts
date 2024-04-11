import time
from threading import Thread

'''
single thread example
'''
COUNT = 500000000
def countdown(n):
    while n > 0:
        n -= 1


start_time = time.time()
countdown(COUNT)
end_time = time.time()
print('time taken in seconds ', end_time - start_time)

