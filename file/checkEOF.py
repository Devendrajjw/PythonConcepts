with open('file001', 'r') as fh:
    while True:
        data = fh.read()
        if data == '':
            print('EOF')
            break
        else:
            print(data, end='')
