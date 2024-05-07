ls = [3, 5, 2, 1, 0, 0]
sr = sorted(ls, reverse=False)
print(sr)
print(sr[2::]+sr[:2:]) # [1, 2, 3, 5, 0, 0]
# ls.insert(1, 22)
# print(ls)
