def deco(func):
    def inner():
        return f'{func().upper()} Devendra'
    return inner


@deco
def greet():
    return 'goodmorning'

print(greet())
