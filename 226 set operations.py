# union of two set


farm_animal={"sheep","hen","cow","horse","goat"}

wild_animal={"lion","elephant","tiger","goat","panther","horse"}


all_animals=farm_animal.union(wild_animal)
print(all_animals)

all_animals_1=farm_animal | wild_animal   # instead of using the method we used the pipe operator here....the result will remain the same
print(all_animals_1)

# the practical application of the union

print("*"*80)

# drugs
amlodipine = ("amlodipine", "Blood pressure")
buspirone = ("buspirone", "Anxiety disorders")
carbimazole = ("carbimazole", "Antithyroid agent")
citalopram = ("citalopram", "Antidepressant")
edoxaban = ("edoxaban", "anti-coagulant")
erythromycin = ("erythromycin", "Antibiotic")
lusinopril = ("lusinopril", "High blood pressure")
metformin = ("metformin", "Type 2 diabetes")
methotrexate = ("methotrexate", "Rheumatoid arthritis")
paracetamol = ("paracetamol", "Painkiller")
propranol = ("propranol", "Beta blocker")
simvastatin = ("simvastatin", "High cholesterol")
warfarin = ("warfarin", "anti-coagulant")

# Drugs that shouldn't be taken together
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]
med_to_watch=set()

for interaction in adverse_interactions:
    #way 1
#    med_to_watch=med_to_watch.union(interaction)     # this isnt the effic9ient way for union .....as this will create the new set everytime aroung the loop
    #way 2
#    med_to_watch=med_to_watch | interaction
    #way 3
    med_to_watch.update(interaction)  # this is efficient way as the this will not creat the new set every time
    #way 4
#    med_to_watch |= interaction    # same as above just use operation instead of undate method

print(sorted(med_to_watch))

#
med_to_watch.update(*adverse_interactions)    # here we are doint the unpacking usig the * 
print(med_to_watch)
