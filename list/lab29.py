# print(remove_duplicates([1, 2, 3, 2, 1]))  # Output: [1, 2, 3]

def remdup(lll):
    result = []
    for ele in lll:
        if ele not in result:
            result.append(ele)
    return result


print(remdup([1, 2, 3, 2, 1]))
