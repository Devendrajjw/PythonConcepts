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

print(nested_dict)
# {'a': 'value1', 'b': {'c': ['value2_1', 'value2_2'], 'd': {'e': 'value2_2_1'}}, 'f': 'value3'}
print(type(nested_dict))
# <class 'dict'>

json_data = json.dumps(nested_dict)
print(json_data)
# {"a": "value1", "b": {"c": ["value2_1", "value2_2"], "d": {"e": "value2_2_1"}}, "f": "value3"}
print(type(json_data))
# <class 'str'>

json_data = json.dumps(nested_dict, indent=4)
print(json_data)
'''
{
    "a": "value1",
    "b": {
        "c": [
            "value2_1",
            "value2_2"
        ],
        "d": {
            "e": "value2_2_1"
        }
    },
    "f": "value3"
}
'''
