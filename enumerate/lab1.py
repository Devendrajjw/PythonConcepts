data_li = ['delhi', 'bangalore', 'madras', 'kolkata', 'mp', 'up']
print(data_li)
e = enumerate(data_li)
print(e)
print(list(e))
print(dict(enumerate(data_li)))
print(dict(list(enumerate(data_li, 1))))

