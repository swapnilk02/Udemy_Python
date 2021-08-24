# way 1

cities=["delhi","jaipur","mumbai","chennai","kolkata"]

with open("D:\Python Programme_ UDEMY\cities.txt","w") as city_file:    # second parameter  w is to indicate writing to file
    for city in cities:
        print(city, file=city_file)

#---------------------------------------------------------------------------------------------------------
# now we will create the new list and then write that list to same text file as earlier....this will overwrite the
# existing content of the file
cities_1=["nashik","pune","nagpur"]

with open("D:\Python Programme_ UDEMY\cities.txt","w") as city_file:    # second parameter  w is to indicate writing to file
    for city in cities_1:
        print(city, file=city_file)

