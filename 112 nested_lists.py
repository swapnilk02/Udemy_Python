empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]  # here the numbers is list of list
print(numbers)

# iterating list of list

for numbers_list in numbers:
    print(numbers_list)
    for value in numbers_list:
        print(value)
#------------------------------------------------------------------------------------------------------------
# processing nested list

menu = [
           ["egg", "bacon"],
           ["egg", "sausages", "bacon"],
           ["egg", "spam"],
           ["egg", "bacon", "spam"],
           ["egg", "bacon", "sausages", "spam"],
           ["spam", "bacon", "sausages", "spam"],
           ["spam", "sausages", "spam", "bacon", "spam", "tomato","spam"],
           ["spam", "egg","spam", "spam", "bacon", "spam"]
]


for meal in menu:
    if "spam" not in meal:
        print(meal)

        #printing all item if the spam is not their
        for item in meal:
            print(item)

    else:
        print("{0} has a spam score of {1}".format(meal,meal.count("spam")))