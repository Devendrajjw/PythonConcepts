def ins(data):
    for i in range(len(data)):
        curr_value = data[i]
        j = i
        while (j > 0) and (data[j - 1] > curr_value):
            data[j] = data[j - 1]
            j -= 1
        data[j] = curr_value
    return data


if __name__ == '__main__':
    data1 = [22, 11, 33, 44, 111, 2222, 321, 213, 55, 332, 33]
    print(ins(data1))
