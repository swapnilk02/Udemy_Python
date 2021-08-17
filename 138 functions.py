#using function we can avoid wrtting same code again and again....we can reuse it
#while some function return some value some will just perform some action...ex sort ,print
#difference in functiona nd method---?a function which is bound to instance of the class are called method
#hence print is the function and sort is the method
#we use the function and method in same way...only differnece is,for method we difene the object on which it will act on

#definning a function
# some rules for defining fuction name-->function name should start in small case....shoukd not start with digit ....
# we can use underscore to separate the name
#after the funtion namr we use () and then :
#here we will define the a function which will multiple two number
#function name always start with keyword "def"
#convetion is to have the two blank line after function ends

#-------------------------------
def multiple():
    result=10.5*4
    return result    # reture key word is used to define the return results of function


answer=multiple()# calling the funciton
print(answer)

#-------------------------------
# in above case we hadcoded what a function will do ...that is not very usefull...instaed we can write the dynamic function

print("functions with parameter")
#parameter are like place holder for the real  values that u may pass for function ....they are also called as formal parameter
def multipler(x,y):
    result=x*y
    return result

answer=multipler(10.2,4)
print(answer)
# argument are the values that will be used by formal parameter when we call a function
#in above call....10.2 and 4 are two argument

#---------------------