sy = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
va = [1, 5, 10, 50, 100, 500, 1000]
# this we need to take in not given
d1 = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

d2 = dict(zip(sy, va))
d1.update(d2)

sd = {k:v for k, v in sorted(d1.items(), key=lambda d1: d1[1], reverse=True)}
ot =[]
num = 8
for k, v in sd.items():
    while num > 0:
        if v <= num:
            ot.append(k)
            print(num, "-", v)
            num -= v
        else:
            break

print(''.join(ot))
