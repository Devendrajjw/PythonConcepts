def brackets(symbols):
    d1 = {'}': '{', ']': '[', ')': '('}
    nwl = []
    for exp in symbols:
        if exp in ['{', '[', '(']:
            nwl.append(exp)
        elif exp in d1:
            if not nwl:
                return False
            crr_symb = nwl.pop()
            if d1[exp] != crr_symb:
                return False
    if nwl:
        return False
    return True

if __name__ == '__main__':
    s = '[]{}'
    print(brackets(s))
    s = '([]{}('
    print(brackets(s))
    s = '([]{})'
    print(brackets(s))
