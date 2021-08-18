
# IF-ELSE BLOCK
name=input("pleas enter your name: ")
name=name.upper() #make the string to upper case
age=int(input("how old are u ,{}?: ".format(name)))   #int is added to covert the user input to integer from string
print(age)
if age>=18:
    print("{} is old enough to vote".format(name))
    print("please put an x in the block")
else:
    print("you are not eligible to vote")

#     # please note the : in the end of if and else statement also we dont use () to enclose the conditions as we do in java

#IF-ELIF-ELSE block

if age>=18:
    print("{} is old enough to vote".format(name))
    print("please put an x in the block")
elif age<0:
    print("please enter a valid age")
else:
    print("you are not eligible to vote")


#value comparison operator:

# less than                   <
# less than or equal to       <=
# greater than                 >
# greater than or equal to    >=
# equal to                    ==
# not equal to                !=
