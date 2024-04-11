def selection(data):
    for i in range(len(data)):
        curr_val = data[i]
        j = i - 1
        while (j >= 0) and (curr_val < data[j]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = curr_val
    return data


if __name__ == '__main__':
    data1 = [32, 445, 322, 746, 198, 119, 9]
    print(selection(data1))
