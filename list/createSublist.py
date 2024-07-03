if __name__ == '__main__':
    N = int(input('number of sublist to be created '))
    arr = []
    for i in range(N):
        e = input('digits inside list single digit or multiple digit with space ').split()
        arr.append(e)
    print(arr)

'''
outer 3
111
222
333
[['111'], ['222'], ['333']]
'''

'''
outer 3
11 12 13
14 15 16
17 18 19
[['11', '12', '13'], ['14', '15', '16'], ['17', '18', '19']]
'''
