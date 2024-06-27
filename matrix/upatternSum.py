def upatt(data):
    sum = 0
    for d1 in range(len(data)):
        if d1 != (len(data) - 1):
           sum = sum + data[d1][0] + data[d1][len(data[d1]) - 1]
        if d1 == (len(data)-1):
            for d2 in data[d1]:
                sum = sum + d2
    return sum


if __name__ == "__main__":
    data1 = [[10, 2, 3, 80],
             [20, 6, 7, 70],
             [30, 40, 50, 60]]
    print(upatt(data1))

