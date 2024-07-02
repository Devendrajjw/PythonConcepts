from functools import reduce
def compdata(l1, l2, l3):
    res = [x for sublist in [l1, l2, l3] for x in sublist if x != 0]
    return sorted(res)
    # res = []
    # for sublist in [l1, l2, l3]:
    #     for x in sublist:
    #         res.append(x)
    # return res


if __name__ == "__main__":
    L1 = [11, 2, 3, 0, 0, 0 ]
    L2 = [4, 35, 6]
    L3 = [74, 8, 9]
    print(compdata(L1, L2, L3))

# L4 = [x for sublist in [L1, L2, L3] for x in sublist]
# print(L4)


