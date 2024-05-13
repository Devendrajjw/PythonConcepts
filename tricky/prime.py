def list_prime(data1):
    for indx in range(len(data1)):
        for div in range(2, data1[indx]//2 + 1):
            if data1[indx] % div == 0:
                break
        else:
            print(data1[indx], end=" ")


def num_prime(num1):
    for div in range(2, num1//2 + 1):
        if num1 % div == 0:
            break
    else:
        print(num1)


if __name__ == '__main__':
    data = [i for i in range(1, 101)]
    # 1 2 3 5 7 11 13 17 19 23 29 31
    data22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 17, 19, 23 ]
    list_prime(data)
    list_prime(data22)
    # print()
    num_prime(7)
    # x = [1, 2, 3]
    # y = 'hello'
    # x.remove(2)
    # x.extend([10, 11, 12])
    # x.append([20, 21, 22])
    # print(x)
    # print(y.isalpha())
    # print(y.isnumeric())

