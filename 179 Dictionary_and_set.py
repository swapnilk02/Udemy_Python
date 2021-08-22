#earlier we saw 2  data structure ...list and tuples ....now we will look at dictionaries and sets..
#but while list and tuples are sequece type and hence we can access the item in it using indexing.
# ...we can not do same thing with dictionaries
#so we have to use the key  to access different items
#dictionaries stores key value pair
# sets are  are unordered collection of list

#dictionaries are collection of value stored using key ....so to get the specific value we need to use unique key....

#creating a dictionaries

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',                  # here we can also use double quotes
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}


# in above definition....left side of the column is key and that to right is value

my_car=vehicles['fiesta']
print(my_car)

learner=vehicles.get("er5")
print(learner)

learner=vehicles.get("xyz",0)    # if the key is nor theit then will return the default value that user defines
# ...here we defined 0
print(learner)

#above are two ways we can get the element in the dictionaries.......
#if the key we gave does not exist in dictionary and we use get method ...it will return none...while the first way w will crash the code
# so we can use get method if we are not sure if the key exist or not
# but first way is faster than get method


#Iterating over dictionaries

for key in vehicles:
    print(key)

# so when ever we iterate over the dictionary we get the keys as result....to print value we can do something like below
print("*"*80)

for key in vehicles:
    print(key,vehicles[key],sep=": ")

#other way
print("*"*80)
for key,value in vehicles.items():
    print(key,value,sep=": ")

# when we iterate eover the dictionaries....the item will iterate in the order of the insertion


#Adding item to dictionaries
print("*"*20,"Addding item to dictionaries","*"*20)

vehicles["startfighter"]="Lockheed F-104"   # new entry added   "startfighter" os thje key  and "Lockheed F-104" is the value
for key,value in vehicles.items():
    print(key,value,sep=": ")    # checkig whether it is  their

#changing the values associated to key
print("*"*20,"changing values associated to key in dictionaries","*"*20)
vehicles["virago"]="Yamaha XV535"    # changing the value for the
for key,value in vehicles.items():
    print(key,value,sep=": ")    # checkig whether it is  their

#removing the valeus from dictionaries

print("*"*40,"removing items in dictionaries","*"*40)


#way one
del vehicles["startfighter"]   # item deleted

for key,value in vehicles.items():
    print(key,value,sep=": ")

#way 2
print("*"*100)
vehicles.pop("fiesta")   # using pop and passing the key to be removed
result=vehicles.pop("f1","Key does not exist")# here we are trying to  delete the key which does not exist...
print(result)                                # .hence we can provide the default value if key doe not exist

# the pop method will return the value corresponding to key which is removed....and if the key is not present then it will
# return the default value that user defines

for key,value in vehicles.items():
    print(key,value,sep=": ")


# just to summeries....lists are enclosed in [],tuplese are enclosed in (), and dictionaries are enclosed in {}

# we can use any object which is immutable as key for dictionary
#hence we can also use a tuple as the key for dictionary...but only limitation is the value in the tuples also should be immutable
#hence suppose if the values in teh tuple are list...then we can not use that tuple as key...as the list is immutable



#https://docs.python.org/3.9/library/stdtypes.html#dict

# for more information...follow above link