import time
from multiprocessing import Pool

COUNT = 500000000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    pool = Pool(processes=2)
    start_time = time.time()
    r1 = pool.apply_async(countdown, [COUNT//3])
    r2 = pool.apply_async(countdown, [COUNT//3])
    pool.close()
    pool.join()
    end_time = time.time()
    print('time taken to complete ', end_time - start_time)
