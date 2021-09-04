
#important part of object oriented programming is encapsulation...idea is to have a class that
# have a data and the method to process those data and dont expose the actual implememntation tpo ourside world

#object are not only way to provide encapsulatioin....theri are several other ways

class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()# even though we are calling the method from same class we need to use self word....inlike java 

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)
