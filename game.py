import pygame

def start_of_story():
    print("You wake up dazed, confused and you can hear screaming voices around you. You look around and you can see goblins, orcs and humans fighting each other.")

def role():
    inventory = []
    stats = {}

    selection = input("You can see Wizard staff, sword and shield and a bow and arrow on the ground next to you. What do you pick up? (wizard staff, sword and shield, bow and arrow): \n").lower()

    if selection == "wizard staff":
        inventory.append("wizard_staff")
        stats["strength"] = 4
        stats["Agility"] = 2
        stats["Intelligence"] = 7
        stats["Charisma"] = 3

    elif selection == "sword and shield":
        inventory.append("sword")
        inventory.append("shield")
        stats["strength"] = 7
        stats["Agility"] = 5
        stats["Intelligence"] = 3
        stats["Charisma"] = 4
    
    elif selection == "bow and arrow":
        inventory.append("bow")
        inventory.append("arrows")
        stats["strength"] = 5
        stats["Agility"] = 7
        stats["Intelligence"] = 4
        stats["Charisma"] = 3

    else: 
        print("Invalid selection, please select a class.")
        return role()

start_of_story()
role()

