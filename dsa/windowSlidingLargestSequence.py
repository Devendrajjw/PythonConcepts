# data = [1, 2, 3, 4, 5, 6, 1, 7, 2, 23, 5, 1]
data = 'abcdefagbwea'


def sw(arr):
    result = l = 0
    s1 = set()
    for i in range(len(arr)):
        while arr[i] in s1:
            s1.remove(arr[l])
            l += 1
        s1.add(arr[i])
        result = max(result, i - l + 1)
    return result


print(sw(data))


def sw(arr):
    result = l = 0
    s1 = set()
    start = 0  # To track the starting index of the longest substring

    for i in range(len(arr)):
        while arr[i] in s1:
            s1.remove(arr[l])
            l += 1
        s1.add(arr[i])

        if i - l + 1 > result:
            result = i - l + 1
            start = l  # Update the start index of the longest substring

    longest_substring = arr[start:start + result]  # Extract the longest substring
    print(f"Longest substring: '{longest_substring}' with length {result}")
    return result

print(sw(data))
