def checkPallindrome(st):
    i = 0
    j = len(st)-1
    while i != j:
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    data = 'civic'
    print(checkPallindrome(data))
