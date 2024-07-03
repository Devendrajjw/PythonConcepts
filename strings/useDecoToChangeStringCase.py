def deco(func):
    def inner():
        return f'{func().upper()} Devendra'
        # r = func()
        # print('r===', r)
        # return r
    return inner


@deco
def greet():
    return 'goodmorning'

print(greet())
