
from model.tournament_model import Tournament
from datetime import datetime


class Tournament_UI:
    def __init__(self, logic_connection: Tournament):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        '''This function shows a menu bar in the tournament'''
        print()
        print("####################################")
        print()
        print("Tournament\n".rjust(23))
        print("1. Create Tournament")
        print("2. Update Tournament")
        print("b. Go Back")


    def input_prompt(self):
        '''This function shows the create tournament option and the tournament
        organizer can input name of the tournament, start date and end date. 
        The split function seperate the dot  '''
        while True:
            self.menu_output()
            print()
            command = input("Enter Command: ")
            print()
            if command == "b":
                return "b"
            elif command == "1":
                tournament = Tournament()
                tournament.name = input("Enter Tournament name: ")
                tournament.start_date = input("Enter start date(yyyy.mm.dd): ").split(".")
                while len(tournament.start_date) != 3:
                    print()
                    print("Date format is incorrect! Please Try again!")
                    tournament.start_date = input("Enter start date(yyyy.mm.dd): ")
                year, month, day =  [int(item) for item in tournament.start_date]
                tournament.start_date = datetime(year, month, day)
                tournament.end_date = input("Enter end date(yyyy.mm.dd): ").split(".")
                while len(tournament.end_date) != 3:
                    print("Date format is incorrect! Please Try again!")
                    tournament.end_date = input("Enter end date(yyyy.mm.dd): ").split(".")
                year, month, day = [int(item) for item in tournament.end_date]
                tournament.end_date = datetime(year, month, day)
                self.logic_wrapper.create_tournament(tournament)
            elif command == "2":
                the_tournament = None
                # Fáum lista af tournaments sem eru til og hvaða id þau eru
                tournament_list = self.logic_wrapper.get_all_tournaments()
                for tournament in tournament_list:
                    print("Tournament id: {} Tournament name: {}".format(tournament.id, tournament.name))
                print()
                tournament_id = input("Enter Tournament id: ")
                tournament_list = self.logic_wrapper.get_all_tournaments()
                for tournament in tournament_list:
                    if tournament.id == tournament_id:
                        the_tournament = tournament
                if the_tournament == None:
                    print("No tournament found with tournament id:{}".format(tournament_id))
                    return
                print()
                new_start_date = input("Enter new start Date(yyyy.mm.dd): ")
                new_end_date = input("Enter new end Date(yyyy.mm.dd): ")

                the_tournament.start_date = new_start_date
                the_tournament.end_date = new_end_date
                self.logic_wrapper.update_tournament(the_tournament)            
            
            else:
                print("Invalid input, please try again!")
            

'''the_match = None
        match_id = input("Enter Match id: ")
        match_list = self.logic_wrapper.get_all_match_results()
        for match in match_list:
            if match.id == match_id:
                the_match = match
        if the_match == None:
            print("No match found with match id:{}".format(match_id))
            return
        #if match_id in self.logic_wrapper.get_all_match_results():
        #match_list = self.logic_wrapper.get_all_match_results(match_id)
        
        
        print()
        new_date = input("Enter New Date(dd.mm.yyyy): ")
        
        the_match.date = new_date
        self.logic_wrapper.update_match(the_match)
        '''