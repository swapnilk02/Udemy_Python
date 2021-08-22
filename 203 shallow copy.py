animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# in below code no two entries will be created
things = animals
animals["teddy"] = "toy"
print(things["teddy"])  # the output shows that...both things,animals point to same  dictionary

print("*" * 100)

# now we will create the copy
copied_things = animals.copy()
animals["teddy"] = "poo"
print(copied_things["teddy"])
print(animals["teddy"])

# from above the shallow copy...any chnges to animal dict, will not reflect in the copied_things dict

print("*" * 100)

animals_list = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

things_list = animals_list.copy()  # shallow copy
print(things_list["teddy"])
print(animals_list["teddy"])

print()

things_list["teddy"].append("toy")
print(things_list["teddy"])
print(animals_list["teddy"])

# surprisingly above two line will print same thing even though we created shallow copy
# why this happened is....in animals_list we have key as "lion" and the corresponding value is  a list
# then we created the copy of animals_list and stored it in things_list
# what is happening in the background is ....the lion key in both the  original dict and the newly created dict are
# both referening to same list ...so mutating the list will reflect the changes to same list
# so the value for the lion key ...which is list will be stored in somewhere in the memory

# we can visualise it something like below

# lion_list = ["scary", "big", "cat"]
# elephant_list = ["big", "grey", "wrinkled"]
# teddy_list = ["cuddly", "stuffed"]
#
# animals_list = {
#     "lion": lion_list
#     "elephant": elephant_list
#     "teddy": teddy_list
# }
#
# things_list = {
#     "lion": lion_list
#     "elephant": elephant_list
#     "teddy": teddy_list
# }
