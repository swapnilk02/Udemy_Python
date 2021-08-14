pangram="The quick brown fox jumps over lazy dog"
letters=sorted(pangram)
print(letters)

#observe the result ....we got capital T before any small letter

#---------------------
#sorting number
numbers=[2.3,4.5,8.7,9.2,1.6]
sorted_nnumbers=sorted(numbers)
print(sorted_nnumbers)

#point to note is 1)the sorted method returns the a list which is sorted. while sort method sort existing list directly
#we should alwasy take care while choosing sort and sorted ....if w use sorted ,a new list will be created and the sorted result will be stored in it....which will take
#memory ,while if we use sort method the existing list will be modified and no new memory is neededd

missing_letters=sorted("The quick brown fox jumps over lazy dog")
print(missing_letters)

print("case sensitive sorting---------------------------")
#observe the chnages in the Positiion of T  in the result list
missing_letters=sorted("The quick brown fox jumps over lazy dog", key=str.casefold)
print(missing_letters)

print("case sensitive sorting using sort---------------------------")
# we can also sort using sort mehtod in case snsitive way
names=["Swapnil","Pradep","savita","urjita"]
names.sort(key=str.casefold)
print(names)


