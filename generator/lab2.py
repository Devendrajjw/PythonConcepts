def gen():
    for i in range(101):
        yield i


if __name__ == '__main__':
    print(next(gen()))



