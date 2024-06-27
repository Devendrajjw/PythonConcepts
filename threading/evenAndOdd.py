import threading
import time

def even(arr):
    for a in arr:
        if a % 2 == 0:
            print(f'{a} is even')
            time.sleep(0.5)


def odd(arr):
    for a in arr:
        if a % 2 != 0:
            print(f'{a} is odd')
y            utime.sleep(0.5)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_thread = threading.Thread(target=even, args=(numbers,))
    odd_thread = threading.Thread(target=odd, args=(numbers,))
    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
