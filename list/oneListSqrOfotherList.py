def comp(a1, a2):
    a1.sort()
    a2.sort()
    a1_sq = [n**2 for n in a1]
    a2_sq = [n**2 for n in a2]
    if (a1 == a2) or (a1_sq == a2_sq) or (a1 == a2_sq) or (a2 == a1_sq):
        print("true")

comp([3,5,2,4], [25,4,9,16])
