from collections import defaultdict

de_dict = defaultdict(int)
L = ['T', 'o', 'b', 'e', 'e', 'l', 'i', 'g', 'i', 'b', 'l', 'e', 'f', 'o', 'r', 'r', 'e', 'f', 'e', 'r', 'r', 'a',
     'l', 'b', 'o', 'n', 'u', 's', ',', 'y', 'o', 'u', 'm', 'u', 's', 't', 'e', 'n', 's', 'u', 'r', 'e', 't', 'h',
     'a', 't', 't', 'h', 'e', 'r', 'e', 's', 'u', 'm', 'e', 'i', 's', 'u', 'p', 'l', 'o', 'a', 'd', 'e', 'd', 'o',
     'n', 't', 'h', 'e', 'M', 'y', 'R', 'e', 'f', 'e', 'r', 'r', 'a', 'l', 'p', 'o', 'r', 't', 'a', 'l', 'b', 'e',
     'f', 'o', 'r', 'e', 't', 'h', 'e', 'f', 'i', 'r', 's', 't', 'i', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w']

for i in L:
    de_dict[i] += 1
print(de_dict)

print('\n')

norm_dict = dict()
for i in L:
    if i not in norm_dict:
        norm_dict[i] = 1
    else:
        norm_dict[i] += 1
print(norm_dict)

