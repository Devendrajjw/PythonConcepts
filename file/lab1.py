import os

# with open('file001.log', 'x') as fh:
#     print('created file')

find_file = 'file001'
# print(os.path.abspath(find_file))
# for root, dirs, files in os.walk(r'C:\Users\DJHUNJHU\PycharmProjects\Lab2\file'):
for root, dirs, files in os.walk(r'C:\Users'):
    # print(root)
    for name in files:
        if name == find_file:
            print(os.path.abspath(os.path.join(root, name)))
