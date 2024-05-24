# user_int = int(input('enter num '))
# rev = 0
# temp = user_int
# while temp > 0:
#     d = temp % 10
#     rev = rev * 10 + d
#     temp //= 10
# if rev == user_int:
#     print("palindrome ")

# ================
# rev = ''
# while temp > 0:
#     d = temp % 10
#     rev = rev + str(d)
#     temp //= 10
# if int(rev) == user_int:
#     print("palindrome ")

a = [1, 2, 3, 4]
print(a[:])
b = a[:]
print(id(a))
print(id(b))
print(b is a)

c = a
print(id(a))
print(id(c))
print(c is a)
