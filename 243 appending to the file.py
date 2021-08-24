# creating the new file and writting something to it !!

with open("sample_1.txt","w") as title:
    print("tables upto twelve",file=title)

# now we will append the table to the file just created  and written

with open("sample_1.txt","a") as tables:  # note.....here we didnt gave full path ...the reason is we have stoed the the file sample_1 into our workspace directory itsef
    for i in range(2,13):
        for j in range(1,13):
            print(f"{j} times {i} is {i*j}",file=tables)
        print("*"*80,file=tables)



# in above code we pass second argument as "a"......which stand for append