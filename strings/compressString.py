def compress_string(s):
    new_list = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            new_list.append(s[i - 1] + str(count))
            count = 1
    new_list.append(s[-1] + str(count))

    new_list_string = ''.join(new_list)
    if len(new_list_string) < len(s):
        return new_list_string
    else:
        return s


# Test cases
s1 = "aabcccccaaa"
s2 = "abcdef"

print(compress_string(s1))  # Output: "a2b1c5a3"
print(compress_string(s2))  # Output: "abcdef"
