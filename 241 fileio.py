# basic steps involved in readin the file is 1)open the file  2)read th file 3)close the file

#way 1
#open the file
jabber=open("D:\Python Programme_ UDEMY\sample.txt","r")  # the first parameter is the path of the file,and the
# second one is saying that we will be reading the file ...


#read through the file
for line in jabber:
    print(line)

#close the file
jabber.close()

#way2


#while with  the above code we explicitely have to close the file....we can use with keyword where we dont have to close it explicitly

print("*"*100)


with open("D:\Python Programme_ UDEMY\sample.txt","r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line,end=" ")


#way3

# using the readline method

with open("D:\Python Programme_ UDEMY\sample.txt","r") as jabber:
    line=jabber.readline()
    while line:
        print(line,end="")
        line=jabber.readline()



#way 4

#using the realines method


with open("D:\Python Programme_ UDEMY\sample.txt","r") as jabber:
    lines=jabber.readlines()    #here we get the list

for line in lines:    # iterating over the list that we got
    print(line,end="")


#way 5

#using the read method

with open("D:\Python Programme_ UDEMY\sample.txt","r") as jabber:
    lines=jabber.read()  # this will return the string....and not the list of string

for line in lines:
    print(line,end="")