# This file contains the menu "interface" that the player can use to check their inventory and stats. It is unlocked after the first fight.

from src.role_select import show_inventory, show_stats

def menu(inventory, stats, unlocked=False):
    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    # Check if the menu is unlocked
    if not unlocked:
        print("The menu is not available yet. Keep playing until it unlocks.")
        return

    # The menu and what the player can do in it
    while True:
        menu_open = input()
        if menu_open.lower() == "menu":
            while True:
                selection = input(f"You open your menu, you can pick between: \n{BLUE}[1] Inventory{RESET}\n{RED}[2] Stats{RESET}\n{GREEN}[3] Exit Menu{RESET} \nYou decide to: ").lower()
                if selection == "1" or selection == "inventory":
                    show_inventory(inventory)

                elif selection == "2" or selection == "stats":
                    show_stats(stats)
                    
                elif selection == "3" or selection == "exit":
                    print("You close your menu")
                    return
                else: 
                    print("Invalid selection, please select one of the options: \n")
