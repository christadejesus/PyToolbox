import sys
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

class OptionsMenu:
    def __init__(self, menu):
        """
        Initialize the menu with a list of options.
        Each option is a tuple of (option number, description, function)
        """
        self.menu = menu
    
    def display_menu(self):
        """Displays the menu using tabulate."""
        menu_display = [[str(idx+1), item[0]] for idx, item in enumerate(self.menu)]
        print("\n")
        # Colorama color "WHITE" here is placeholder for quick color customization
        print(Fore.WHITE + tabulate(menu_display, headers=["Option", "Description"], tablefmt="simple"))
    
    def get_option(self, selected_option):
        """Validates the user's selection and returns the associated function."""
        try:
            selected_index = int(selected_option) - 1
            if 0 <= selected_index < len(self.menu):
                return self.menu[selected_index][1]  # Return the function
            else:
                print(Fore.RED + f"Option {selected_option} is not a valid option.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")
        return None
    
    def run(self):
        """Main loop for displaying the menu and running the selected function."""
        while True:
            try:
                self.display_menu()
                selected_option = input("Enter a menu option: ")
                function_to_call = self.get_option(selected_option)
                if function_to_call:
                    function_to_call()
                else:
                    continue
            except KeyboardInterrupt:
                sys.exit()
