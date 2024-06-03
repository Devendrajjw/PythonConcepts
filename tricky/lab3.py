# def func1(nums):
#     sq = nums * 2
#     return sq


if __name__ == '__main__':
    data = [2, 3, 4, 5]
    # x = map(func1, data)
    x = map(lambda x : x **2, data)
    print(list(x))
