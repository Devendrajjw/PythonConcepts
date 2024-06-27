import threading
import time


def evenNumber(arr, results, key):
    for a in arr:
        if a % 2 == 0:
            results[key] = a
            return
    time.sleep(0.5)

def oddNumber(arr, results, key):
    for a in arr:
        if a % 2 != 0:
            results[key] = a
            return
    time.sleep(0.5)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    results = {}
    t1_even = threading.Thread(target=evenNumber, args=(arr, results, 'even'))
    t2_odd = threading.Thread(target=oddNumber, args=(arr, results, 'odd'))
    t1_even.start()
    t2_odd.start()
    t1_even.join()
    t2_odd.join()
    # Print results
    print('even numbers ', results.get('even'))
    print('odd numbers ', results.get('odd'))


