def dict_list(data):
    for k, v in data.items():
        if isinstance(v, dict):
            dict_list(v)
        elif isinstance(v, list):
            for i in range(len(v)):
                if isinstance(v[i], dict):
                    dict_list(v[i])
                    if k == 'e':
                        print(f'{k}:{v}')
                elif isinstance(v[i], str):
                    if k == 'e':
                        print(f'{k}:{v}')
                    # v[i] = v[i].upper()
                    # print(v[i])
        elif isinstance(v, str):
            if k == 'e':
                print(f'{k}:{v}')
            data[k] = v.upper()


nested_dict = {
    'a': 'value1',
    'b': {
        'c': ['value2_1', 'value2_2'],
        'd': {
            'e': 'value2_2_1'
        }
    },
    'f': 'value3'
}
dict_list(nested_dict)
