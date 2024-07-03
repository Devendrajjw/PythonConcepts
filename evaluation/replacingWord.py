def replace(data, old, new):

# creating the list to store the start indices
    occurrences=[i for i in range(len(data)) if data.startswith(old, i)]
    if len(occurrences)<=1:
        return data

# using for loop through all occurances except the last one
    for i in occurrences[:-1]:
        data=data[:i]+new+data[i+len(old):]
    return data

# given the string and replace 1 with 2
data='this is 1 sample to replace 1 only except 1 at the end 1'
result=replace(data, '1','2')
print(result)
