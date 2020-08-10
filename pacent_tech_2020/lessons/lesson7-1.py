'''

####################################################################################

LESSON 7 PART 1

DICTIONARIES

> A Simple Dictionary

Consider a game featuring aliens that can have different colors and point
values. This simple dictionary stores information about a particular alien:

>>> alien = {'color': 'green', 'points': 5}
>>> print(alien['color'])
>>> print(alien['points'])

The dictionary alien stores the alien’s color and point value. The last
two lines access and display that information.

As with most new programming concepts, using dictionaries takes
practice. Once you’ve worked with dictionaries for a bit you’ll soon see how
effectively they can model real-world situations.

> Working with Dictionaries

A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.

In Python, a dictionary is wrapped in braces, {} , with a series of key-
value pairs inside the braces, as shown in the earlier example.

A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are sepa­rated
by commas. You can store as many key-value pairs as you want in a
dictionary.

> Accessing Values in a Dictionary

To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:

>>> alien = {'color': 'green'}
>>> print(alien['color'])

This returns the value associated with the key 'color' from the diction­ary alien.

> Adding New Key-Value Pairs

Dictionaries are dynamic structures, and you can add new key-value pairs
to a dictionary at any time. For example, to add a new key-value pair, you
would give the name of the dictionary followed by the new key in square
brackets along with the new value.

>>> alien['lives_left'] = 2
>>> print(alien)

> Starting with an Empty Dictionary

It’s sometimes convenient, or even necessary, to start with an empty diction­ary
and then add each new item to it. To start filling an empty dictionary,
define a dictionary with an empty set of braces and then add each key-value
pair on its own line. For example, here’s how to build the alien dictionary
using this approach:

>>> alien = {}
>>> alien['color'] = 'green'
>>> alien['points'] = 5
>>> alien['lives_left'] = 2
>>> print(alien)

> Modifying Values in a Dictionary

To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with
that key. For example, consider an alien that changes from green to yellow
as a game progresses:

>>> alien = {'color': 'green'}
>>> print(f"The alien is {alien['color']}.")
>>> alien['color'] = 'yellow'
>>> print(f"The alien is now {alien['color']}.")

> Removing Key-Value Pairs

When you no longer need a piece of information that’s stored in a diction­
ary, you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to remove.
For example, let’s remove the key 'points' from the alien dictionary along
with its value:

>>> alien = {'color': 'green', 'points': 5}
>>> print(alien)
>>> del alien['points']
>>> print(alien)

> Using get() to Access Values

Using keys in square brackets to retrieve the value you’re interested in
from a dictionary might cause one potential problem: if the key you ask for
doesn’t exist, you’ll get an error.
Let’s see what happens when you ask for the point value of an alien that
doesn’t have a point value set:

>>> alien = {'color': 'green', 'speed': 'slow'}
>>> print(alien['points'])

This results in a traceback, showing a KeyError

'''