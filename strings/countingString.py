# merastr = 'kkkzzzzzzaabbbbc'
# check = ''
# lll = []
# for ch in merastr:
#
#     if ch not in check:
#         ct = merastr.count(ch)
#         check = check + ch
#         lll.append((ch, ct))
# lll.sort(key=lambda el: el[1])
# print(lll[-1][0])
# print(check)
#

# input = "abcde" [::-1]
# print(input)

fruits = [("apple", 5), ("banana", 15), ("cherry", 25), ("date", 3), ("elderberry", 12)]

# Dictionary comprehension to filter fruits with quantity > 10
fruit_dict = {fruit: quantity for fruit, quantity in fruits if quantity > 10}

print(fruit_dict)
