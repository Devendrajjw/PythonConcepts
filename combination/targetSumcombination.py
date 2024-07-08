# arr = [2, 3, 1, 5, 8, 9, -10, 4, 6, 5, 20]
arr = [19, 2, 3, 4, 5, 6, 1]
target = 10
nl = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            nl.append((arr[i], arr[j]))
print(nl)

