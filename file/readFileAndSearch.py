import os
import re

l_file = ['file001', 'file002']
p_file = os.getcwd()
p_final = ''
d1 = {}
for ll in l_file:
    p_final = os.path.join(p_file, ll)
    if os.path.exists(p_final):
        # print(f'{p_final} exists ')
        with open(p_final, 'r') as fh:
            # wordLists = fh.readlines()
            for word in fh:
                if word not in d1:
                    d1[word] = 1
                else:
                    d1[word] += 1
print(d1)

