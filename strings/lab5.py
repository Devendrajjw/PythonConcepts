if __name__ == '__main__':
    data = 'HackerRank.com presents "Pythonist 2".'
    newData = ''
    for d in data:
        if d.isalpha():
            if d.isupper():
                newData = newData + d.lower()
            if d.islower():
                newData = newData + d.upper()
        else:
            newData = newData + d

    print(newData)
