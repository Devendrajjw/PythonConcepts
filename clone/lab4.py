import copy

x = [[1, 2], [11, 22]]
y = copy.copy(x)

print("======== orignal shallow copy ========")
print(f'X=  {x}')
print(f'Y=  {y}')

print("======== changing Y  ========")
y[0][1] = 3
print(f'X=  {x}')
print(f'Y=  {y}')

print("======== changing x  ========")
x[0][1] = 1010
print(f'X=  {x}')
print(f'Y=  {y}')
