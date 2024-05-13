import sys
if __name__ == '__main__':
    x = range(100)
    # w = [num for num in range(100)]
    # print(sys.getsizeof(x))
    # print(sys.getsizeof(w))
    e = []
    o = []
    v = lambda k:'Even' if k%2 == 0 else 'odd'
    for i in x:
        if v(i) == 'Even':
            e.append(i)
        else:
            o.append(i)
    print('even numbers ', e)
    print('odd numbers ', o)
