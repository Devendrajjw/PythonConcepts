# Write a function called rotate_tuple that takes a tuple and an integer n as input and rotates the
# elements of the tuple to the right by n positions. For example, if n is 2 and the input tuple is
# (1, 2, 3, 4, 5), the output should be (4, 5, 1, 2, 3)

t1 = (1, 2, 3, 4, 5)
n = 2
print(t1[2:] + t1[:2])
