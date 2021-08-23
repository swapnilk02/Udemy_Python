# sets are unordered collection of object with no diplicate item
# set have no order
# their is no way to access individual element of set
# the elements in the set are unique
# hence suppose we convert the list to set will automatically remove the duplicate
#set are faster than list.......as set uses the hashcode

farm_animal={'cow', 'sheep' , 'hen','horse','goat'}
print(farm_animal)

# above declared the set farm_animal,while we also used the curly bracket for dictionary,the difference is we dont
# have key value pair here ,...this signifies that it is set

for animals in farm_animal:
    print(animals)


# running the above code again and again will print the set in different order
# hence set are unordered

# as the set are unordered........we can not use indexing to access particular members