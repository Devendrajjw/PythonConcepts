# Write a function that returns all possible substrings of a given string

def manipulate_str(givenStr):
    new_list = []
    for i in range(len(givenStr)):
        for j in range(i + 1, len(givenStr) + 1):
            new_list.append(givenStr[i:j])
        # return new_list # ['a', 'ab', 'abc']
    return new_list # ['a', 'ab', 'abc', 'b', 'bc', 'c']


print(manipulate_str('abc'))
