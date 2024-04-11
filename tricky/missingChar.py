data1 = ['a', 'a', 'b', 'b', 'b', 'c', 'd']
data2 = ['a', 'a', 'b', 'b', 'c', 'd']

for i in range(len(data1)-1):
    # print(data1[i])
    if len(data2) < len(data1):
        # print(data2[i])
        d2 = data2[i]
    if d2 != data1[i]:
        print(data1[i])
        if len(data1) > len(data2):
            print(data1.pop())
    # else:
    #     break
