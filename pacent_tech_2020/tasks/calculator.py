def sum(a, b):
	return a + b

def diff(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	return a / b


def main():
	try:
		operand1 = float(input('Enter first operand:\n'))
		operand2 = float(input('Enter second operand:\n'))
		operator = int(input('Choose operator -\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\n'))
		if (operator == 1):
			print(sum(operand1, operand2))
		elif (operator == 2):
			print(diff(operand1, operand2))
		elif (operator == 3):
			print(mul(operand1, operand2))
		elif (operator == 4):
			print(div(operand1, operand2))
		else:
			print('Invalid operation choosen.')
	except Exception:
		print('Invalid input. Input must be a number.')

try:
	main()
except Exception:
	print('Something went wrong, try again.')
	main()
