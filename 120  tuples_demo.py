#mathematical name  for irdered set od data
#in python....tuples are another sequence type along with string,lists,ranges
#tuples--->immutable
#lists---->mutable
#string----->immutable
#as the tuples are sequence type ...we can use index for accessig the member in it
t=("a","b","c")    # defining tuple
print(t)

#--------------------------------------------------------------------------
welcome="welcome to my nightmare","alice cooper",1975
bad="bad company","bad company",1974
budgie="nightfight","Budgie",1981
imelda="more mayhem","emila day",2011
metallica="ride th lighting","metallica",1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#metallica[0]="master of puppet"  # here we are replacig the item i tuple with other item aswe did in the tuple......bbut this will not work as the tuple
#are immutable unlike list

#tuple use ess memory than tuple
#seocondly as the tuple are immutable .......they maintai the integrity od the data

# we can create th list uing the tuple by following way

metallica_list=list(metallica)
print(metallica_list)

# now we can edit the list that we obtain from tuple
metallica_list[0]="master  of puppet"
print(metallica_list)

# wee can preferr usig the tuple for the things that should not change


#----------------------------------------------------------------------------
print("---------------------unpacking tuple------------------")

x,y,z=1,2,8
print(x)
print(y)
print(z)


data=1,2,8 # data here is the tuple
x,y,z=data
print(x)
print(y)
print(z)

print("unpacking list")
data=[12,13,14]   # data in this case is list .we can unpack it similar to tuple
x,y,z=data

print(x)
print(y)
print(z)

#practical uses of unpacking the tuples

#as we already sen the enumerate method....the function return a tuple

print("enumerate and tuples demo")
for index,value in enumerate("abcdefg"):
    print(index,value)
# what is happening in the above line is ....we are getting tuple as output of the enumerate method which will be
# comnibation  of index and value pair and that tuple we are unpacking and the result of which we are biding to two variable
#below code will print tuple

for t in enumerate("abcdef"):
    print(t)  # t here is a tuple
    a,b=t   # here we are unpacking the tuple
    print(a,b)

#above for loop is just the other version of earlier for loop

