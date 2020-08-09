'''

operations -> +, -, /, *
+ -> add
- -> sub
/ -> div
* -> mul
inputs -> operand1, operand2, operator

'''


def calculate(operand1, operand2, operator):
    if operator == 'add':
        return operand1 + operand2
    elif operator == 'sub':
        return operand1 - operand2
    elif operator == 'div':
        return operand1 / operand2
    elif operator == 'mul':
        return operand1 * operand2
    else:
        return 'Invalid input'


operand1 = int(input('Enter first number:\n'))
operand2 = int(input('Enter second number:\n'))
operator = input(
    'Choose operator:\nEnter "add" for addition\nEnter "sub" for subtraction\nEnter "div" for division\nEnter "mul" for multiplication\n'
)

result = calculate(operand1, operand2, operator)

print(result)
