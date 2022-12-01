from ui.player_ui import Player_UI
from model.team_model import Team



class Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    
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
        team.team_name = input("Enter name team: ")
        team.captain = input("Enter name of captain: ")
        team.club = input("Enter name of club: ")
        player_ui = Player_UI(self.logic_wrapper)
        player_ui.input_prompt()
        self.logic_wrapper.create_team(team)





            
