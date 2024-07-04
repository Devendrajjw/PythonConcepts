strr = 'devendra'
nstr = ''
for i in range(len(strr)):
    if i in [0 , len(strr)-1]:
        nstr = nstr + strr[i]
    else:
        nstr = nstr + '*'
print(nstr)
