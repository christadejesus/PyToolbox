# Options Menu Module
[Features](#features) | [Requirements](#requirements) | [Usage](#usage) | [Resources](#resources) | [License](#license) | [Get in Touch](#get-in-touch)

The ```options_menu``` module provides an interactive terminal menu system for Python programs. It allows you to create an enumerated menu of options and dynamically call functions based on user input.

```bash
# As displayed in the terminal

  Option  Description  
--------  -------------
       1  Option 1     
       2  Option 2     
       3  Option 3     
       4  Exit
Enter a menu option:   
```

## Features
- **Dynamic Menu Creation:** Creates a menu with a list of options and corresponding functions.
- **User Input Validation:** Ensures the user selects a valid option.
- **Error handling:** Colorized messages provide user feedback.
- **Function Execution:** Automatically calls the function associated with the selected option.

## Requirements
To use this module, first install the **tabulate** and **colorama** libraries if you don't already have them:
```bash
pip install tabulate colorama
```
Checkout the [Resources](#resources) section for more information on these dependencies.
## Usage

### 1. Create a Menu
In your main project file (e.g., ```project.py```), you need to define a list of menu options, where each option is a tuple containing:
- A description of the option (a string).
- The name of the function to be executed when the option is selected.

( Don't forget to define the functions to be executed! )

```python
    # Define menu options
    menu_options = [
        ("Action 1", action_1),
        ("Action 2", action_2),
        ("Action 3", action_3)
    ]

    # Define functions
    def action_1():
        print("You chose action 1!")

    def action_2():
        print("You chose action 2!")

    def action_3():
        print("You chose action 3!")
```

### 2. Initialize the OptionsMenu Class
Pass the menu list to the ```OptionsMenu``` class.
```python
    menu_system = OptionsMenu(menu_options)
```

### 3. Run the Menu
Use the ```run()``` method to display the menu and handle user input.
```python
    menu_system.run()
```

### Example
```python

from options_menu import OptionsMenu

def main():
    # Define actions (these can be anything you need in your program)
    def option_1():
        print("Option 1 was triggered!")

    def option_2():
        print("Option 2 was triggered!")

    def option_3():
        print("Option 3 was triggered!")

    def exit_program():
        print("Exit program was triggered!")
        exit()

    # Define menu with descriptions and associated functions
    menu = [
        ("Option 1", option_1),
        ("Option 2", option_2),
        ("Option 3", option_3),
        ("Exit", exit_program)
    ]
    
    # Initialize the options menu
    menu_system = OptionsMenu(menu)
    menu_system.run()  # Call the menu system's main loop

if __name__ == "__main__":
    main()
```

In the example:

- Each menu option has a description and a corresponding function.
- The ```OptionsMenu``` instance is created with the list of options.
- The ```run()``` method displays the menu and calls the appropriate function based on user input.

### Resulting Options Menu
```bash
# As displayed in the terminal

  Option  Description  
--------  -------------
       1  Option 1     
       2  Option 2     
       3  Option 3     
       4  Exit
Enter a menu option:   
```

## Resources

- [Tabulate package documentation on PyPi](https://pypi.org/project/tabulate/)
- [Colorama package documentation on PyPi](https://pypi.org/project/colorama/)

## License
Copyright 2025 Christa DeJesus

This project is licensed under the MIT License. See the [LICENSE](https://github.com/christadejesus/PyToolbox/menus/options_menu/LICENSE.md) file for details.

**Third-Party Licenses:**
- tabulate (MIT License, Copyright (c) 2011-2020 Sergey Astanin and contributors)
- colorama (BSD License, Copyright (c) 2010 Jonathan Hartley)

## Get in Touch
If you have any questions, suggestions, or want to contribute to this project, feel free to reach out in this repo's Discussions or:

Email: christa.tech@outlook.com

GitHub: [github.com/christadejesus](https://github.com/christadejesus)
