even=[2,4,6,8]
odd=[1,3,5,7]
even.extend(odd)   # combining two list using extend function
another_list=even
print("printing even list {}".format(even))
print("printing another list list {}".format(another_list))

# sorting
even.sort()
print(even) #pringitng sorted list
print(another_list)

even.sort(reverse=True)
print(even)

#remember sort method does not create the new list.instead it will sort the existing list and save the result in sae variale ...even in our case

#python have some built in functions......https://docs.python.org/3/library/functions.html

