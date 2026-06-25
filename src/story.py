# This file contains the story of the game, this will be called and executed in the game.py file which acts as the main file of the "game"

from src.enemy import *
from src.role_select import *
from src.menu import menu

# Variables for text colors
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PURPLE = "\033[35m"
RESET = "\033[0m"

def story(stage, stats=None, inventory=None):
    if stage == 1:
        print("You wake up dazed, confused and you can hear screaming voices around you. You look around and you can see goblins, orcs and humans fighting each other.")
    if stage == 2:
        goblin_stats = goblin()
        choice = input(f"You can see a {RED}{enemy_goblin}{RESET} running towards you, you can see that it has a axe in it's hand and it looks like it is going to attack you. {YELLOW}How will you proceed?{RESET}\n{RED}[1] Attack the {enemy_goblin}{RESET}\n{BLUE}[2] Check enemy stats{RESET}\n{GREEN}[3] Run away{RESET}\nYou decide to: ")
        
        if stats:
            if choice == "1" or choice.lower() == "attack":
                damage = goblin_stats["Attack"]
                xp = goblin_stats["xp"]
                stats["total_hp"] -= damage
                stats["xp"] += xp
                print(f"You attack the {RED}{enemy_goblin}{RESET} and you manage to kill it, but you got injured in the process. \n")
                print(f"You lose {damage} HP. Your current HP is now {stats['total_hp']}. You got {stats['xp']}{xp_given} from defeating the {RED}{enemy_goblin}{RESET} \n")
                
            elif choice == "2" or choice.lower() == "check":
                print(f"Goblin Stats: {goblin_stats} \n")
                return story(2, stats, inventory)
            
            elif choice == "3" or choice.lower() == "run":
                print(f"You run away from the {RED}{enemy_goblin}{RESET}! \n")
                if choice == "3" or choice.lower() == "run":
                    print(f"{RED}You're story ends here \n{RESET}")

                    choice = input(f"You can either: \n{BLUE}[1] Restart the game{RESET} \n{GREEN}[2] Exit the game:{RESET} \nYou decide to: ")
                    if choice == "1":
                        return "restart"
                    if choice == "2":
                        quit()
            else:
                print("Invalid selection, please select one of the options: \n")
                return story(2, stats, inventory)

    if stage == 3:
        print(f"You manage to survive the encounter with the {RED}{enemy_goblin}{RESET}, you can gratualy hear the sound of fighting and screamingaround you getting quieter and quieter and in the distance you can see a {YELLOW}group{RESET} of people approaching you.")
        print(f"The group of people intorduce themselves as the group of the {YELLOW}caravan{RESET} that you helped defend. As a gratetute over helping them they tell you about two very important things.")
        print(f"1. You can access you're {YELLOW}items{RESET} and {YELLOW}stats{RESET} by typing in {YELLOW}menu{RESET} in the {YELLOW}terminal{RESET}\n2. They tell you about what {YELLOW}location{RESET} that you are in and where you can move from here on out. From what you can gather you can either: \n")
    
    if stage == 4:
        move_foward = input(f"{BLUE}[1] Move foward{RESET}\n{RED}[2] Move left{RESET}\n{GREEN}[3] Move right{RESET}\n{PURPLE}[4] Open menu{RESET} \nYou decide to: ")

        if move_foward == "1" or move_foward.lower() == "move forward":
            dog_stats = white_dog()
            print(f"You decided to {YELLOW}move foward{RESET} \n")
            print(f"When walking foward you can see a {YELLOW}small White pixel Dog{RESET}, It seems friendly at first, but as you continue walking foward it starts a {RED}fight with you{RESET}")
            
            while True:
                dog_encounter = input(f"You got draged into a {RED}fight{RESET} with the {YELLOW}{enemy_dog}{RESET}\n{RED}[1] Attack the {enemy_dog}{RESET}\n{BLUE}[2] Check enemy stats{RESET}\n{GREEN}[3] Run away{RESET}\nYou decide to: ")

                if dog_encounter == "1" or dog_encounter.lower() == "attack":
                    damage = dog_stats["Attack"]
                    xp = dog_stats["xp"]
                    stats["total_hp"] -= damage

                    print(f"You attack the {RED}{enemy_dog}{RESET}, but you didn't manage to hurt it much \n")
                    print(f"You lose {damage} HP. Your current HP is now {stats['total_hp']}. \n")
                    print(f"You {RED}died{RESET} \n")
                    print(f"{RED}You're story ends here \n{RESET}")
                    choice = input(f"You can either: \n{BLUE}[1] Restart the game{RESET} \n{GREEN}[2] Exit the game:{RESET} \nYou decide to: ")
                    if choice == "1":
                        return "restart"
                    if choice == "2":
                        quit()
                    break
                        
                elif dog_encounter == "2" or dog_encounter.lower() == "check":
                    print(f"White Dog Stats: {dog_stats} \n")
                    continue
                    
                elif dog_encounter == "3" or dog_encounter.lower() == "run":
                    print(f"You tried to away from the {RED}{enemy_dog}{RESET}, but it caught up with you and {RED}killed you{RESET} \n")
                    choice = input(f"You can either: \n{BLUE}[1] Restart the game{RESET} \n{GREEN}[2] Exit the game:{RESET} \nYou decide to: ")
                    if choice == "1":
                        return "restart"
                    if choice == "2":
                        quit()
                    break
                else:
                    print("Invalid selection, please select one of the options: \n")
                    continue

        elif move_foward == "2" or move_foward.lower() == "move left":
            print(f"You enter a old looking church, inside of the church you find a {YELLOW}key{RESET} \n")
            inventory.append("key")
            pick_up_necklaces = input(f"You can also see a strange looking {YELLOW}necklaces{RESET} \n{BLUE}[1] Pick up necklaces{RESET} \n{GREEN}[2] Leave necklaces{RESET}\nDo you want to pick up the {YELLOW}necklaces?{RESET}: ")
            
            if pick_up_necklaces == "1" or pick_up_necklaces.lower() == "pick up necklaces":
                inventory.append("necklaces")
                print("You picked up the necklaces")
                return story(4, stats, inventory)
            elif pick_up_necklaces == "2" or pick_up_necklaces.lower() == "leave necklaces":
                print("You decided to leave the necklaces")
                return story(4, stats, inventory)
            
        elif move_foward == "3" or move_foward.lower() == "move right":
            if  "key" in inventory and "necklaces" in inventory:
                print("You managed to enter the Castle with the key and the power of the necklaces protection you. This is the end of the story...for now")

                print(f"{YELLOW}Thank you for playing! \n{RESET}")
                choice = input(f"You can either: \n{BLUE}[1] Restart the game{RESET} \n{GREEN}[2] Exit the game:{RESET} \nYou decide to: ")
                if choice == "1":
                    return "restart"
                if choice == "2":
                    quit()
                print(f"{RED}You're story ends here \n{RESET}")

            if  "key" not in inventory and "necklaces" in inventory:
                print("You made your way to the castle, but couldn't open the gate")
                return story(4, stats, inventory)

            if "key" in inventory and "necklaces" not in inventory:
                print(f"You made your way to the castle, you open the gate. but you're vision goes dark and you {RED}die{RESET}")
                choice = input(f"You can either: \n{BLUE}[1] Restart the game{RESET} \n{GREEN}[2] Exit the game:{RESET} \nYou decide to: ")
                if choice == "1":
                    return "restart"
                if choice == "2":
                    quit()
                print(f"{RED}You're story ends here \n{RESET}")

            if "key" not in inventory and "necklaces" not in inventory:
                print("You made your way to the castle, but couldn't open the gate")
                return story(4, stats, inventory)

        elif move_foward == "4" or move_foward.lower() == "menu":
            menu(inventory, stats, unlocked=True)
            return story(4, stats, inventory)
        else:
            print("Invalid selection, please select one of the options: \n")
            return story(4, stats, inventory)