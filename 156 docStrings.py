# it is important to document the function u write....so that someone who willl use it later will get to  know what ur function do
#while in java we add comments before the function .....in python we use docString inside the function

# how we addded th doc string....on the first line after function definiton...type three double quotes and then press enter
# and then give description their
def multiplication(x,y):
    """
    Gets two number for multiplication

    enter two valid number and function returns the multiplication
    :param x:the first of two number to be multiplied
    :param y:the second of the two numbers to be multiplied
    :return: multiplication of two number
    """
    result=x*y
    return result


answer=multiplication(10,4)    #here we can hover over the multiplocation name and we can see our docString
print(answer)


# how to print the doctring for a particular function

#way1
help(multiplication)  #remember to enter the function name without paranthesis

print("*"*80)
#way2
print(multiplication.__doc__)