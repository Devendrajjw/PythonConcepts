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

with open('file1.json', 'w') as fh:
    json_data = json.dump(nested_dict, fh, indent=4)
    # check file1.json getting created
