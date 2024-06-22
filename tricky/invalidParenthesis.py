def isValid(ss):
    bracketdict = {')':'(', '}': '{', ']':'['}
    stack = []
    for ch in ss:
        if ch in bracketdict:
            top = stack.pop() if stack else '#'


print(isValid("()"))
