# Write a  Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
l1 =[[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
for l in range(len(l1)-1):
    l1[l].extend(l1[-1])
    l1.pop()
l2 = []
for l in l1:
    l2.extend(l)
print(l2)

