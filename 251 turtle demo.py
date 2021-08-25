import turtle   #here we are importing the turtle .....which is a inbult module

turtle.forward(150)
turtle.right(90)
turtle.forward(150)

turtle.done()

#way 2

from turtle import forward   # here we are only importing the forward method from the turtle module

forward(150)   # note ....here no need to do turtle.forward

turtle.done()


#way 3
from turtle import forward,right,backward   # here we are importing the multiple methods from the turtle module

forward(150)
right(90)
backward(150)

turtle.done()

#way 4
from turtle import *   # here we are importing all method from the module turtle
#above method is not recommended
forward(150)
right(90)
backward(150)

done()