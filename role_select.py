def role():
    inventory = []
    stats = {}

    selection = input("You can see Wizard staff, sword and shield and a bow and arrow on the ground next to you. What do you pick up? (wizard staff, sword and shield, bow and arrow): \n").lower()

    if selection == "wizard staff":
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

    elif selection == "sword and shield":
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
    
    elif selection == "bow and arrow":
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
        print("Invalid selection, please select one of the classes: ")
        return role()