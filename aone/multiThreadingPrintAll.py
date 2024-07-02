import threading
import time


def even_num(arr, even_list):
    for a in arr:
        if a % 2 == 0:
            even_list.append(a)
            time.sleep(0.5)


def odd_num(arr, odd_list):
    for a in arr:
        if a % 2 != 0:
            odd_list.append(a)
            time.sleep(0.5)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    even_list = []
    odd_list = []
    t1_even = threading.Thread(target=even_num, args=(data, even_list))
    t2_odd = threading.Thread(target=odd_num, args=(data, odd_list))
    t1_even.start()
    t2_odd.start()
    t1_even.join()
    t2_odd.join()
    print('even num', even_list)
    print('odd num', odd_list)
