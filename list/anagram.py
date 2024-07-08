words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict1 = {}
for ele in words:
    sorted_ele = ''.join(sorted(ele))
    if sorted_ele in dict1:
        dict1[sorted_ele].append(sorted_ele)
    else:
        dict1[sorted_ele] = [ele]
print(dict1)
print(list(dict1.values()))

# {'aet': ['eat', 'aet', 'aet'], 'ant': ['tan', 'ant'], 'abt': ['bat']}
# [['eat', 'aet', 'aet'], ['tan', 'ant'], ['bat']]
