from model.team_model import Team
from logic.logic_wrapper import Logic_Wrapper


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
        counter = 0
        while counter <=3:
            team.players_id = input("Enter player id: ")
            counter += 1
            self.logic_wrapper.create_team(team)
