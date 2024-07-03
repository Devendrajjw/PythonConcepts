def search(arr, target):
    bubllesort(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def bubllesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    lis1 = [2, 3, 1, 12, 11]
    tar = 3
    print(search(lis1, tar))
