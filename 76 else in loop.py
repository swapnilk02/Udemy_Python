number=[1,45,31,12,60]

for number in numbers:
    if number %8==0:
        print("the number are unacceptable")
        break
else:
    print("all those number are fine")

#in above piece of code ....we are using else block when entire for loop executes successfully
# .i.e if first we will check the number divisible by eight ..if a so we will give message that it is unacceptable
#but if non of the number is divible by 8 then  we will execute the else block ...
# .so here we are suing the else in combination with for loop and not with if  statemnet