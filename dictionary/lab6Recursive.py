'''
Test for : Dictonary, Function, Recursion/ without recursion
WAP to fetch value for 'e' key from the given Dictonary, using recursion.
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
'''

def dict_fun(d):
    for key, value in d.items():
        if isinstance(value, dict):
            dict_fun(value)
        else:
            if isinstance(value, str):
                if key == 'e':
                    print(f'{key}:{value}')
                d[key] = value.upper()

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

dict_fun(nested_dict)
print(nested_dict)
