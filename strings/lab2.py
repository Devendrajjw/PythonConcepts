if __name__ == '__main__':
    str1 = "Emma25 is Data scientist50 and AI Expert"
    spl = str1.split(" ")
    # print(dir(str))
    for wr in spl:
        if not wr.isalpha():
            print(wr)

