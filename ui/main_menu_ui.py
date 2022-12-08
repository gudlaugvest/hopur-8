from logic.logic_wrapper import Logic_Wrapper
from ui.captain_ui import Captain_UI
from ui.general_user_ui import General_User_UI
from ui.organizer_menu_ui import Organizer_Menu_UI


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
     

    def menu_output(self):
        '''This function shows the menu bar for basement open which 
        where the user has option to choose from'''
        print()
        print("####################################")
        print()
        print("Basement-Open".rjust(23))
        print()
        print("1. Tournament Orginizer")
        print("2. General User")
        print("3. Captain Menu")
        print("q. Quit")


    def input_prompt(self):
        '''This function takes you to the selected option 
        or gives error if the user inputs an incorrect information '''
        while True:
            self.menu_output()
            print()
            command = input("Enter in command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                quit()
            elif command == "1":
                organizer_menu = Organizer_Menu_UI(self.logic_wrapper)
                back_method = organizer_menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                general_user = General_User_UI(self.logic_wrapper)
                general_user.input_prompt()
            elif command == "3":
                captain_menu = Captain_UI(self.logic_wrapper)
                captain_menu.input_prompt()
            else:
                ("Invalid input, try again!")

