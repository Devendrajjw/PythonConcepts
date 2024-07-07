import threading
import sys
import time


def even(num):
    for n in range(num):
        if n%2==0:
            print(n)

start_time = time.time()
arr1 = 100000//2
arr2 = arr1//2
t1 = threading.Thread(target=even, args=(arr1,))
t2 = threading.Thread(target=even, args=(arr2,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
result = end_time - start_time
print('======time======',result)


