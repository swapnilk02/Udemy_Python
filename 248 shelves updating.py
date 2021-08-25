import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]
donut=["bread"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta" ] = pasta
    recipes["donut"]=donut

    for snacks in recipes:
        print(snacks,recipes[snacks])

    print("*"*100)

    # now we will change the value for the key "pasta"
    temp_list = recipes["pasta"]
    temp_list.append("butter")
    recipes["pasta"]=temp_list

    for snacks in recipes:
        print(snacks,recipes[snacks])
