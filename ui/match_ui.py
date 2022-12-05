
class Match:

    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Match Menu".rjust(18))
        print()
        print("1. Create Match")
        print("2. Update Match")
        print("b. Go Back")

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
                self.create_match()
            elif command == "2":
                self.update_match()
            else:
                print("Invalid input, try again!")
            
    