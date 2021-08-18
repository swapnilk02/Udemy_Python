#--------------
#below is the programme where use will have number in the mind and the computer will guess it in maz 10 guess
# we will also print the num er pf the guessses neede to guess the number
low = 1
high = 1000
print("pleae think number between {} and {}".format(low, high))

input("press ENTER to start")
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My Guess is {} .should i guess higher or lower? enter h or l or c if my guess was correct: ".format(
        guess).casefold())
    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print("i got it in {} guesses".format(guesses))
        break
    else:
        print("please enter h or l or c")

    guesses+=guesses    #what we have done in thi sline is called augmented assignment ... this is same as  guesses =guesses + 1,