def add_to_return_value(add_value):
    print('1')
    def decorator(func):
        print('2')
        def wrapper(*args, **kwargs):
            print('3')
            result = func(*args, **kwargs)
            print('result', result)
            return result + add_value
        print('4')
        return wrapper
    print('5')
    return decorator


@add_to_return_value(10)
def get_number():
    print('0')
    return 5


print(get_number())
