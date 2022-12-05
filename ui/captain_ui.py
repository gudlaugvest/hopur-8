
from ui.register_score_ui import Register_Score


class Captain_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################\n")
        print("Captain menu\n".rjust(18))
        print("1. Register score")
        print("b. Go back")
        print("q. Quit\n")



    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
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