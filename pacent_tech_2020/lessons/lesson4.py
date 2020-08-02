'''
#####################################################################################################

CONSOLIDATING ON LISTS

> Organising a Lists

Often, your lists will be created in an unpredictable order, because you can’t
always control the order in which your users provide their data. Although
this is unavoidable in most circumstances, you’ll frequently want to present
your information in a particular order. Sometimes you’ll want to preserve the
original order of your list, and other times you’ll want to change the origi-
nal order. Python provides a number of different ways to organize your lists,
depending on the situation.

> Sorting a List Permanently with the sort() Method

We've seen this before. During the challenge [ hack :) ]  on Friday.

Say we have a list

>>> friends = ['Michael', 'Chukwuma', 'Francis', 'Joshua']

We can use the sort function to organize this list in alphabetical using the sort()
function of the list object.

>>> friends.sort()
>>> print(friends)

The sort() method changes the order of the list permanently. The friends list
are now in alphabetical order, and we can never revert to the original order.

You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method.

>>> friends.sort(reverse=True)
>>> print(friends)

Again, the order of the list is permanently changed.

> Sorting a List Temporarily with the sorted() Function

To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function. The sorted() function lets you display your list
in a particular order but doesn’t affect the actual order of the list.

>>> friends = ['Michael', 'Chukwuma', 'Francis', 'Joshua']
>>> print(friends)
>>> print(sorted(friends))
>>> print(friends)

Notice how the list maintains its original order even after being sorted.

> Printing a List in Reverse Order

To reverse the original order of a list, you can use the reverse() method.

>>> friends = ['Michael', 'Chukwuma', 'Francis', 'Joshua']
>>> friends.reverse()
>>> print(friends)

Notice that reverse() doesn’t sort backward alphabetically; it simply
reverses the order of the list.

The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time.

> Finding the Length of a List

You can quickly find the length of a list by using the len() function. The list
in this example has four items, so its length is 4.

>>> friends = ['Michael', 'Chukwuma', 'Francis', 'Joshua']
>>> print(len(friends))

You’ll find len() useful when you need to identify the number of aliens
that still need to be shot down in a game, determine the amount of data
you have to manage in a visualization, or figure out the number of regis-
tered users on a website, among other tasks.

Note:
Python counts the items in a list starting with one, so you shouldn’t run into any 
off-by-one errors when determining the length of a list.




'''