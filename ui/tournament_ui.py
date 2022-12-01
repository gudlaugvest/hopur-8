
from model.tournament_model import Tournament


class Tournament_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Tournament".rjust(18))
        print()
        print("c. Continue")
        print("b. Go Back")


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter command: ")
            if command == "b":
                return "b"
            elif command == "c":
                tournament = Tournament()
                tournament.organizer_name = input("Enter name of organizer: ")
                tournament.tournament_name = input("Enter Tournament name: ")
                tournament.number_rounds = input("Enter number of rounds: ")
                #stoppa loop kiktu a tetta i kvold
                #tournament.date = date()
