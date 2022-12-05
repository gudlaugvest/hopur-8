from model.team_model import Team
from logic.logic_wrapper import Logic_Wrapper


class Team_UI:
    def __init__(self, logic_wrapper: Logic_Wrapper):
        self.logic_wrapper = logic_wrapper

    
    def menu_output(self):
        print()
        print("############################")
        print()
        print(" Team \n".rjust(18))
        print("c. Continue to create Team")
        print("b. Go back to Organizer Menu")


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
            captain_ssn = input("Enter captan id: ")
            captain = self.logic_wrapper.get_player_by_id(captain_ssn)
            if captain is None:
                print()
                print("No player found with that id! Please Try again!")
                return
            team.captain_id = captain.id_number
            self.logic_wrapper.create_team(team)
 

