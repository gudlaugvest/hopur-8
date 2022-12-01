from matches_ui import Matches_UI


class General_User_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################")
        print()
        print(" General User".rjust(18))
        print()
        print("1. Get list of matches")
        print("2. Get list of teams of matches with recorded result")
        print("3. Get status in tournament")
        print("b. Go back")
        print("q. Quit")


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                return "q"
            elif command == "1":
                matches = Matches_UI(self.logic_wrapper)
                matches.input_prompt()
            elif command == "2":
                pass
            
            else:
                print("Invalid input, try again!")