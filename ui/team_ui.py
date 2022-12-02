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
        print("c. Continue")
        print("b. Go Back")

    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter command: ")
        if command == "b":
            return "b"
        elif command == "c":
            print()
            team = Team()
            team.name = input("Enter name team: ")
            team.club = input("Enter name of club: ")
            self.logic_wrapper.create_team(team)

