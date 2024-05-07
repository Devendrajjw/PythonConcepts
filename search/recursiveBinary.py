arr = [21, 22, 19, 18, 20, 10, 11, 14, 13, 20]
search_str = 14


def binarySearch(arr, l , r, search_str):
    arr.sort()
    if r >= l:
        m = l + r // 2
        if arr[m] == search_str:
            return m
        elif arr[m] < search_str:
            return binarySearch(arr, m + 1, r, search_str)
        else:
            return binarySearch(arr, l, m -1, search_str)
    else:
        return 0


print(binarySearch(arr, 0, len(arr) - 1, search_str))

