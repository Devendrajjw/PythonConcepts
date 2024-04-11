def bubble(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    # print(data)
    return data


if __name__ == "__main__":
    data1 = [33, 21, 12, 4, 10, 99, 15, 102]
    print(bubble(data1))

