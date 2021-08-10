string1="he's"
string2="probably "
string3="pining "
string4="for the "
string5="fjords"
print(string1+string2+string3+string4+string5)
print("he's" "probably " "pining ""for the ""fjords")

#-------------------------------
print("Hello " *5)
#print("Hello " *5+4)   #---<not possible
print("Hello "*(5+4))  # will print 9 times
print("Hello "* 5+"4")

#-------------------------------
# to check  whether a string is substring of other  string

today="friday"
print("fri" in today)
print("day" in today)
print("rid" in today)
print("sat" in today)
