def valid_parentheses(parens):
    stack = []
    for p in parens:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                return False
            stack.pop()
    return not stack