from collections import OrderedDict

if __name__ == '__main__':
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    od['d'] = 4
    print("initial value")
    for k, v in od.items():
        print(k, "=", v)

    od.pop('a')
    print('\n')
    print("first time pop value using pop() passwd a to pop")
    for k, v in od.items():
        print(k, "=", v)

    od.popitem()
    print('\n')
    print("second time pop value using popitem() default remove last item")
    for k, v in od.items():
        print(k, "=", v)

    od.update({'z': 99})
    print('\n')
    print("third time update value using update({'z':99})")
    for k, v in od.items():
        print(k, "=", v)
