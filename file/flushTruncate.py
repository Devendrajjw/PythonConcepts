with open('file001', 'r+') as fh:
    # print(fh.name)
    # print(fh.mode)
    # print(fh.seek()) # TypeError: seek expected at least 1 argument, got 0
    user_inp = input(" enter your name ")
    fh.write(user_inp + "\n")
    while True:
        line = fh.readlines()
        if not line:
            # print(fh.readline())
            print("EOF")
            break
    # fh.flush() # clear ram memory
    fh.truncate(0) # clear file, contents in file got deleted
