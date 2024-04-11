def insert(data):
    for i in range(len(data)):
        curr_val = data[i]
        pos = i
        while (pos > 0) and (data[pos - 1] > curr_val):
            data[pos] = data[pos - 1]
            pos -= 1
        data[pos] = curr_val
    return data


if __name__ == '__main__':
    data1 = [111, 21, 122, 134, 29, 443, 33]
    print(insert(data1))
