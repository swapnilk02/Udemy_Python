#if a function  defination has two parameter ,....then in that case while calling them we need to pass two arguments.
#but we can also provide default value for this parameter and in that case we can pass only one argument

def multiplication(x=4,y=5): #here we gave default value to parameter y i.e 1
    result=x*y
    return result


answer=multiplication(10,4)   # here 10,4 can be called positional argument ....ebecause argumnet at postion one will be bind two parameter at postion one and the argument at potion 2 will be bind to parameter at position 2
print(answer)
answer=multiplication(10)  #here we are passing only one argument i.e x while y has default value of 1 if not passeed while calling
print(answer)
answer=multiplication()
print(answer)
answer=multiplication(y=10)  # here we are explixitely defininng which parameter we are passing to avoid confusion if we pass only one argumentn hence it is called keyword argument
print(answer)
