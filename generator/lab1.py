def dem():
    for i in range(10):
        yield i


gen = dem()
print(type(gen))
print(next(gen))
for g in gen:
    print(g, end=' ')
