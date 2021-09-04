# all python function retuirn somehting
#if it returns nothing .....then it will return the none

#basic intro;

def python_food():
    print("spam and eggs")

# call the function
python_food()

#printing the output of the function
print(python_food())     # thing to note iss....the implementation of the print function is in c language

print("*"*80)

# creating function having parameter....the function will centre align the input text

def centre_text(text):
    left_margin = (80-len(text)) // 2
    print(" "*left_margin, text)


centre_text("spam and eggs")
centre_text("spam,spam and eggs")


# function that accept multiple arguments
print("*"*80)
def centre_text_mul(*args):    # * here signifies the multiple arguments
    text=""
    for arg in args:
        text+=arg+" "
    left_margin = (80-len(text)) // 2
    print(" "*left_margin, text)


centre_text_mul("swapnil","pradeep","kagane")
print("*"*80)

# if we opent the defination of the print function....we can see some names parameter like sep,end,file,flush
#and those are also having the default values
#creating the fucntion with named parameter


def centre_text_mul_named(*args,sep=" ",end="\n",file=None,flush=False):    # on this line ...the sep,end,file,flush are the named parameter.....and we have also provided default parameter id user does not passa anything
    text=""
    for arg in args:
        text+=arg+sep
    left_margin = (80-len(text)) // 2
    print(" "*left_margin, text,end=end,file=file,flush=flush)

#calling the function
centre_text_mul_named("swapnil","pradeep","kagane",sep="*",end="")


#same method as above only we will retunr the value

print("*"*80)

def centre_text_return(*args,sep=" "):
    text=""
    for arg in args:
        text+=arg+sep
    left_margin = (80-len(text)) // 2
    return " "*left_margin+text    # here we are using the return keyword to return the value