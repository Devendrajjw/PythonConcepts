def even_number_in_chunks(num, list_size=3):
    even_list = []
    for n1 in num:
        if n1 % 2 == 0:
            even_list.append(n1)
            if len(even_list) == list_size:
                yield even_list
                even_list = []
    if even_list:
        yield even_list


if __name__ == '__main__':
    data = [n for n in range(100)]
    for n in even_number_in_chunks(data):
        print(n)
