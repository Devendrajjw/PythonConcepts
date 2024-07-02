num = 123
# s = ''
# while num > 0:
#     rev = num % 10
#     s = s + str(rev)
#     num //= 10
# print(s)
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print(rev)
