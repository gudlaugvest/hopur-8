
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
        #print("2. Update Tournament")
        print("b. Go Back")


    def input_prompt(self):
        '''This function shows the create tournament option and the tournament
        organizer can input name of the tournament, start date and end date  '''
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
                pass
            else:
                print("Invalid input, please try again!")
            
            '''update_tournamnet = self.logic_wrapper.update_tournament(tournament)
            for info in update_tournamnet:
                print(info) 
        while True:
            self.menu_output()
            print()
            command = input("Enter Command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                return "q"
            elif command == "1":
                self.create_tournament_menu()
            elif command == "2":
                self.update_tournament_menu()
            else:
                print()
                print("Invalid input, please try again!")    
    


    def create_tournament_menu():
        pass
        print()
        print("####################################")
        print()
        print("Create Tournament".rjust(23))
        print()

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


    def update_tournament_menu():
        print()
        print("####################################")
        print()
        print("Update Tournament".rjust(23))
        print()
        print("Enter id of the tournament you want to change")
        print()

        the_tournament = None
        tournament_id = input("Enter tournament id: ")
        tournament_list = self.logic_wrapper.get_all_tournaments()
        for tournament in tournament_list:
            if tournament.id == tournament_id:
                the_tournament = tournament
        if the_tournament == None:
            print("No tournament found with tournament id:{}".format(tournament))
            return

        print()
        new_date = input("Enter new date(yyy.mm.dd): ")
        
        the_tournament.date = new_date
        self.logic_wrapper.update_tournament(the_tournament)  
        
        
        
       
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
            tournament = Tournament()
            update_tournamnet = self.logic_wrapper.update_tournament(tournament)
            for info in update_tournamnet:
                print(info)    
                '''
