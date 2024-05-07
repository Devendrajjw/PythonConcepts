# input_list = [1, 2, 3, 3, 4, 4, 5]
# output_list = remove_duplicates(input_list)
# # Output: [1, 2, 3, 4, 5]
# Write a function that takes a list as input and returns a new list with duplicates removed while preserving
# the original order of elements.
if __name__ == '__main__':
    input_list = [1, 2, 3, 3, 4, 4, 5]
    new_list = []
    for elem in input_list:
        if elem not in new_list:
            new_list.append(elem)
    print(new_list)
