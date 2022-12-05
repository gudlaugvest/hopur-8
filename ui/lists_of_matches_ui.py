class Matches_UI:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def menu_output(self):
        print()
        print("############################")
        print()
        print(" Matches".rjust(18))
        print()
        print("1. Get list of all matches")
        print("2. Get list of played matches")
        print("3. Get list of unplayed matches")
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
                quit()
            elif command == "1":
                pass
            elif command == "2":
                pass
            
            else:
                print("Invalid input, try again!")

                