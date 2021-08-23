set_1={1,2,3,5,6,7}
set_2={4,2,5,6,10}

#using themethod
set_diff=set_1.difference(set_2)
print(set_diff)

set_diff_1=set_2.difference(set_1)
print(set_diff_1)

# using operator

set_diff_2=set_1-set_2
print(set_diff_2)

set_diff_3=set_2-set_1
print(set_diff_3)