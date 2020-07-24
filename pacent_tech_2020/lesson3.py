'''

############################################################################

PRE_CLASS FUN

The ZEN of PYTHON.
Try importing 'this' in the interactive console and read through what you find there.

>>> import this

As you go remember, SIMPLE IS BETTER THAN COMPLEX

############################################################################

WORKING WITH LISTS

What Is a List?
A list is a collection of items in a particular order.

BEST PRACTICE
When naming your list variable, it makes sense to give it plural a name as it is a collection.

In Python, square brackets ( [] ) indicate a list, and individual elements
in the list are separated by commas.

>>> friends = ['Obi', 'Francis', 'Michael', 'Timothy',]
>>> print(friends)

If you ask Python to print a list, Python returns its representation of the
list, including the square brackets.Because this isn’t the output you want your users to see, let’s learn how
to access the individual items in a list.

Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an ele-
ment in a list, write the name of the list followed by the index of the item
enclosed in square brackets.

# What do you think will be outputted?
>>> print(friends[2])
>>> print(friends[-1])

Changing, Adding, and Removing Elements

Most lists you create will be dynamic, meaning you’ll build a list and
then add and remove elements from it as your program runs its course.

Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing
an element in a list. To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have.

>>> friends[0] = 'Ekene'
>>> print(friends)

Adding Elements to a List

You might want to add a new element to a list for many reasons. For
example, you might want to make new aliens appear in a game, add new
data to a visualization, or add new registered users to a website you’ve
built. Python provides several ways to add new data to existing lists.

Appending Elements to the End of a List

The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list.

>>> friends.append('Isaac')
>>> print(friends)

The append() method makes it easy to build lists dynamically. For
example, you can start with an empty list and then add items to the list
using a series of append() calls.

>>> enemies = []
>>> enemies.append('Francis')

Building lists this way is very common, because you often won’t know
the data your users want to store in a program until after the program is
running. To put your users in control, start by defining an empty list that
will hold the users’ values. Then append each new value provided to the list
you just created.

Inserting Elements into a List

You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item.

>>> friends.insert(1, 'Ruby')
>>> print(friends)

Removing Elements from a List

Often, you’ll want to remove an item or a set of items from a list. For
example, when a player shoots down an alien from the sky, you’ll most
likely want to remove it from the list of active aliens. Or when a user
decides to cancel their account on a web application you created, you’ll
want to remove that user from the list of active users. You can remove an
item according to its position in the list or according to its value.

Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, you can
use the del statement.

>>> del enemies[0]
>>> print(enemies)

You can no longer access the value that was removed
from the list after the del statement is used.

If the item removed is not at the end, the list collapses to fill the void left
by the removed element.

>>> print(friends[2])
>>> del friends[2]
>>> print(friends[2])

Removing an Item Using the pop() Method

Sometimes you’ll want to use the value of an item after you remove it from a
list. For example, you might want to get the x and y position of an alien that
was just shot down, so you can draw an explosion at that position. In a web
application, you might want to remove a user from a list of active members
and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.

>>> popped_friend = friends.pop()
>>> print(popped_friend)

Popping Items from any Position in a List

You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in parentheses.

>>> popped_friend = friends.pop(1)
>>> print(popped_friend)

Remember that each time you use pop() , the item you work with is no
longer stored in the list.

Removing an Item by Value

Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method.

>>> friends = ['Obi', 'Francis', 'Michael', 'Timothy',]
>>> friends.remove('Obi')
>>> print(friends)

You can also use the remove() method to work with a value that’s being
removed from a list.

>>> removed_friend = friends.remove('Michael')
>>> print(removed_friend)

The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed.

'''
