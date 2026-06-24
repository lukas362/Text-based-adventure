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
        choice = input(f"You can see a {RED}Goblin{RESET} running towards you, you can see that it has a axe in it's hand and it looks like it is going to attack you. {YELLOW}How will you proceed?{RESET}\n{RED}[1] Attack the goblin{RESET}\n{BLUE}[2] Check enemy stats{RESET}\n{GREEN}[3] Run away{RESET}\nYou decide to: ")
        
        if stats:
            if choice == "1" or choice.lower() == "attack":
                damage = goblin_stats["Attack"]
                stats["total_hp"] -= damage
                print(f"You attack the {RED}Goblin{RESET} and you manage to kill it, but you got injured in the process. \n")
                print(f"You lose {damage} HP. Your current HP is now {stats['total_hp']}")
                
            elif choice == "2" or choice.lower() == "check":
                print(f"Goblin Stats: {goblin_stats} \n")
                return story(2, stats)
            
            elif choice == "3" or choice.lower() == "run":
                print(f"You run away from the {RED}Goblin{RESET}! \n")
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
        print("")