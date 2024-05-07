if __name__ == "__main__":
    try:
        with open('file001', 'r') as fh:
            while True:
                lines = fh.readline()
                # print(lines, end='')
                last_5 = fh.readlines()
                for l5 in last_5[-5:]:
                    print(l5, end='')
                if not lines:
                    break
    except FileNotFoundError:
        print("file not found")
    except IOError:
        print("error reading the file")
#
