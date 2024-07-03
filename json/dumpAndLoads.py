import json

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

some_str = 'abcdef'

# converting to json data
conv_to_js_d = json.dumps(nested_dict)
print(conv_to_js_d)
'''
{"a": "value1", "b": {"c": ["value2_1", "value2_2"], "d": {"e": "value2_2_1"}}, "f": "value3"}
'''

# reconverting to python data
conv_to_py_d = json.loads(conv_to_js_d)
print(conv_to_py_d)
'''
{'a': 'value1', 'b': {'c': ['value2_1', 'value2_2'], 'd': {'e': 'value2_2_1'}}, 'f': 'value3'}
'''

s_js = json.dumps(some_str)
print(s_js)
print(type(s_js))

s_py = json.loads(s_js)
print(s_py)
print(type(s_py))
