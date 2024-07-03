# Write a  Python program to replace the last element in a first list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
l1 =[[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
# print(l1[0][-1])
l1[0][-1] = l1[1]
l1.remove(l1[1])
print(l1)
