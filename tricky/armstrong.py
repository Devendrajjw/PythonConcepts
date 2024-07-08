num = 153
sum = 0
temp = num
while temp > 0:
    # print(temp)
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
print(sum)

