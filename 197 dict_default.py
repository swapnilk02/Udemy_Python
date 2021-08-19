#the setdefault method  --->If key is in the dictionary, return its value. If not, insert key with a value of default and return default.


pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

chicken_quantity=pantry.setdefault("chicken",0)
print(f"chicken: {chicken_quantity}")

beans_quantity=pantry.setdefault("beans",0)   # this will insert the bean in the dictionary with value as 0
print(f"beans: {beans_quantity}")

ketchup_quantity=pantry.get("ketchup",0)
print(f"ketchup: {ketchup_quantity}")


print()
