def brackets(expr):
    d1 = {
        '}':'{', ']':'[', ')':'('
    }
    nwl = []
    for ele in expr:
        if ele in ['[', '{', '(']:
            nwl.append(ele)
        elif ele in d1:
            if not nwl:
                return False
            crr_symb = nwl.pop()
            if d1[ele] != crr_symb:
                return False
    if nwl:
        return False
    return True


if __name__ == '__main__':
    s = '{[()]}()'
    print(brackets(s))
    s = '{}[]()'
    print(brackets(s))
