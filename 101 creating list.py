#way 1
empty_list=[]  #creating empty list

#way 2
even=[2,4,6,8]
odd=[1,3,5,7]


#way 3
numbers=even+odd  #creating list by concatenating  two list
print(numbers)

#way 4
sorted_number=sorted(numbers)  #creatig a sorted list using sorted method
print(sorted_number)

#way 5

digits=list("76435446")   # creating list with list method
print(digits)

#way 6
more_number=list(numbers)  #this will create the new list which will be same as "numbers" list ...but we will have two different list
                            # hence this not same as more_number=numbers....this will make more_number point to mubers and will no0t craetenew list
                            #and changes in numbers will reflect in more_numbers tooo
print(more_number)
print(more_number is numbers)  #false as the list are not same
print(more_number == numbers)# true as list are having same content

#way 7

more_number=numbers[:] #here we are suing slicing to create new list
print(more_number)

#way 8
more_number=numbers.copy()
print(more_number)