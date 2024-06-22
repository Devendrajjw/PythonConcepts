# wap to count number of vowels and constants
def count_vow_const(sss):
    vow = 'aeiouAEIOU'
    v = c = 0
    for char in sss:
        if char.isalpha():
            if char in vow:
                v += 1
            else:
                c += 1
    return v, c


if __name__ == "__main__":
    print(count_vow_const("aeixyz"))
