def demo():
    for i in range(11, 20):
        yield i


gen = demo()

print(type(gen))
print(next(gen))

for g in gen:
    print(g, end=' ')
