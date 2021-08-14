pty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]  # here the numbers is list of list
print(numbers)

# iterating list of list

for numbers_list in numbers:
    print(numbers_list)
    for value in numbers_list:
        print(value)
'|' \
''
