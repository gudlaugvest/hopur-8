class Captain_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################")
        print()
        print(" Captain menu".rjust(18))
        print()
        print("1. Register final match")
        print("q. Quit")



    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                return "q"
            elif command == "1":
                pass           
            
            else:
                print("Invalid input, try again!")