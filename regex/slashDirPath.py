import re
path1 = 'c:/devendra/users'
path2 = '/a/b/.../c//d'
# p2 = path2.replace(r'.','')
# print(p2)
x = re.sub(r'\.|(\/)', '', path2)
# print('/'.join(x.split(' ')))
x = "/".join(list(x))
print(path1+"/"+x)
