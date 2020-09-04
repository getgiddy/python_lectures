'''
a e i o u => 1 2 3 4 5

all consonants => consonant + a --- Ex. b => ba, c => ca, d => da

Take input, loop through each character in the string returned and
perform the above manipulation.

'''

def convert_vowel(letter):
	if letter in 'aA':
		return '1'
	elif letter in 'eE':
		return '2'
	elif letter in 'iI':
		return '3'
	elif letter in 'oO':
		return '4'
	elif letter in 'uU':
		return '5'

def convert_consonant(letter):
	return letter + 'a'


def main():
	consonants = 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
	vowels = 'aAeEiIoOuU'

	text = input('Enter text to translate:\n')
	
	manipulated_text = ''
	
	for letter in text:
		if letter in consonants:
			manipulated_text += convert_consonant(letter)
		elif letter in vowels:
			manipulated_text += convert_vowel(letter)
		else:
			manipulated_text += letter

	print(f'\n{manipulated_text}\n')


def greet():
	print('Welcome to our jungle language translator.\nTo exit, press CTRL + C.\n')


greet()

while True:
	try:
		main()
	except KeyboardInterrupt:
		print('\nThank you for using our translator. Until next time, bye bye.\n')
		exit()
