
from ui.register_score_ui import Register_Score


class Captain_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        """Print out Captain Menu with options on what Captain can do"""
        print()
        print("####################################\n")
        print("Captain Menu\n".rjust(23))
        print("1. Register Score")
        print("b. Go Back")
        print("q. Quit\n")


    def input_prompt(self):
        """Get input from user"""
        while True:
            self.menu_output()
            command = input("Enter Command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                quit()
            elif command == "1":
                register_score = Register_Score(self.logic_wrapper)
                register_score.input_prompt()
            else:
                print("Invalid input, try again!")