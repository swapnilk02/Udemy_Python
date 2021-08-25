# note: the shelve lecture not done in depth ....need to revisit the lecture for better understanding

# shelve and the dictionary pritty much similar...the only difference is that we are incase of the shelve ..
# ..the key has to be a string and the value will be pickled
import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])


#when we use the with keyword....it will close the shelve by itseld..but we have to close it manually if we dont use
#with code for that can be somehting like below

fruit=shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
fruit['lime']="great with tequila"      #  here we are assigninng new value to a exisitng key

print(fruit["lemon"])
print(fruit["grape"])
print(fruit["lime"])

#print(fruit["limee"])    # on this line we are trying to get the value for the key which is not present in shelve..this will give the error
#to avoid getting the error if we try to get the value for the key which does not exist /.....we can use get method

#trying to get the value for the key that does not exist using get method
description=fruit.get("limee","we dont have key")    # second argument is the defalut value to be printed if key is absent n
print(description)

fruit.close()