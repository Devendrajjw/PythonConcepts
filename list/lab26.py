l1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
l2 = []
c = 0
for ind in range(len(l1) + 1):
    c += 1
    if c == 2:
        l2.append(l1[ind])
        c = 0


print(l2)
