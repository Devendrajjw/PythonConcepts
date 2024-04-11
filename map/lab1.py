def sq(n):
    return n * n

def cub(n):
    return n*n*n


n = [2, 3, 4]
func = [sq, cub]
for f in func:
    newl = list(map(f, n))
    print(newl)
