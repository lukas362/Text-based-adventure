import pygame

def start_of_story():
    print("You wake up dazed, confused and you can hear screaming voices around you. You look around and you can see goblins, orcs and humans fighting each other.")

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
        stats["Agility"] = 2
        stats["Intelligence"] = 7
        stats["Charisma"] = 4

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
        stats["Agility"] = 5
        stats["Intelligence"] = 3
        stats["Charisma"] = 4
    
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
        stats["Agility"] = 7
        stats["Intelligence"] = 4
        stats["Charisma"] = 5

    else: 
        print("Invalid selection, please select a class.")
        return role()

start_of_story()
role()

