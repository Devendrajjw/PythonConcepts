if __name__ == '__main__':
    data = 'HackerRank.com presents "Pythonist 2".'
    newData = ''
    for d in data:
        if d.isalpha():
            if d.isupper():
                newData += d.lower()
            if d.islower():
                newData += d.upper()
        else:
            newData += d

    print(newData)
