from collections import OrderedDict

if __name__ == '__main__':
    ''' Normal dict '''
    print('from normal dict')
    d = dict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    print(type(d))
    # print(d)
    # print(dir(d))
    d['e'] = 5
    for k, v in d.items():
        print(k, "=", v)
    print('\n')

    d.pop('b')
    for k, v in d.items():
        print(k, "=", v)
    print('\n')

    d.update({'b': 22})
    for k, v in d.items():
        print(k, "=", v)
    print('\n')


    ''' Ordered dict '''
    print('from ordered dict')
    od = OrderedDict()
    od['w'] = 91
    od['x'] = 92
    od['y'] = 93
    od['z'] = 94
    print(type(od))
    od['v'] = 90
    for k, v in od.items():
        print(k, "=", v)
    # print(od)
    # print(list(od))
    # print(dict(od))
    # print(tuple(od))
    # print(dir(od))
