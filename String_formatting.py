# note the allignment of the output

for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i,i**2,i**3))

print()
# note in 1:4 , 4 is the lenght of the value
for i in range(1,13):
        print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))

print()
for i in range(1,13):
        print("No. {0} squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))
print()


for i in range(1,13):
    print("No. {0} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

print()

print("the value of the pi is {0}".format((22/7)))   # gives the defailt precision of the 15 decimals
print("the value of the pi is {0:12}".format((22/7)))
print("the value of the pi is {0:12f}".format((22/7)))
print("the value of the pi is {0:52.50f}".format((22/7)))
print("the value of the pi is {0:62.51f}".format((22/7)))# we are saying the take precision of the 50 digit after decimal
print("the value of the pi is {0:<62.50f}".format((22/7)))




#---------------------------------------------------------------------------------

#F-STRING:used to concatenate string and int ...which we cant do normally

name="swapnil"
age=25

#print(name+"is "+age +"years old")   -->this will not work...hence we use f string

print(name+f"is {age} years old")   # note: we added the f letter before string

print(f"pi is approx {22/7 :12.50f}")

