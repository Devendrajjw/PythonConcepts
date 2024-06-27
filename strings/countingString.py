merastr = 'kkkzzzzzzaabbbbc'
check = ''
lll = []
for ch in merastr:

    if ch not in check:
        ct = merastr.count(ch)
        check = check + ch
        lll.append((ch, ct))
lll.sort(key=lambda el: el[1])
print(lll[-1][0])
print(check)

