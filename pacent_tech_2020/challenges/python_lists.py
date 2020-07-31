list_of_integers = []

'''

insert e into position i

print list_of_integers

remove e

append e

sort lis_of_integers

pop

reverse

1, 2, 3, 4

s.split(',')
'''

# n = int(input('Enter n:\n'))

# Iterate through the commands

def insert_func():
    entered = input('insert ')
    i, e = entered.split() 
    list_of_integers.insert(int(i), int(e))

def printing():
    print(list_of_integers)

def remove():
    e = int(input('remove '))
    list_of_integers.remove(e)

def append():
    e = int(input('append '))
    list_of_integers.append(e)

def sort():
    list_of_integers.sort()

def pop():
    list_of_integers.pop()

def reverse():
    list_of_integers.reverse()


commands = [
    insert_func(),
    insert_func(),
    insert_func(),
    printing(),
    remove(),
    append(),
    append(),
    sort(),
    printing(),
    pop(),
    reverse(),
    printing(),
]

def main():
    for command in commands:
        command

main()