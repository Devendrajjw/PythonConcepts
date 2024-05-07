list_data = [13, 12, 11, 14, 'abc', 'def', 'ghi']
list_1 = []
for _ in list_data:
    list_1.append(str(_))
    
list_1.sort(reverse=True)
print(list_1)
list_1.sort()
print(list_1)

