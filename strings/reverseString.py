''' in multiple line using reverse function '''
# inp_str = "hello world in BTM"
# split_var = inp_str.split(" ")
# rev_var = reversed(split_var)
# join_var = " ".join(rev_var)
# print(join_var)

''' in single line '''
# inp_str = "hello world in BTM"
# print(' '.join(reversed(inp_str.split(" "))))
''' '''

''' using slice '''
# inp_str = "hello world in BTM"
# split_var = inp_str.split(" ")
# print(" ".join(split_var[::-1])) # BTM in world hello

''' using loop or list pop and append'''
# inp_str = "hello world in BTM"
# split_var = inp_str.split(" ")
# pop_var = []
# for i in range(len(split_var)):
#     pop_var.append(split_var.pop())
# print(pop_var) # ['BTM', 'in', 'world', 'hello']
# print(" ".join(pop_var)) # BTM in world hello
# print(" ". join((map(str, pop_var)))) # BTM in world hello

''' not using append or join '''
# inp_str = "hello world in BTM"
# split_var = inp_str.split(" ")
# ch_str = ""
# for i in range(len(split_var)):
#     ch_str += split_var.pop() + " "
# print(ch_str) # BTM in world hello
