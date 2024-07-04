def chunkPrime(data, chunk_size=3):
    new_list = []
    for i in range(len(data)):
        for d in range(2, data[i]//2 + 1):
            if data[i] % d == 0:
                break
        else:
            new_list.append(data[i])
            if len(new_list) == chunk_size:
                yield new_list
                new_list = []
    if new_list:
        yield new_list


if __name__ == '__main__':
    lower_range = eval(input('enter lower range '))
    higher_range = eval(input('enter higher range '))
    num_list = [n for n in range(lower_range, higher_range)]
    for n in chunkPrime(num_list):
        print(n)
