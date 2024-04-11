def outer(func):
    def inner(z, a):
        print("hi")
        func(z, a)
        print("welcome")
    return inner


@outer
def name(i, j):
    print("devendra", i, j)

name("one", "two")





