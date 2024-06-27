list_data = [11, 12, 13, 14]

print(id(list_data), list_data) # print memory address and data
cp1 = list_data.copy()
print(id(cp1), cp1) # print memory address and data

cp2 = list_data
print(id(cp2), cp2) # print memory address and data

list_data.insert(0, 'hello') # modifying main list
print(list_data) # checking for change in main list
print(cp1)      # checking change does not affect copied list

cp1.insert(1, 'world') # change done on copied list
print(cp1)
print(list_data)    # checking change does not affect main list
