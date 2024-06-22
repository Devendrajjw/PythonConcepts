import functools
# def some_array(a):
#     return a**2
#
# if __name__ == '__main__':
#     # ad = [11, 12, 13, 'aa', 'ee', 'dd']
#     n1 = [101, 102]
#     m1 = list(map(some_array, n1))
#     print(m1)
'''--------------'''

# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5]
# m = list(map(lambda x:x**2, arr1))
# print(m) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''--------------'''
# m1 = list(map(lambda x:x if x%2 == 0 else '', arr1))
# print(m1) # ['', 2, '', 4, '', 6, '', 8, '', 10]

'''--------------'''
# m2 = list(map(lambda x:x%2 == 0, arr1))
# print(m2) # [False, True, False, True, False, True, False, True, False, True]

'''--------------'''
# m3 = list(filter(lambda x:x%2==0, arr1))
# print(m3) # [2, 4, 6, 8, 10]

'''--------------'''
# m4 = functools.reduce(lambda a, b: a + b, arr2)
# print(m4) # 100

'''-------------'''
# m5 = functools.reduce(lambda a,b:a if a>b else b, arr2)
# print(m5) # 40

'''-------------'''
# m6 = list(map(lambda x:x**2, arr2))
# print(m6) # [1, 4, 9, 16, 25]
# m7 = list(filter(lambda x:x%2==0, m6))
# print(m7) # [4, 16]
# m8 = functools.reduce(lambda a,b:a if a>b else b, m7)
# print(m8) # 16
