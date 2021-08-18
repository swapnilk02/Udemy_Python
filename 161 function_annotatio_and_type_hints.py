# function annotation make it clear what  kind of the vslues ur  functions can accept and what they return.

def multiplication(x: float,y: float) -> float:    # here we are providing the functional annotation and defining what will be our parameter types and what will be the return type our function
    result=x*y                                     # this will be usefull while the time of calling
    return result

# supppose if we replace the float at above code with string....still the code works fine...

answer=multiplication(10,2)  # while typing this thing u will get the expected data type that we difined in above function signature
print(answer)


print("*"*80)

# use of functional annotation with default value


def multiplication(x: float = 4,y: float = 5) -> float:   # here we are defining the defaut values and functional annotation both  at a time...note  the spave before and after the = sign
    result=x*y
    return result


print(multiplication())   # calling the function using the default values