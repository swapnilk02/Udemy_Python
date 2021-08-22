import copy    # here we import the copy module to do deep copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

#things=animals.copy()  # shallow copy

things=copy.deepcopy(animals)   # deep copy
print(things["teddy"])
print(animals["teddy"])

things["teddy"].append("toy")

print(things["teddy"])
print(animals["teddy"])


#while in shallow copy ,the copy of the list was not created....in deep copy ...the copy was also crated
