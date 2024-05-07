list_data = [13, 12, 14, 11, 'def', 'abc', {'name': 'Devendra', 'id': 1001,
                'Address': ['Karnataka', 'Bangalore', 560076]}, 'jkl', {'work': 'Bangalore', 'location':
                'ecospace', 'pin': 10001}, 'ghi', {'baseHome': 'dumka', 'pin': 814101}, ('karan', 21), ('amar', 11),
             ('mohammed', 25)]

l1 = []
l2 = {}
l3 = []
l4 = []

for _ in list_data:
    if isinstance(_, dict):
        l2.update(_)
    elif isinstance(_, int):
        l1.append(_)
    elif isinstance(_, tuple):
        l3.append(_)
    else:
        l4.append(_)
# print(l1)
# print(l2)
# print(l3)
# print(l4)

l1.sort()
print(l1)
sl2 = sorted(l2.items(), key=lambda x: str(x[1]))
print(sl2)
