def plaindrome(ss):
    s = ss.lower().replace(" ","")
    if s == s[::-1]:
        return True
    return False


if __name__ == "__main__":
    # print(plaindrome("A man a plan a canal Panama"))
    print(plaindrome('AbcD dCBa'))
