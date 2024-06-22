nested_dict = {
    'a': 'value_a_1',
    'b': {
        'c': ['value_c_1', 'value_c_2'],
        'd': {
            'e': 'value_e_1'
        }
    },
    'f': 'value_f_1'
}
for k1, v1 in nested_dict.items():
    if isinstance(v1, dict):
        for k2, v2 in v1.items():
            if isinstance(v2, dict):
                for k3, v3 in v2.items():
                    if isinstance(v3, str):
                        if v3 == 'value_e_1':
                            print(f'value of {k3} is {v3}')

