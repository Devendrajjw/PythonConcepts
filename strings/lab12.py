# replaces all occurrences of '1' with '2' except for the last occurrence.
data = 'this is 1 sample to replace 1 only except 1 at the end 1'
if '1' in data:
    c = data.count('1')
    data = data.replace('1', '2', c-1)

print(data)
