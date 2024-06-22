def guess_str(my_str):
    for i in range(len(my_str)-1, -1, -1):
        yield my_str[i]

c=[]
for char in guess_str("hello champ"):
    c.append(char)
print("".join(c[::-1]))
