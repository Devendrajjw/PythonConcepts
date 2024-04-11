import copy

x = [[1, 2], [11, 22]]
y = copy.deepcopy(x)

print("======== orignal deepcopy ========")
print(f'X=  {x}')
print(f'Y=  {y}')

print("======== changing Y  ========")
y[0][1] = 2020

print(f'X=  {x}')
print(f'Y=  {y}')
print("======= changing X =========")

x[0][1] = 3030

print(f'X=  {x}')
print(f'Y=  {y}')
