#thier are several different paradigm of programming .....we were using the imperative style til now
# now we will look into object oriented style....bu thte thing to note is ...this style are not completely distinct
# ....infact we used many objects inside imperative style till now

#python supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. I

#object oriented programming uses classes and method to provide the object that encapsulate both data and function that operate on that data

#in python ....when a function is part of the class....then we call it as the method
#-------------------------------------------------------------------------------------------------------------------------------
#creating class
# a class can be seen as the template from which object can be made
class Kettle(object):
    power_source="electricity"
    def __init__(self,make,price):
        self.make=make
        self.price=price
        self.on=False


kenwood=Kettle("kenwood",8.99)  # creatign the instance/object of the class kettle and naming it as kettle
print(kenwood.make)
print(kenwood.price)

kenwood.price=12.75
print(kenwood.price)

hamilton=Kettle("hemilton",14.55)# creatign the instance/object of the class kettle and naming it as hemilton

#other way of printing the result

print("models: {0.make}={0.price} ,{1.make}={1.price}".format(kenwood,hamilton))
#as we can note....once we defined the class.....we can create as many object as we want ...

kenwood.power=1    # this is very different than java...here we can add new attibute to the object of class kettle.
                    # power was not their in original class kettle
print(kenwood.power)


#from above we can conclude that instace(kenwood,hamilton) of same class can endup having the different attribute
#as we can modify the attribute like we did in above line

print(kenwood.power_source)
Kettle.power_source="atomic"    # changes the vale in class itself
print(kenwood.power_source)

kenwood.power_source="nuclear"   #will only change the value for specific instance
print(kenwood.power_source)
print(hamilton.power_source)
