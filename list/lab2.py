# list1 = [5, 6, 30, 29, 50, 100]
import copy

orig = [20, 26, 33, 41, 50]
# everytime find max 2 elements and subtract it and add to the list
# at the end you should get 1 integer as output
# Sri Girinath
# 11:27
# [5,6,29,30,50]

# list2 = []
# for li in range(len(list1)-1):
#     res = list1[-1] - list1[-2]
#     list1.remove(list1[-1])
#     list2.append(res)
# print(list2)
# print(list1)

'''
[9, 8, 7, 6]
[20]
'''
list1 = copy.copy(orig)

def examp(list1):
    list2 = []
    for l in range(len(list1)-1):
        res = list1[-1] - list1[-2]
        list2.append(res)
        list1.remove(list1[-1])
        if len(list1) == 1:
            print(list1)
            if len(orig) - len(list2) == 1:
                print(list2)
                l = list2
                examp(l)


orig = [20, 26, 33, 41, 50]
list1 = copy.copy(orig)
examp(list1)

'''
[20]
[9, 8, 7, 6]
[9]
'''
