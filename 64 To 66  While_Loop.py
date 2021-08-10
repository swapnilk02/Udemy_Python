#while loops basic code
i=0
while i<10:
    print("i is not {}".format(i))
    i+=1    #equivalent to i=i+1

#---------------------------------------------------------------------------------------------------
available_exits=["north","south","east","west"]
chosen_exit=""
while chosen_exit not in available_exits:
    chosen_exit=input("please choose direction: ")

print("arent u glad u are out of the room")

#one of the main use of the while loop is  when u cant predict
# in advance how mamny time loop will execute

#------------------------------------------------------------------------------------------------------------------------------
#while loop with break example:
available_exits=["north","south","east","west"]
chosen_exit=""
while chosen_exit not in available_exits:
    chosen_exit=input("please choose direction: ")
    if chosen_exit.casefold()=="quit":
        print("Game Over")
        break
print("arent u glad u are out of the room")
#------------------------------------------------------------------------------------------------------------------------------