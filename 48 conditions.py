# #use of "and" and "or"
# age= int(input("how old are u ?: "))
# if age>=16 and age<=65:
#     print("have good daya at work")
#
#     #doing same code with other implementation
#
# if 16<=age<=65:
#     print("have a great day at work")
# else:
#     print("enjoy freetime!!")
#
# print("-"*80)
#
# if age<16 or age>65:
#     print("enjoy freetime!!")
# else:
#     print("have a great day at work")
#
# #note
# #while comparison the condition using and the python will stop checking as sson as it finds a condtiton that is false
# #while checking condition using or ,it will stop as soon as it find a true condition
#
# #Boolean values
# #True and False are two constant defined by python .these are case sensitive ...(hence T and F has to be in capital)
#
# #to reverse the value of the boolean we use "not" keyword
# b=False
# print(b)
# print(not b)
# #------------------------------------------------------------------------------------------------------------
#
#
# day="monday"
# temparature=30
# raining=True
# if (day=="saturday" and temparature>27 ) or not raining:    # remember we should use paranthesis to make code readble if we
#                                                             # are using multiple and ,or in same expression
#     print("go swimimng")
# else:
#     print("learn python")
#
# # few things which are consider as false in the python
#     # 1)constant defined as false or None
#     # 2)zero of any numeric type decimal or fractional
#     # 3)empty sequence and collections : ex range(0),"",{},(),set()
# #----------
# if 0:
#     print("True")
# else
#     print("false")
# ----------
# name=0    # if we give the name = 0 or name ="" then in that case name will be treated as false
# if name:
#     print("Hello {}".format(name))
# else:
#     print("are u a man with no name ??")
# #run this programme with  not giving any input....i.e an empty screen

#-------------------------------------------------------------
#  use of "in"
parrot ="Norwegien blue"
letter=input("entre a character: ")
if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("i dont need that letter")

#--------------------
#use of "not in"
parrot ="Norwegien blue"
letter=input("entre a character: ")
if letter not in parrot:
    print("i dont need that letter")
else:
    print("{} is in {}".format(letter,parrot))
