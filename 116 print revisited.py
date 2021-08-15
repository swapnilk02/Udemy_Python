# here we willl see how the print function is used in differnt way

name ="tim"
age=10

print(name,age,"python",2020)   #giving multiple argument
print(name,age,"python",2020,sep=", ")  # we are exlusively defineing the separator betweeen arguments....by default it is a blacnk space

#--------------------------------------------------------------------
#check the difference in two for loop
names=["swapnil","urjita","pradeep","savita"]
for name in names:
    print(name)

for name in names:
    print(name,end=" ")


#


