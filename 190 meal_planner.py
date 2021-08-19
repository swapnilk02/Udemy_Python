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

recipes = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}

def add_shopping_item(data: dict,item: str,amount: int) -> None:
   if item in data:
       data[item]+=amount
   else:
       data[item]=amount

display_dict={}
for index,key in enumerate(recipes):    #note...here we are using the enumarate for a dictionary
    display_dict[str(index+1)]=key

# in above loop we are just creating the new dictionary out of the exisitng one

#creating a dictionary.....this will have the list of item and qunatitiy needed to purchase incase of sortage
shopping_list={}
while True:
    # display the menu of the recipe we know how to cook
    print("please choose your recipe")
    print("-"*80)
    for key,value in display_dict.items():
        print(f"{key} - {value}")

    choice=input(": ")
    if choice=="0":
        break
    elif choice in display_dict:
        selected_item=display_dict[choice]
        print(f"you have selected  {selected_item}")
        print("checking ingredients....")
        ingredients=recipes[selected_item]
        print(ingredients)
        # cheking whether ingredient needed are their in pantry
        for food_item,quantity_required in ingredients.items():
            quantity_in_pantry=pantry.get(food_item,0)   # if ingredient is not their ...then return 0
            if quantity_required<=quantity_in_pantry:
                print(f"\t{food_item}  is available")
            else:
                quantity_to_buy=quantity_required-quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of  {food_item}")
                add_shopping_item(shopping_list,food_item,quantity_to_buy)

for things in shopping_list.items():
    print(things)


