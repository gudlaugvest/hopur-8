class Others_Menu_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################")
        print()
        print(" Menu".rjust(18))
        print()
        print("1. Get info on tournament")
        print("2. Register matches results")

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
                pass
            elif command == "2":
                pass
            
            else:
                print("Invalid input, try again!")