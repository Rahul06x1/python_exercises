def evaluate(n):
    stack = []
    for i in n:
        if i in ['+']:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(operand_1 + operand_2)
        else:
            stack.append(int(i))

    return stack.pop()