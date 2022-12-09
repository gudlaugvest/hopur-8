from model.player_model import Player
from model.team_model import Team


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """Menu for Players"""
        print()
        print("####################################")
        print()
        print("Player".rjust(18))
        print()
        print("c. Continue To Input Player Info")
        print("u. Update Player Info")
        print("b. Go Back To Organizer Menu")


    def input_prompt(self):
        '''The function counts how many players the Organizer wants to input and inputs the information 
        for each players and gives role for 1 captain and rest players'''
        
        self.menu_output()
        print()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "u":
            self.update_player_info()
        elif command == "c":
            print()
            while True:
                try:
                    how_many = int(input("How many players?: "))
                    while how_many >= 4:
                        for i in range(how_many):
                            print()
                            player = Player()
                            player.name = input("Enter Player name: ")
                            while True:
                                try:
                                    player.ss_number = input("Enter Social Security Number(0000000000): ")
                                    if len(player.ss_number) == 10:
                                        break
                                    else:
                                        print()
                                        print("Invalid ss number, try again")
                                except:
                                    ValueError
                                
                            player.home_address = input("Enter Home Address: ")
                            while True:
                                try:
                                    player.phone_number = input("Enter phone number: ")
                                    if len(player.phone_number) == 7:
                                        break
                                    else:
                                        print()
                                        print("Not a valid phone number, try againn")
                                except:
                                    ValueError
                            player.email_address = input("Enter Email Address: ")
                            player.role = "Player"
                            self.logic_wrapper.create_player(player)
                    else:
                        print()
                        print("Players for each team has to be at least 4! Please try again!")
                except:
                    ValueError
                    print() 
                    ("Invalid input, can't be a string") 
        else:
            print()
            print("Invalid input, please try again!")

    def update_player_info(self):
        """Add 4 players to Team"""
        print("####################################")
        print()
        print("Update Player".rjust(18))
        print()
        print("a. Add player to Team")
        print()
        command = input("Enter command: ")
        if command == "a":
            p = None
            t = None
            first = True
            for i in range(4):
                if first:
                    team.captain_id = check_player
                    captain = "Captain"
                    all_players = self.logic_wrapper.get_all_players()
                    for player in all_players:
                        player.role = captain
                    self.logic_wrapper.change_player_to_captain(captain)
                    self.c
                    first = False
                check_player = input("Input Player SSN: ")
                all_players = self.logic_wrapper.get_all_players()
                for player in all_players:
                    if player.ss_number == check_player:
                        p = player
                team_id = input("Enter ID of Team: ")
                all_teams = self.logic_wrapper.get_all_teams()
                for team in all_teams:
                    if team.id == team_id:
                        t = team
                p.team_id = t.id
                self.logic_wrapper.add_player_to_team(p)
                
