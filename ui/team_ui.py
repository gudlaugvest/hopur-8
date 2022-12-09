from model.team_model import Team
from logic.logic_wrapper import Logic_Wrapper
from model.player_model import Player


class Team_UI:
    def __init__(self, logic_wrapper: Logic_Wrapper):
        self.logic_wrapper = logic_wrapper

    
    def menu_output(self):
        print()
        print("####################################")
        print()
        print(" Team \n".rjust(18))
        print("c. Continue To Create Team")
        print("b. Go Back To Organizer Menu")



# Þurfum að breyta þessu þannig að það er fyrst beðið um team_id/team_name og síðan venjulegt
# Síðan afþví að það er beðið um captain id í team.csv-inu þá þarf að hafa þannig að sá sem er captain í liðinu þarf að hafa sömu kennitölu og er í team csv-inu

    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter Command: ")
            if command == "b":
                return "b"
            elif command == "c":
                print()
                team = Team()
                team.name = input("Enter Team Name: ")
                self.logic_wrapper.create_team(team)

            else:
                print()
                print("Invalid input, please try again!")