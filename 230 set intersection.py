#first we will generate the set using the iterable

multiple_2=set(range(0,50,2))
multiple_3=set(range(1,50,3))

print()

print(multiple_3.intersection(multiple_2))  #inteersection using the method
print(multiple_2 & multiple_3)  # intersection using & operator

