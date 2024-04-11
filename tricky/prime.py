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
    list_prime(data)
    print()
    num_prime(7)
