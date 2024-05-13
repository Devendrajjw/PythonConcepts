dict1 = {}
key1 = ['name', 'age', 'location']
list1 = []
for i in range(2):
    for k1 in key1:
        value = input(f" enter {k1}: ")
        dict1[k1] = value
    list1.append(dict1)
print(list1) # [{'name': 'bbb', 'age': '14', 'location': 'b'}, {'name': 'bbb', 'age': '14', 'location': 'b'}]

# dict1 = {}
# key1 = ['name', 'age', 'location']
# for k1 in key1:
#     value = input(f" enter {k1}: ")
#     dict1[k1] = value
#     print(dict1)
