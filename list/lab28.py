arr1 = [1, 1, 1, 10, 1]
s = 0
for i in range(len(arr1) - 1):
    s = arr1[i] + arr1[i+1]
print(s)
