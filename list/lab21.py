# Write a function called rotate_tuple that takes a tuple and an integer n as input and rotates the
# elements of the tuple to the right by n positions. For example, if n is 2 and the input tuple is
# (1, 2, 3, 4, 5), the output should be (4, 5, 1, 2, 3)

l1 = [1, 2, 3, 4, 5]
r = 2


def rotate(l1, r):
    for i in range(r):
        l1.insert(0, l1.pop())
    return l1


print(rotate(l1, r))
