'''
##################################################################################

HELLO WORLD! VARIABLE DECLARATION AND THE STD_OUT

Here is a sample line of code that can be executed in Python:

>>> print("Hello, World!")

You can just as easily store a string as a variable and then print it to stdout:

>>> my_string = "Hello, World!"
>>> print(my_string)

The above code will print Hello, World! on your screen. Try it yourself in the editor below!

Output Format

Print Hello, World! to stdout.

Sample Output:

Hello, World!

##################################################################################

THE STD_IN

Users can be allowed to provide the data for you program using the through the 'input' keyword

Sample code :

>>> name = input('Enter your name:\n')
>>> print('Hello '+name+'!')

Sample input:

Gideon

Sample output:

Hello Gideon!

###################################################################################

WORKING WITH STRINGS

"This is a string."
'This is also a string.'

'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

>>> name = "ada lovelace"
>>> print(name.title())
>>> print(name.upper())
>>> print(name.lower())

A method is an action that Python can perform on a piece of data

>>> full_name = "{} {}".format(first_name, last_name)

>>> first_name = "ada"
>>> last_name = "lovelace"
>>> full_name = f"{first_name} {last_name}"
>>> print(full_name)

>>> first_name = "ada"
>>> last_name = "lovelace"
>>> full_name = f"{first_name} {last_name}"
>>> print(f"Hello, {full_name.title()}!")

Adding and stripping whitespaces

RESEARCH - Escape sequences

>>> favorite_language = 'python '
>>> favorite_language.rstrip()

'''