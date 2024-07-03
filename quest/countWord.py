str_data = 'is is ok'
x = list(str_data)
seen_list = []
for ch in x:
    if ch not in seen_list:
        print(f'{ch} = {x.count(ch)}')
    seen_list.append(ch)
