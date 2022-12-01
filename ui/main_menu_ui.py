from logic.logic_wrapper import Logic_Wrapper
from ui.general_user_ui import General_User_UI
from ui.organizer_menu_ui import Organizer_Menu_UI


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Basement-Open".rjust(18))
        print()
        print("1. Tournament Orginizer")
        print("2. Other")
        print("q. Quit")


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter in command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                organizer_menu = Organizer_Menu_UI(self.logic_wrapper)
                back_method = organizer_menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                general_user = General_User_UI()
                general_user.input_prompt()
            elif command == "3":
                pass
            else:
                ("Invalid input, try again!")

