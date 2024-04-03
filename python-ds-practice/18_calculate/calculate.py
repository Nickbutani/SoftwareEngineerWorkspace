def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        return 'Invalid operation'
    
    if make_int:
        result = int(result)
    
    return f'{message} {result}'
