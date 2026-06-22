from src.role_select import show_inventory, show_stats

def menu(inventory, stats):

    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    while True:
        menu_open = input()
        if menu_open.lower() == "menu":
            selection = input(f"You open your menu, you can pick between: \n{BLUE}[1] Inventory{RESET}\n{RED}[2] Stats{RESET}\n{GREEN}[3] Exit Menu{RESET} \nYou decide to: ")
            if selection == "1" or selection == "inventory":
                show_inventory(inventory)
            elif selection == "2" or selection == "stats":
                show_stats(stats)
            elif selection == "3" or selection == "exit":
                print("You close your menu")
                break

            else: 
                print("Invalid selection, please select one of the options: \n")
                return menu(inventory, stats)