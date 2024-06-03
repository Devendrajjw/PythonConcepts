import collections

def anagrams(words):
    anagrams = collections.defaultdict(list)

# sort characters create a key and append word into a listr
    for i in words:
        anagrams[tuple(sorted(i))].append(i)
    return list(anagrams.values())

print(anagrams(['eat', 'tea', 'tan', 'ate', 'nat','bat']))
