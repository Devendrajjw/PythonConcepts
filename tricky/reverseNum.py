num = 123
s = ''
while num > 0:
    rev = num % 10
    s = s + str(rev)
    num //= 10
print(s)
