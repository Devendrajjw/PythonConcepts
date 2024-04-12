def fibox(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result


def fibgen(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(fibox(10))
    for num in fibgen(10):
        print(num, end=' ')
