if __name__ == '__main__':
    N = int(input('enter number '))
    ls = []
    for i in range(N):
        c = input('nums').split()
        # print(cmd)

        if c[0] == 'insert':
            ls.insert(int(c[1]), int(c[2]))

        if c[0] == 'print':
            print(ls)

        if c[0] == 'remove':
            ls.remove(int(c[1]))

        if c[0] == 'append':
            ls.append(int(c[1]))

        if c[0] == 'sort':
            ls.sort()

        if c[0] == 'pop':
            ls.pop()

        if c[0] == 'reverse':
            ls.reverse()
