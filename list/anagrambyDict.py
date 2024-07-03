# Write a function that takes a list of strings as input and groups anagrams together. An anagram
# is a word formed by rearranging the letters of another word, using all the original letters exactly once. For
# example:
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# grouped_anagrams = group_anagrams(words)
# # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def createKey(strings):
    key = ''
    for ch in sorted(strings):
        key += ch
    return str(key)
# print(createKey('bca'))


def groupWords(data):
    group = dict()
    for ele in data:
        if group.get(createKey(ele)) == None:
            group[createKey(ele)] = [ele]
        else:
            group[createKey(ele)].append(ele)
    return group


result1 = groupWords(words)
print(result1)

result2 = []
for k, v in result1.items():
    result2.append(v)
print(result2)
