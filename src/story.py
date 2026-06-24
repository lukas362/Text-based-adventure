# This file contains the story of the game, this will be called and executed in the game.py file which acts as the main file of the "game"

from src.enemy import *
from src.role_select import *

# Variables for text colors
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def story(stage, stats=None):
    if stage == 1:
        print("You wake up dazed, confused and you can hear screaming voices around you. You look around and you can see goblins, orcs and humans fighting each other.")
    elif stage == 2:
        goblin_stats = goblin()
        choice = input(f"You can see a {RED}{enemy_goblin}{RESET} running towards you, you can see that it has a axe in it's hand and it looks like it is going to attack you. {YELLOW}How will you proceed?{RESET}\n{RED}[1] Attack the {enemy_goblin}{RESET}\n{BLUE}[2] Check enemy stats{RESET}\n{GREEN}[3] Run away{RESET}\nYou decide to: ")
        
        if stats:
            if choice == "1" or choice.lower() == "attack":
                damage = goblin_stats["Attack"]
                stats["total_hp"] -= damage
                print(f"You attack the {RED}{enemy_goblin}{RESET} and you manage to kill it, but you got injured in the process. \n")
                print(f"You lose {damage} HP. Your current HP is now {stats['total_hp']} \n")
                
            elif choice == "2" or choice.lower() == "check":
                print(f"Goblin Stats: {goblin_stats} \n")
                return story(2, stats)
            
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
                return(story(2, stats))

    elif stage == 3:
        print(f"You manage to survive the encounter with the {RED}{enemy_goblin}{RESET}, you can gratualy hear the sound of fighting and screamingaround you getting quieter and quieter and in the distance you can see a {YELLOW}group{RESET} of people approaching you.")
        print(f"The group of people intorduce themselves as the group of the {YELLOW}caravan{RESET} that you helped defend. As a gratetute over helping them they tell you about two very important things\n1. You can access you're {YELLOW}items{RESET} and {YELLOW}stats{RESET} by typing in {YELLOW}menu{RESET} in the {YELLOW}terminal{RESET}\n2. They tell you about what {YELLOW}location{RESET} that you are in and where you can move from here on out. From what you can gather you can either: \n")

        move = input(f"{BLUE}[1] Move foward{RESET}\n{RED}[2] Move left{RESET}\n{GREEN}[3] Move right{RESET}")