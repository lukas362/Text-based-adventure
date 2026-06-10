def role():
    inventory = []
    stats = {}

    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    w = "wizard"
    s_a_s = "warrior"
    b_a_a = "archer"

    selection = input(f"You can see Wizard Staff, Sword and Shield and a Bow and Arrow on the ground next to you. \nWhat do you pick up?\n{BLUE}[1] Wizard Staff{RESET}\n{RED}[2] Sword and Shield{RESET}\n{GREEN}[3] Bow and Arrow{RESET} \nYou decide to pick up: ").lower()

    if selection == "1" or selection == "wizard staff":
        print(f"You chose the Wizard Staff, therefore you are a {BLUE}{w}{RESET}")
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