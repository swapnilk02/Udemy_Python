numbers={}  # this will create the the new dict and not the set
numbers_set=set()    # this is one way we can create empty set
print(numbers,type(numbers)) #
print(numbers_set,type(numbers_set))

numbers_set.add(1) # adding the element in the set

while len(numbers_set) < 4:
    next_value=int(input("please enter ur next value: "))
    numbers_set.add(next_value)

print(numbers_set)

print("*"*80)
# progrmme to remove duplicate from the list

data =["blue","red","green","yellow","green","red"]
# we need to remove the duplicate from the list

unique_data=set(data)
print(unique_data)

unique_data_sorted=sorted(set(data))    # this will return the sorted list and not the set
print(unique_data_sorted)

#programme to remove the duplicate from the list bu to preserve the order

unique_data_ordered=list(dict.fromkeys(data))   # here first we are converting the list to dictionary and then back again to list
print(unique_data_ordered)


print("*"*80)

#progeamme to remove item from set

small_ints=set(range(21))   # we are passing the range here...python will create the set for us
print(small_ints)

#removing all iten from set

# small_ints.clear()   #clearing the all items
# print(small_ints)

small_ints.discard(10) # this will not raise any exception if we try to remove the item that does not exist
small_ints.remove(11)  # this will raise the exception if we try to remove the item that does not exist
