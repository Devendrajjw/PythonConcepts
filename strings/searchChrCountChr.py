# character or word count

if __name__ == '__main__':
    data = input("enter sentence ")
    char = input("search character ")
    cnt = 0
    if len(char) == 1:
        for c in data:
            if c == char:
                cnt += 1
    elif len(char) > 1:
        for c in data.split():
            a = c.strip(',.!') # hi there how are you, are you checking something here. you. you!
            if a == char:
                cnt += 1
    else:
        print('nothing to do')
    print(cnt)
