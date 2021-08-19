available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}

current_choice=None
computer_parts={}   # create an empty dictionary

while current_choice!="0":
    if current_choice in available_parts:   # when use " in " dictionary...we  check key only and not the value
        chosen_part=available_parts[current_choice]   #to get the value corresponding to the given key
        if current_choice in computer_parts:
            # its already their so remove
            print(f"removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"adding {chosen_part}")
            computer_parts[current_choice]= chosen_part

        print(f"the dictionary now contain  {computer_parts}")          # here we used f string
    else:
        print("please add option from the list ")
        for key,value in available_parts.items():
            print(f"{key}:{value}")
        print("press 0 to finish")
    current_choice=input("> ")

