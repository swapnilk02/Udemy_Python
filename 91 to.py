available_parts=["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat"]
current_choice="-"
computer_part=[] #empty list created

while current_choice!='0':
    if current_choice in "12345":
        print("adding {}".format(current_choice))
        if current_choice=="1":
            computer_part.append("computer")
        elif current_choice=="2":
            computer_part.append("monitor")
        elif current_choice=="3":
            computer_part.append("keyboard")
        elif current_choice=="4":
            computer_part.append("mouse")
        elif current_choice=="5":
            computer_part.append("mouse mat")
    else:
        print("please add options from list below:")
        #for part in available_parts:
           # print("{0}: {1}".format(available_parts.index(part)+1, part))

        # now we will iterate over the list in other way

        for number , part in enumerate(available_parts):     #enumerate is the function in the python which returns the pair of index and element at that index
            print("{0}: {1}".format(number+1,part))
    current_choice=input()

print(computer_part)



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Improving above code

available_parts=["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat"]

valid_choice=[]
for i in range(1,len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)

current_choice="-"
computer_part=[]

while current_choice!='0':
    if current_choice in valid_choice:
        print("adding {}".format(current_choice))
        index=int(current_choice) -1
        choosen_part=available_parts[index]
        computer_part.append(choosen_part)
    else:
        print("please add options from list below:")
        for number , part in enumerate(available_parts):     #enumerate is the function in the python which returns the pair of index and element at that index
            print("{0}: {1}".format(number+1,part))
    current_choice=input()

print(computer_part)

#--------------------------------------------------------------------------------------
# removing item from the list

available_parts=["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat"]

valid_choice=[]
for i in range(1,len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)

current_choice="-"
computer_part=[]

while current_choice!='0':
    if current_choice in valid_choice:
        index=int(current_choice) -1
        choosen_part=available_parts[index]
        if choosen_part in computer_part:
            print("Removing {}".format(current_choice))
            computer_part.remove(choosen_part)
        else:
            print("adding{}".format(current_choice))
            computer_part.append(choosen_part)
        print("your list contain {}".format(computer_part))
    else:
        print("please add options from list below:")
        for number , part in enumerate(available_parts):     #enumerate is the function in the python which returns the pair of index and element at that index
            print("{0}: {1}".format(number+1,part))
    current_choice=input()

print(computer_part)



