if __name__ == '__main__':
    data = input("enter the sentence ")
    lis_data = []
    temp = ''
    for d in data:
        if d != " ":
            temp = temp + d
        else:
            lis_data.append(temp)
            temp = ""
    print(lis_data)
    lis_data.append(temp)
    print(lis_data)

# enter the sentence hi how are you
# ['hi', 'how', 'are']
# ['hi', 'how', 'are', 'you']
