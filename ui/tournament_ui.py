
from model.tournament_model import Tournament


class Tournament_UI:
    def __init__(self, logic_connection: Tournament):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Tournament\n".rjust(18))
        print("1. Create Tournament")
        print("2. Update Tournament")
        print("b. Go Back")


    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter command: ")
        print()
        if command == "b":
            return "b"
        elif command == "1":
            tournament = Tournament()
            tournament.name = input("Enter Tournament name: ")
            tournament.number_of_rounds = input("Enter number of rounds: ")
            tournament.date = input("Enter date: ")
            self.logic_wrapper.create_tournament(tournament)
        elif command == "2":
            pass
        else:
            print()
            print("Invalid input, please try again!")
        

            

