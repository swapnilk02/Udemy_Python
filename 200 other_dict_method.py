d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict=dict.fromkeys(pantry_items,0)   # here the dict is the class and we are calling the fromkey method of that class,pantry_items is a list
print(new_dict)
# the fromekey method will create dictionary from an iterable..in our case we use list..... the newly created list has the key as the iterable item
# and the default values will be None...unless use define it....we defined the 0


keys=d.keys()
print(keys)

#the item variable will be the keys
for item in d:
    print(item)


#update method

d2={
    7: "lucky seven",
    10:"ten",
    3:"this is the new three",

}
d.update(d2)

for keeys,values in d.items():
    print(keeys,values)

#note ...the order remain same after updation

#values method

v=d.values()# this returns the list of the values  from the dictionary
print(v)

d[10]="new ten"  # here we are changing the original dictionary
print(v) # as we can obseve...updating the original list will automatically update the v we gopt from values method

print("four" in v)   # checking whether the list of values contain the particular values


#The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes,
# the view reflects these changes.
