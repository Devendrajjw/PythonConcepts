def transform_nested_dict(data):
    for k, v in data.items():
        if isinstance(v, dict):
            transform_nested_dict(v)
        elif isinstance(v, list):
            for i in range(len(v)):
                if isinstance(v[i], dict):
                    transform_nested_dict(v[i])
                elif isinstance(v[i], str):
                    v[i] = v[i].upper()
        elif isinstance(v, str):
            data[k] = v.upper()

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

transform_nested_dict(nested_dict)
print(nested_dict)
