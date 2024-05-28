# a = 'python program to get output as a/b/c/d/e from input a/b/..../c///d/e'

a = 'a/b//..../c///d/e'
b = ''
for c in a:
    if c.isalpha():
        b += c
d = '/'.join(b)
print(d) # a/b/c/d/e



# sr = re.sub(r'[.]+',r'//',a)
# print(sr)
