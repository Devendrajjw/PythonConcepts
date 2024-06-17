def check_zero(func):
    def wrapper(a, b):
        if a != 0 and b != 0:
            return func(a, b)
        else:
            print("give positive number")
    return wrapper

@check_zero
def add_number(n1, n2):
    return n1 + n2

if __name__ == "__main__":
    print(add_number(0, 2))
