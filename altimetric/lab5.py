def Calculator(strParam):
    # Step 1: Tokenize the input string
    tokens = []
    i = 0
    while i < len(strParam):
        if strParam[i].isdigit():
            num = 0
            while i < len(strParam) and strParam[i].isdigit():
                num = num * 10 + int(strParam[i])
                i += 1
            tokens.append(num)
            continue
        elif strParam[i] in "+-*/()":
            tokens.append(strParam[i])
        i += 1

    # Step 2: Implement the Shunting Yard algorithm to convert infix to postfix
    def precedence(op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        return 0

    output = []
    stack = []

    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    # Step 3: Evaluate the postfix expression
    eval_stack = []

    for token in output:
        if isinstance(token, int):
            eval_stack.append(token)
        else:
            b = eval_stack.pop()
            a = eval_stack.pop()
            if token == '+':
                eval_stack.append(a + b)
            elif token == '-':
                eval_stack.append(a - b)
            elif token == '*':
                eval_stack.append(a * b)
            elif token == '/':
                eval_stack.append(a // b)  # Integer division

    # The result will be the only element left in the evaluation stack
    return eval_stack.pop()

# Test cases
print(Calculator("6*(4/2)+3*1"))  # Output: 15
print(Calculator("6/3-1"))        # Output: 1
print(Calculator("2+(3-1)*3"))    # Output: 8
print(Calculator("(2-0)*(6/2)"))  # Output: 6
