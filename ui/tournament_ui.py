
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
<<<<<<< HEAD
            tournament.name = input("Enter Tournament name: ")
            tournament.number_of_rounds = input("Enter number of rounds: ")
            start_date = input("Enter start date(yyyy.mm.dd): ")
            tmp_start = start_date.split(".")
            if (len(tmp_start) < 3):
                pass
            start_date = datetime(tmp_start[0], tmp_start[1], tmp_start[2])
            end_date = input("Enter end date(yyyy.mm.dd): ")
            tmp_end = end_date.split(".")
            if (len(tmp_end) < 3):
                pass
            end_date = datetime(tmp_end[0], tmp_end[1], tmp_end[2])



            #day_of_start = tournament.start_date[2]
            #month_of_start = tournament.start_date[1]
            #year_of_start = tournament.start_date[0]
            #tournament.start_date = datetime(year=year_of_start, month=month_of_start, day=day_of_start)
            #day_of_end = tournament.start_date[2]
            #month_of_end = tournament.start_date[1]
            #year_of_end = tournament.start_date[0]
            #tournament.end_date = datetime(year=year_of_end, month=month_of_end, day=day_of_end)
=======
            tournament.name = input("Enter Tournament Name: ")
            tournament.number_of_rounds = input("Enter Number Of Rounds: ")
            tournament.start_date = input("Enter Start Date(yyyy.mm.dd): ")
            tournament.end_date = input("Enter End Date(yyyy.mm.dd): ")
            day_of_start = tournament.start_date[2]
            month_of_start = tournament.start_date[1]
            year_of_start = tournament.start_date[0]
            tournament.start_date = datetime(year=year_of_start, month=month_of_start, day=day_of_start)
            day_of_end = tournament.start_date[2]
            month_of_end = tournament.start_date[1]
            year_of_end = tournament.start_date[0]
            tournament.end_date = datetime(year=year_of_end, month=month_of_end, day=day_of_end)
>>>>>>> 2ce297694414425f6a4291369ad832ea58253a5b
            self.logic_wrapper.create_tournament(tournament)
        elif command == "2":
            pass
        else:
            print()
            print("Invalid input, please try again!")


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
            

