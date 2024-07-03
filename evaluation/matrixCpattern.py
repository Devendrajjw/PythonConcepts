def pattern(matrix):

#  check if matrix is empty or not

    if len(matrix)==0 or len(matrix[0])==0:
        return 0
    rows=len(matrix)
    cols=len(matrix[0])

 # calculating the sum of rows and columns to get cmatrix
    first_row_sum=sum(matrix[0])
    first_column_sum=sum(matrix[i][0] for i in range(1, rows))
    last_row_sum=sum(matrix[rows-1][j] for j in range(1, cols))
    c_sum=first_row_sum+first_column_sum+last_row_sum
    return c_sum

matrix=[
     [20,10,10,10],
    [10,60,70,80],
     [10,60,70,80],
     [10,10,10,10]]
result=pattern(matrix)
print(result)
