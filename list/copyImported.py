import copy

list_data = [11, 12, 13, 14]
#
# print(list_data)
# cp1 = copy.copy(list_data)
# print(cp1)

# print(list_data[6]['Address'][2])

cp2 = copy.copy(list_data)
# print(id(list_data))
# print(id(cp2))

# cp2.insert(6, 'washington')
# print(list_data)
# print(cp2)

for _ in cp2:
    print(_)
print(list_data)
print(cp2)
