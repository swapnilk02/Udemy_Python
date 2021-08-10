import random     #random is the inbuit module (similar to package in java) in python
heightest=10
answer=random.randint(1,heightest)

print("please guess the number between 1 to {}: ".format(heightest))
guess=int(input())

if guess==answer:
    print("u got it first time")
else:
    if guess<answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess==answer:
        print("well done guessed it correctly")
    else:
        print("sorry u didnt guessed correctly second time either.the number was {}".format(answer))

#-----------------------------------------------------------------------------------