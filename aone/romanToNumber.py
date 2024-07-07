d1 = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

num = 14
ot = []
for k, v in d1.items():
    while num > 0:
        if v <= num:
            ot.append(k)
            num -= v
        else:
            break
print(''.join(ot))


# {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
# 'CM': 900, 'M': 1000}
