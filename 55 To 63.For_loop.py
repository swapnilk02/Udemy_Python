#python provide severla ways to  repeat a block of code
#ex for loop,while loop,list comprehension and generator expression

parrot="Norwegian Blue"
for character in parrot:  # note we had " in " keyword as condtion check also
    print(character)

#--------------------------------------------------------------------------------------------------------
#aim is to ommit the numeber and make the string that will only have the symbol
number="9,223;234:124 653,423:987"
separator=""

for char in number:
    if not char.isnumeric():
        separator=separator+char
print(separator)
#--------------------------------------------------------------------------------------------------------
#use of ranges in for looop
for i in range(1,20):     # this will print 1 to 19 and no include 20
    print("i is not {}".format(i))
#if start value is not given then default start value is 0

for i in range(10):
    print("i is not {}".format(i))
#-------
for i in range(0,10,2):   # here we have the 2 as the stepping value...(.by default is 2)
    print("i is not {}".format(i))
#-------
for i in range(10,0,-2):
    print("i is now {} after using negative stepping value".format(i))

#--------------------------------------------------------------------------------------------------------
#nested for loop

for i in range(1,10):
    for j in range(1,10):
        print("{} times {} is {}".format(j,i,i*j))
    print("-----------")
#hence we can use  for loop to iterate over a squence ...a sequence can be string ,a range any other squence other than this'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# use of "Continue"   :
shopping_list=["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_list:
    if item != "spam":
        print("Buy "+item)
print("-----")
for item in shopping_list:
    if item=="spam":
        continue
    print("Buy "+item)
# above two programme gives same output only that we are using continue clause in second code block...
# when code comes to continue block it will exist the current loop iteration and will switch to next iteration
#note if we never want to use the continue clause and just use first execution above ...then that is pefectly fine
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#use of "break"

print("using continue :\n")
for item in shopping_list:
    if item=="spam":
        continue
    print("Buy "+item)
print("using break :\n")
for item in shopping_list:
    if item=="spam":
        break
    print("Buy "+item)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#search programme using break
shopping_list=["milk","pasta","eggs","spam","bread","rice"]
item_to_find="eggs"
found_At_index=None    # we are initialising the variable to None ...it is rughly equivalent to null in java
for index in range(len(shopping_list)):   # note the len function
    if shopping_list[index]==item_to_find:
        found_At_index=index
        break
if found_At_index!=None:
    print("Found at index {}".format({found_At_index}))
else:
    print("item Not Found")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#same code can be more efficiently done like below
print("[][][][[][[][][][][")
item_to_find="eggs"
if item in shopping_list:
    print("found at index {}".format(shopping_list.index(item)))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
