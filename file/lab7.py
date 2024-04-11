import os

# with open('file001', 'a+') as fh:
#     for i in range(10):
#         w1 = fh.write(f'This is number {i} \n')

with open('file001', 'r') as fh:
    x = fh.readlines()
    print(x)
    print(type(x.count('number')))
    print(x.count('number'))
    # print(fh.readlines().count('number'))
    # for line in fh.readlines():
    #     print(line)

z = ['is', 'is', 'on', 'off', 'on', 'yes']
print(z)
print(z.count('on'))
