#sequence--->it is order collection of the items--->order is the  important point to note --->so a sequence is always order
#in poython ...anything on which we can iterate are called iterable ....so if we can use it in for loop then it is a iterable
#indexing must start from zero
# all sequence type can be iterated over ---->henc all sequence type....i.e string ,list,etc  are also iterable typpe
#3 imp sequence type in python ---->List,tuples,range
# detail aboput sequences can be found at https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


#   List   :
# in python the list are enclosed in square bracket

computer_parts=["computer","monitor","keyboard","mouse","mouse mat"]     # this is list

#aas the list is sequence type we can iterate over it
for part in computer_parts:
    print(part)

# retrieving the individual item in list

print("------------------------------------")

print(computer_parts[2])

#slicing a list
print("------------------------------------")

print(computer_parts[0:3])
print(computer_parts[-1])

print("------------------------------------")

#so we can observe that the indexing and sequenceing works in same way in seqqunce as in string.....as bothg of them are string
#but theri is one differnce ......string are immutable but the list are mutable

#immutable object mean those which can not be chnaged
#immutable types buit in python are:   int,float,bool(true,false)---->sub classs of int,str (strintg),tuples,frozenset,bytes
result="Correct"
print(id(result))
result+="ish"
print(id(result))

#as the rsult of the above code shows ....when we concatenated the string with other string then.....new string was created
# and then result variable was assigne to that new string
print("----------------------")

#mutable object ---->the one those can be chnageed
#inbubit python mutable object :
#List,dict,set,byteArray
computer_parts=["computer","monitor","keyboard","mouse","mouse mat"]     # this is list
print(computer_parts)
print(id(computer_parts))
computer_parts +=["Speakers"]    # here we are mutating the list
print(computer_parts)
print(id(computer_parts))

# as the result of the above code shows ....even after the concatenatig the list....the id remain same even afer mutating it
#hence strings are immutable and list  are mutable

print("----------------------")

computer_parts=["computer","monitor","keyboard","mouse","mouse mat"]
temp_list=computer_parts#this line will make the temp_list point the existing computer)list....it iwll not create the new list
print(computer_parts)
print(temp_list)
#now changin the content of th computer_part list
computer_parts.append("headphone")
print(computer_parts)
print(temp_list)    # the temp_list changes automatically

print("----------------------")
#comman operatioj that can be perfomed on the sequence

even=[2,4,6]
odd=[1,3,5,7,9]

print(min(even))  # returnthe min element in the list
print(min(odd))
print(max(even))  # retunr the max element inthe list
print(max(odd))
print(len(even))   #lenght of the list
even.append(8)
print(even)
print("----------------------")
#here we are counting how may time trhe particular letter appeared in the string

river="mississipi"
print(river.count("s")) #will give how many time a  s letter repeaeted
print("----------------------")
#dot natation
#in above line river.count("s") ---->river is the object that we are calling the method on  ,count  is the method we wanted to call ,s is argument
print("----------------------")

