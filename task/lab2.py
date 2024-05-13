list = [1,2,4,5,3,7,6]

for i in range(len(list)-1):
    for j in range(len(list) - i - 1):
        if list[j] < list[j+1]:
            list[j+1], list[j] = list[j], list[j+1]
print(list)
