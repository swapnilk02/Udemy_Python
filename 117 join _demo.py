flowers=["daffodil","evening primose","hydrangea","iris","lavendar","sunflower","tiger lilly"]


separator=" | "
output=separator.join(flowers)
print(output)

# fro abbove code obswrve that we dont have to iterate over the  list..join method iterate thelist for us
#how it work is ....koin method will create the string from list and then then it will separte  all the item by a seperator we defined
# for the join to work ...all the item in the list has to be string
#in list we can store the diffent types but list are idelly for storing the homogenious items
#a=["a","b","c","d",5]
#a=["a","b","c","d"]

#bth of the above case are valid


#---------------------------------------------
print("---------------split method-------------")

panagram="the quick brown fox jump over the lazy dog"
words=panagram.split()
print(words)

numbers="9,223,036,854,775,807"
print(numbers.split(",")) # what we are oing here is sliptting the string at the places where their is  ,

#remember the split  will convert the sting to  a list while  join will convert the list to string

