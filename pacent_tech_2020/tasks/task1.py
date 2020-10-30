'''
##########################################################################

TASK 1

> Start a new project called (python_lessons) in its own virtual environment using virtualenv.

> Open the python iteractive shell in your terminal(command prompt)

> Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”

> Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.

> Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
    Albert Einstein once said, “A person who never made a
    mistake never tried anything new.”

> Famous Quote 2: Repeat previous exercise, but this time, represent the
famous person’s name using a variable called famous_person . Then compose
your ­message and represent it with a new variable called message . Print your
message.

> Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n" , at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip() ,
rstrip() , and strip() .


'''
# 3
name = 'Eric'
print(f"Hello {name}, would you like to learn some Python today?")

# 4
print(name.lower())
print(name.upper())
print(name.title())

# 5
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

# 6
famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# 7
name = '  \t  Eric \n    '
print(name.lstrip())
print(name.rstrip())
print(name.strip())
