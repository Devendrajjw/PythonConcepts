def outer(func):
    def inner(z, a):
        func(z, a)
    return inner


@outer
def name(i, j):
    print("My name is", i, j)

name("first", "last")





