l1 = [1, 2, 3, 4, 5]
r = 2

def rotate(l1, r):
    for i in range(r):
        l1.insert(0, l1.pop())
    return l1

print(rotate(l1, r))
