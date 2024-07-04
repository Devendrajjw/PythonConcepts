def even_number_in_chunks(narr, list_size=2):
    even_list = []
    for n in narr:
        if n % 2 == 0:
            even_list.append(n)
            if len(even_list) == list_size:
                yield even_list
                even_list = []
    if even_list:
        yield even_list


if __name__ == '__main__':
    data = [n for n in range(10)]
    for n in even_number_in_chunks(data):
        print(n)
