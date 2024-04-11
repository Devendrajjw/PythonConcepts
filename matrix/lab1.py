def add_func(data1):
    # print(data1)
    # ld1 = len(data1)
    # c = 0
    # print(data1[2][1])
    # print(len(data1))
    for d1 in range(len(data1)):
        if d1 != (len(data1)-1):
            print(d1, data1[d1][0], data1[d1][len(data1[d1])-1])
        if d1 == (len(data1)-1):
            # print(d1, data1[d1])
            # print(len(data1[d1]))
            # print(d1, data1[d1][1:len(data1[d1])-1])
            print(d1, data1[d1])
        # print(d1[0], d1[2])
        # c += 1
        # print(c)
        # print(len(data1))
        # print(d1)
        # while ld1 == c:
        #     print(ld1, c)
        #     break


if __name__ =="__main__" :
    data = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    add_func(data)

