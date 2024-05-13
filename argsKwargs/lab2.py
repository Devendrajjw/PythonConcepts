def fun1(*args, **kwargs):
    for _ in args:
        print(_)
    for k, v in kwargs.items():
        print(k, " = ", v)

fun1(1, 2, 3, 'devendra')
