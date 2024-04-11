def upattern(data):
    # print(len(data))
    for d1 in range(len(data)):
        # print(d1)
        # print(data[d1])
        if d1 != (len(data)-1):
            # print(data[d1])
            print(data[d1][0], data[d1][len(data[d1])-1])
        if d1 == (len(data)-1):
            print(data[d1])


if __name__ == "__main__":
    data1 = [[1, 2, 3, 10],
             [4, 5, 6, 20],
             [7, 8, 9, 30]]
    upattern(data1)
