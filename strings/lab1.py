import copy
# from collections import Counter
import collections
if __name__ == '__main__':
    data = 'To be eligible for referral bonus, you must ensure that the resume is uploaded on the My Referral portal before the first interview'
    print(data)
    split_data = data.split(' ')
    print(split_data)
    print('\n')

    deep_copy_data = copy.deepcopy(data)
    print(deep_copy_data)
    rem_space_data = deep_copy_data.replace(' ', '')
    print(rem_space_data)
    # split_rem_space_data = rem_space_data.split('') #ValueError: empty separator
    # split_rem_space_data = [rem_space_data]
    split_rem_space_data = list(rem_space_data)
    print(split_rem_space_data)

    print('\n')
    print(collections.Counter(split_rem_space_data))
    print(dict(collections.Counter(split_rem_space_data)))



