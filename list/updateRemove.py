list_data = [11, 12, [13, 14], 'def', 'abc', {'name': 'Devendra'} ]
l1 = list_data.copy()
l2 = {}
for _ in list_data:
    if isinstance(_, dict):
        l2.update(_)
        l1.remove(_)
print(l2)
print(l1)

