def deco(func):
    def inner(a, b):
        print('I am going to divide', a, b)
        return func(a, b)
    return inner


@deco
def div(a, b):
    return a // b


print(div(10, 2))
