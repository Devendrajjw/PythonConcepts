# c pattern
matrix = [[10, 10, 10, 10],
        [10, 6, 7, 1],
        [10, 4, 3, 2],
        [10, 10, 10, 10]
       ]


def cpatt(mat1):
    rows = len(mat1)
    col = len(mat1[0])
    s = 0

    for j in range(col):
        s += mat1[0][j]
    for i in range(1, rows):
        s += mat1[i][0]
    for k in range(1, col):
        s += mat1[rows - 1][k]
    return s


print(cpatt(matrix))

