# Write a Python function called find_pairs that takes a list of integers and a target sum as input.
# The function should return a list of tuples, where each tuple represents a pair of integers from the input
# list that sum up to the target sum.
l1 = [1, 2, 3, 4, 5, 6]
target_sum = 7
# result = find_pairs(numbers, target_sum)
# print(result)
# # Output: [(1, 6), (2, 5), (3, 4)]

def find_pairs(l1, target_sum):
    res = []
    while l1:
        num = l1.pop()
        diff = target_sum - num
        if diff in l1:
            res.append((diff, num))
    return res


print(find_pairs(l1, target_sum))
