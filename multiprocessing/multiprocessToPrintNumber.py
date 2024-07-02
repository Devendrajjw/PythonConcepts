import multiprocessing
import time


def number(start, end):
    for i in range(start, end):
        print(i)

if __name__ == '__main__':
    num_of_process = 100
    num_per_process = 100000 // num_of_process
    p_list = []
    start_time = time.time()
    print(start_time, 'start time') # 1719855108.498556 start time
    for i in range(num_of_process):
        st = i * num_per_process
        end = st + num_per_process
        p1 = multiprocessing.Process(target=number, args=(st, end))
        p_list.append(p1)
        p1.start()

    for p in p_list:
        p.join()
    end_time = time.time()
    print(end_time, 'end time') # 1719855114.0678122 end time
