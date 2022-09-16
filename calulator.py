def calc(s):
    """Evaluate expression.
    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6
    """
    digits = s.split()

    #start from the end
    
    while digits:
        operand1 = int(digits.pop())
        operand2 = int(digits.pop())
        operator = digits.pop()
    

        if operator == "+":
            operand2 = operand1 + operand2
        elif operator == "-":
            operand2 = operand1 - operand2

        elif operator == "*":
            operand2 = operand1 * operand2

        elif operator == "/":
            operand2 = operand1 // operand2
    
    return operand2
