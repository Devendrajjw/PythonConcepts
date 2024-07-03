# extract name from email

if __name__ == "__main__":
    email = input('enter email ')
    pos = email.index('@')
    print(email[:pos])
