def binary(arr, target):
    # arr = sorted(arr)
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

if __name__ == '__main__':
    arr = [10, 11, 14, 13, 20]
    target = 13
    print(binary(arr, target))
