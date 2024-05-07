data = [44, 22, 11, 33, 21, 43, 23, 34, 24, 42, 14, 21, 22, 33, 12, 34, 41, 21, 24, 31, 34, 42, 43, 11, 12, 13, 14]
print(max(data))
data.remove(max(data))
print(max(data))

print(data.count(34))

for dig in data:
    print(f'{dig}= {data.count(dig)}', end=', ')
