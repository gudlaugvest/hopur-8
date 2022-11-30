


from ui.tournament_ui import Tournament_UI


class Tournament_Organizer_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Tournament Organizer".rjust(18))
        print()
        print("1. Create Tournament")
        print("2. Go to existing tournament")
        print("b. Go Back")


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                return "b"
            elif command == "q":
                return "q"
            elif command == "1":
                tournament_menu = Tournament_UI(self.logic_wrapper)
                back_method = tournament_menu.input_prompt()
                if back_method == "q":
                    return "q"
            else:
                print("Invalid input, try again!")
