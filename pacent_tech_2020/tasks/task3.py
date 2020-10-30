'''
#####################################################################################

TASK 3

Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each day's tasks to keep
them organized.

The following exercises are a bit more complex than those in previous tasks, but
they give you an opportunity to use lists in all of the ways described.

SIMPLE IS BETTER THAN COMPLEX.

> Names: Store the names of a few of your friends in a list called names . Print
each person’s name by accessing each element in the list, one at a time.

> Greetings: Start with the list you used in the previous task, but instead of just
printing each person’s name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person’s name.

> Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
keke.” :-)

> Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.

> Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
    • Start with your program from the previous task. Add a print() call at the end
    of your program stating the name of the guest who can’t make it.
    • Modify your list, replacing the name of the guest who can’t make it with
    the name of the new person you are inviting.
    • Print a second set of invitation messages, one for each person who is still
    in your list.

> More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

    • Start with your program from the previous two tasks. Add a print()
    call to the end of your program informing people that you found a bigger
    dinner table.
    • Use insert() to add one new guest to the beginning of your list.
    • Use insert() to add one new guest to the middle of your list.
    • Use append() to add one new guest to the end of your list.
    • Print a new set of invitation messages, one for each person in your list.

> Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
    • Start with your program from the previous task. Add a new line that prints a
    message saying that you can invite only two people for dinner.
    • Use pop() to remove guests from your list one at a time until only two
    names remain in your list. Each time you pop a name from your list, print
    a message to that person letting them know you’re sorry you can’t invite
    them to dinner.
    • Print a message to each of the two people still on your list, letting them
    know they’re still invited.
    • Use del to remove the last two names from your list, so you have an empty
    list. Print your list to make sure you actually have an empty list at the end
    of your program.

'''

# 1
names = ['Eric', 'Patrick', 'Emmanuel', 'Jennifer']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 2
print(f'Hello {names[0]}')
print(f'Hello {names[1]}')
print(f'Hello {names[2]}')
print(f'Hello {names[3]}')

# 3

