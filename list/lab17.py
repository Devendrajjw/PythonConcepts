# Write a function that takes two sorted lists as input and returns a new list that contains all
# elements from both input lists in sorted order. Avoid using built-in sorting functions.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# merged_list = merge_sorted_lists(list1, list2)
# # Output: [1, 2, 3, 4, 5, 6, 7, 8]

def merge_sorted_lists(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3


if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print(merge_sorted_lists(list1, list2))
