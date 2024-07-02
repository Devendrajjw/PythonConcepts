import threading
import time


def numbers(start, end):
    for i in range(start, end):
        print(i)


if __name__ == '__main__':
    c = 0
    d = 0
    num_of_thread = 100
    num_per_thread = 100000 // num_of_thread
    thread_list = []
    start_time = time.time()
    print(start_time, 'start time') # 1719855004.1177015 start time
    for i in range(num_of_thread):
        d += 1
        st = i * num_per_thread
        end = st + num_per_thread
        t1 = threading.Thread(target=numbers, args=(st, end))
        thread_list.append(t1)
        print(f"============started thread {d}===============")
        t1.start()

    for tl in thread_list:
        c += 1
        print(f"============join thread {c}===============")
        tl.join()
    end_time = time.time()
    print(end_time, 'end time') # 1719855010.0524411 end time

