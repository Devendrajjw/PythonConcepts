str_data = 'aaaabbbzzzzzll'
seen = []
for elem in str_data:
    if elem not in seen:
        print(f'{elem} {str_data.count(elem)}')
        seen.append(elem)
