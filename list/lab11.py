list_data = [13, 12, 11, 14, 'def', 'abc', 'ghi']
l1, l2 = [], []
# l2 = []
for _ in list_data:
    if isinstance(_, int):
        l1.append(_)
    else:
        l2.append(_)
l1.sort()
print(l1)
l2.sort()
print(l2)
print(l1 + l2)

