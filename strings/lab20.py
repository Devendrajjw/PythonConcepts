def rem_dup(ddd):
    nnn = ''
    for ch in ddd:
        if ddd.count(ch) == 1:
            print(f'{ch} is not duplicate')
        if ch not in nnn:
            nnn = nnn+ch
    return nnn


if __name__ == "__main__":
    print(rem_dup("ahhhelllooo"))
