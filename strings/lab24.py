# # Check for Balanced Brackets in an expression (well-formedness)
# def bracket(expr):
#     stack = []
#     for ch in expr:
#         if ch in ["(","{","["]:
#             stack.append(ch)
#         else:
#             if not stack:
#                 return False
#             current_ch = stack.pop()
#             if current_ch == '(':
#                 if ch != ')':
#                     return False
#                 if current_ch == '{':
#                     if ch != '}':
#                         return False
#                 if current_ch == '[':
#                     if ch != ']':
#                         return False
#     if stack:
#         return False
#     return True
#
#
# if __name__ == '__main__':
#     b1 = "[)"
#     print(bracket(b1))

# # Check for Balanced Brackets in an expression (well-formedness)
# def bracket(expr):
#     stack = []
#     bracket_map = {')': '(', '}': '{', ']': '['}  # Map closing brackets to opening brackets
#
#     for ch in expr:
#         if ch in ["(", "{", "["]:  # If the character is an opening bracket, push it to the stack
#             stack.append(ch)
#         elif ch in bracket_map:  # If the character is a closing bracket
#             if not stack:  # If stack is empty, return False
#                 return False
#             current_ch = stack.pop()  # Pop the top element from the stack
#             if bracket_map[ch] != current_ch:  # Check if the popped element matches the corresponding opening bracket
#                 return False
#
#     if stack:  # If there are any remaining opening brackets in the stack, return False
#         return False
#     return True
#
#

def bracket(s1):
    stack = []
    dict_sym = {')': '(', ']': '[', '}': '{'}
    for ch in s1:
        if ch in ['(', '[', '{']:
            stack.append(ch)
        elif ch in dict_sym:
            if not stack:
                return False
            current_ch = stack.pop()
            if dict_sym[ch] != current_ch:
                return False
    if stack:
        return False
    return True



if __name__ == '__main__':
    b1 = "(([)])"
    print(bracket(b1))
    b2 = "({[]})"
    print(bracket(b2))


