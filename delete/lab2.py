str1 = 'devendra'
# op = 'd######a'
op_str = ''
for ind in range(len(str1)):
    if ind in [0, len(str1)-1]:
        op_str = op_str + str1[ind]
    else:
        op_str = op_str + '#'
print(op_str)
