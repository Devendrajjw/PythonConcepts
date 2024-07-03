def gen():
    for i in range(101):
        yield i


if __name__ == '__main__':
    obj = gen()
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))



