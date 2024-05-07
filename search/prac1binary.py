def binariySearch(arr, search_str):
    arr.sort()
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == search_str:
            return mid
        elif arr[mid] < search_str:
            l = mid + 1
        else:
            r = mid - 1
    return 0


arr = [21, 22, 19, 18, 20, 10, 11, 14, 13, 20]
search_str = 11
print(binariySearch(arr, search_str))
