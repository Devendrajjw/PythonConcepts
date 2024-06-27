words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict1 = {}
for ele in words:
    sorted_ele = ''.join(sorted(ele))
    if sorted_ele in dict1:
        dict1[sorted_ele].append(sorted_ele)
    else:
        dict1[sorted_ele] = [ele]
print(list(dict1.values()))
