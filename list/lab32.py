from functools import reduce
def compdata(l1, l2, l3):
    return [x for sublist in [l1, l2, l3] for x in sublist]
    # res = []
    # for sublist in [l1, l2, l3]:
    #     for x in sublist:
    #         res.append(x)
    # return res


if __name__ == "__main__":
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    L3 = [7, 8, 9]
    print(compdata(L1, L2, L3))

# L4 = [x for sublist in [L1, L2, L3] for x in sublist]
# print(L4)


