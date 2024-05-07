list_data = [11, 12, 13, 14, 'abc', 'def', {'name': 'Devendra', 'id': 1001,
                'Address': ['Karnataka', 'Bangalore', 560076]}, 'ghi']

print(id(list_data), list_data)
cp1 = list_data.copy()
print(id(cp1), cp1)

cp2 = list_data
print(id(cp2), cp2)

list_data.insert(0, 'hello')
print(list_data)
print(cp1)

cp1.insert(1, 'world')
print(cp1)
print(list_data)
