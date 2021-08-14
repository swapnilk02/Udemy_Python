data=[4,5,40,60,67,77,45,78,44]

print(data)

del data[0:2]
print(data)  # deleting list from start to index 2

del data[5:] # deleting the list elements from index 5 onward
print(data)

#-----------------------------------------------------------------------------------------
 # here we are trying to remmove the item out of specific range

numbers=[4,5,104,105,110,120,130,130,150,160,170,183,187,188,191,350,360]
# we only want to kep the values from the range 100 to 200
# this code will only work if the list is order in ascendgin order

min_valid=100
max_valid=200

stop=0
for index,values in enumerate(numbers):
    if values>=min_valid:
        stop=index
        break
print(stop)
del numbers[:stop]
print(numbers)

start =0

for index in range(len(numbers)-1,-1,-1):
    if numbers[index] <=max_valid:
        start=index+1
        break

print(start)
del numbers[start:]
print("final result is")
print(numbers)
#--------------------------------------------------------------------------------------------------------------
# here we are doijng same thing bug just iterating in reverse order
#while above code workonly if the list is ordered ....this code will work even if the list id not ordered
data = [104,101,4,105,308,5,107,100,306,102,108]
print(data)
min_valid=100
max_valid=200

for index in range(len(data)-1,-1,-1):
    if data[index]<min_valid or data[index]>max_valid:
        del data[index]
print(data)


#--------------------------------------------------------------------------------------------------------------
# here we are making use of the reverse function....which iterate the list in reverse order to delete item out of the range
print("------------using the reveresed function--------------")
data = [104,101,4,105,308,5,107,100,306,102,108]
print(data)
min_valid=100
max_valid=200

top_index=len(data)-1
for index,values in enumerate(reversed(data)):
    print(index,values) # check the output of the this line  and observe the index value printed
    if values<min_valid or values>max_valid:
        del data[top_index-index]
print(data)