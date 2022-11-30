from logic.logic_wrapper import Logic_Wrapper
from ui.player_ui import Player_UI




class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Main Menu".rjust(18))
        print()
        print("1. Player Menu")
        print("2. Tournament Orginizer Menu")
        print("3. Team Menu")
        print("4. Club Menu")
        print("5. Tournmanet Menu")


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
                menu = Player_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                pass
            else:
                ("Invalid input, try again!")

