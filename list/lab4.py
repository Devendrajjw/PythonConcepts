if __name__ == '__main__':
    N = int(input('outer '))
    arr = []
    # for i in range(N):
    #     arr.insert(i, input('inner '))
    #     print(arr)
    for i in range(N):
        e = input().split()
        arr.append(e)
    print(arr)

'''
outer 3
111
222
333
[['111'], ['222'], ['333']]
'''
