def role():
    # list and dictionary to store the player's inventory and stats
    inventory = []
    stats = {}

    # color codes for the different classes
    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    # vars for the different classes
    w_s = "wizard"      # w_s = short for wizard staff
    s_a_s = "warrior"   # s_a_s = short for sword and shield
    b_a_a = "archer"    # b_a_a = short for bow and arrow

    # selection of the player's class and the stats and inventory that come with it
    selection = input(f"You can see Wizard Staff, Sword and Shield and a Bow and Arrow on the ground next to you. \nWhat do you pick up?\n{BLUE}[1] Wizard Staff{RESET}\n{RED}[2] Sword and Shield{RESET}\n{GREEN}[3] Bow and Arrow{RESET} \nYou decide to pick up: ").lower()

    if selection == "1" or selection == "wizard staff":
        print(f"You chose the Wizard Staff, therefore you are a {BLUE}{w_s}{RESET}")
        inventory.append("wizard_staff")
        stats["hp"] = 25
        stats["max_hp"] = 50
        stats["stamina"] = 40
        stats["max_stamina"] = 50
        stats["mana"] = 100
        stats["max_mana"] = 100
        stats["level"] = 1
        stats["xp"] = 0

        stats["strength"] = 4
        stats["agility"] = 2
        stats["intelligence"] = 7
        stats["charisma"] = 4

    elif selection == "2" or selection == "sword and shield":
        print(f"You chose the Sword and Shield, therefore you are a {RED}{s_a_s}{RESET}")
        inventory.append("sword")
        inventory.append("shield")
        stats["hp"] = 50
        stats["max_hp"] = 100
        stats["stamina"] = 70
        stats["max_stamina"] = 80
        stats["mana"] = 10
        stats["max_mana"] = 10
        stats["level"] = 1
        stats["xp"] = 0

        stats["strength"] = 7
        stats["agility"] = 5
        stats["intelligence"] = 3
        stats["charisma"] = 4
    
    elif selection == "3" or selection == "bow and arrow":
        print(f"You chose the Bow and Arrow, therefore you are an {GREEN}{b_a_a}{RESET}")
        inventory.append("bow")
        inventory.append("arrows")
        stats["hp"] = 40
        stats["max_hp"] = 75
        stats["stamina"] = 50
        stats["max_stamina"] = 60
        stats["mana"] = 20
        stats["max_mana"] = 20
        stats["level"] = 1
        stats["xp"] = 0

        stats["strength"] = 5
        stats["agility"] = 7
        stats["intelligence"] = 4
        stats["charisma"] = 5

    else: 
        print("Invalid selection, please select one of the weapons: \n")
        return role()
    
    return inventory, stats

def show_inventory(inventory):
    print("\nThis is your inventory:")
    if inventory:
        for item in inventory:
            print(f"  - {item}")
    else:
        print("Your inventory is empty.")

def show_stats(stats):
    print("\nThese are your stats:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    else:
        print("Your stats are not set.")