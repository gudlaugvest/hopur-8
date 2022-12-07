
from model.tournament_model import Tournament
from datetime import datetime


class Tournament_UI:
    def __init__(self, logic_connection: Tournament):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("####################################")
        print()
        print("Tournament\n".rjust(23))
        print("1. Create Tournament")
        print("2. Update Tournament")
        print("b. Go Back")


    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter Command: ")
        print()
        if command == "b":
            return "b"
        elif command == "1":
            tournament = Tournament()
            tournament.name = input("Enter Tournament name: ")
            tournament.number_of_rounds = input("Enter number of rounds: ")
            tournament.start_date = input("Enter start date(yyyy.mm.dd): ").split(".")
            while len(tournament.start_date) != 3:
                print()
                print("Date format is incorrect! Please Try again!")
                tournament.start_date = input("Enter start date(yyyy.mm.dd): ")
            year, month, day =  [int(item) for item in tournament.start_date]
            tournament.end_date = input("Enter end date(yyyy.mm.dd): ").split(".")
            while len(tournament.end_date) != 3:
                print("Date format is incorrect! Please Try again!")
                tournament.end_date = input("Enter end date(yyyy.mm.dd): ").split(".")
            year, month, day = [int(item) for item in tournament.end_date]
            tournament.start_date = datetime(year, month, day)
            tournament.end_date = datetime(year, month, day)
            self.logic_wrapper.create_tournament(tournament)

            
"""

year = 2021
month = 12
day = 26
date = datetime(year, month, day)
date_search_from = datetime(2021, 12, 10)
date_search_to = datetime(2021, 12, 31)
if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
date_search_to = datetime(2021, 12, 1)
if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
        
"""
            

