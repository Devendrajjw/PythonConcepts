list_data = [11, 12, [13, 14], 'def', 'abc', {'name': 'firstname'}]
l1 = []
for _ in list_data:
    if isinstance(_, dict):
        l1.append(_)
print(list_data)
print(l1[0]['name'])
