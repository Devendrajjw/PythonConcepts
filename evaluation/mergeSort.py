class MergeSort:
    def __init__(self):
        print('from merge sort class')

    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data)//2
            left = data[:mid]
            right = data[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1
            return data


# objMergeSort = MergeSort()
if __name__ == '__main__':
    objMergeSort = MergeSort()
    unsorted_data = [3, 2, 2.2, 5, 0, 11, 43, 12, 9]
    print(objMergeSort.merge_sort(unsorted_data))