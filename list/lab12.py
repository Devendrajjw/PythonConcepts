list_data = [11, 12, 13, 14, 'def', 'abc', {'name': 'Devendra', 'id': 1001,
                'Address': ['Karnataka', 'Bangalore', 560076]}, 'jkl', {'work': 'Bangalore', 'location':
                'ecospace', 'pin': 10001}, 'ghi', {'baseHome': 'dumka', 'pin': 814101}]
l1 = list_data.copy()
l2 = {}
for _ in list_data:
    if isinstance(_, dict):
        l2.update(_)
        l1.remove(_)
print(l2)
print(l1)

