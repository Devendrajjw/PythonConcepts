def revWord(mystr):
    ls1 = mystr.split()
    return " ".join(ls1[::-1])


if __name__ == '__main__':
    print(revWord('I have a car'))
