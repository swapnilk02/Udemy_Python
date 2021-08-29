# note date and time module done perfectly ....need to revisit

# their are two complexity involved in dealing with date time...1)localisation 2)day light saving

#python standard library provides  3 modules to deal with the  date and time
#1)time 2)date & time 3)calendar   ...three modules

import  time
print(time.gmtime(0))
print(time.localtime())   #will return the local date and time in tuple format
print(time.time())


time_here=time.localtime()
print(time_here)
print("year :",time_here[0])
print("month :",time_here[1])
print("day :",time_here[2])


