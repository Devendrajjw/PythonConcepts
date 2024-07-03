import multiprocessing

def number(start, end):
    for i in range(start, end):
        print(i)

if __name__ == '__main__':
    num_of_process = 100
    num_per_process = 100000 // num_of_process
    p_list = []
    for i in range(num_of_process):
        st = i * num_per_process
        end = st + num_per_process
        p1 = multiprocessing.Process(target=number, args=(st, end))
        p_list.append(p1)
        p1.start()

    for p in p_list:
        p.join()
