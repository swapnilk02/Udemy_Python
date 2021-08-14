#https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
# refer the above link for details

computer_part=["computer","monitor","keyboard","mouse","mouse mat"]
print(computer_part)
computer_part[3]="trackball"   # herer we are trying to replace the item at index 3 with item trackball
print(computer_part)

print("--------------------------------------------------------------------------------------")
computer_part[3:] = ["trackball"]  #here we are trying to replace the slice from 3 to end of list with over list
print(computer_part)
