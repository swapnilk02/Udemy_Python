# symmetric difference is exactly opposite of the intersection
# it returns te item which is present in iher of the set but not in both
morning={"java","c","ruby","lisp","c#"}
afternoon={"python","c#","java","c","ruby"}

possible=morning ^ afternoon   #  symmetric difference using opearator
print(possible)

possible_1=morning.symmetric_difference(afternoon)
print(possible_1)



