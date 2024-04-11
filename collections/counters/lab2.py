from collections import Counter

if __name__ == '__main__':
    data1 = ['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']
    print(Counter(data1))
    print(type(Counter(data1)))
    print(list(Counter(data1)))
    print(dict(Counter(data1)))
    print(tuple(Counter(data1)))

    for k, v in Counter(data1).items():
        print(k)
