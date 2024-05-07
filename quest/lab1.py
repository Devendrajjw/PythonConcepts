a = 10
b = 20
a, b = b, a
print("a", a, "\n", "b", b)

stra = 'hello world'
listr = list(stra)
dicta = {}
for ch in (listr):
    if ch not in dicta:
        dicta[ch] = 1
    else:
        dicta[ch] += 1
print(dicta)

s = sorted(dicta)
print('s = sorted(dicta)==> ', s)
s = sorted(dicta.items())
print('sorted(dicta.items()==> ', s)
s = sorted(dicta.items(), key= lambda x:x[1])
print('sorted(dicta.items(), key= lambda x:x[1])==> ', s)
print(s[-1])
lis = []
lis.append(s[-1])
m = {k: v for k, v in lis}
print(m)
s = sorted(dicta.items(), key= lambda y:y[0])
print('sorted(dicta.items(), key= lambda y:y[0])==> ', s)
