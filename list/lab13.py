list_data = [11, 12, 13, 14, 'def', 'abc', {'name': 'firstname', 'id': 1001,
                'Address': ['Karnataka', 'Bangalore', 560001]}, 'jkl', {'work': 'Bangalore', 'location':
                'ecospace', 'pin': 10001}, 'ghi', {'baseHome': 'basehomeloc', 'pin': 998811}]
l1 = []
for _ in list_data:
    if isinstance(_, dict):
        l1.append(_)
print(l1[1]['work'])
