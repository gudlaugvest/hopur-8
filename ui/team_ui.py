from model.team_model import Team
from logic.logic_wrapper import Logic_Wrapper
from model.player_model import Player


class Team_UI:
    def __init__(self, logic_wrapper: Logic_Wrapper):
        self.logic_wrapper = logic_wrapper

    
    def menu_output(self):
        print()
        print("############################")
        print()
        print(" Team".rjust(18))
        print()



    def input_prompt(self):
        self.menu_output()
        print()
        team = Team()
        team.name = input("Enter name team: ")
        team.club = input("Enter name of club: ")
        team.captain_id = input("Enter captain id: ")
        print()
        player = Player()
        player.name = input("Enter name of Player: ")
        player.id_number = input("Enter id number: ")
        player.home_address = input("Enter home address: ")
        player.phone_number = input("Enter phone number: ")
        player.email_address = input("Enter email address: ")
        

