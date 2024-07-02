import threading
import time

def even_num(arr):
    for a in arr:
        if a % 2 == 0:
            print('even', a)
            time.sleep(0.5)

def odd_num(arr):
    for a in arr:
        if a % 2 == 0:
            print('odd', a)
            time.sleep(0.5)

if __name__  == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    t1_even = threading.Thread(target=even_num, args=(data, ))
    t2_even = threading.Thread(target=odd_num, args=(data, ))
    t1_even.start()
    t2_even.start()
    t1_even.join()
    t2_even.join()

