from model.team_model import Team
from logic.logic_wrapper import Logic_Wrapper


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


    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "c":
            print()
            team = Team()
            #Fá lista af öllum klúbbum og prenta út
            all_clubs = self.logic_wrapper.get_all_clubs()
            print("Name of clubs:\n".rjust(10))
            for club in all_clubs:
                print("Club Name:{:<10}\n".format(club.name))
            team.club = input("Enter Club name: ")
            #club = self.logic_wrapper.get_club_by_name(team.club)
            #if club is None:
                #print("No club found with that name! Please try again!")
                #return
            #team.club == club.name
            team.name = input("Enter Team Name: ")
            captain_ssn = input("Choose a captain for this team, enter captain SSN: ")
            captain = self.logic_wrapper.get_player_by_id(captain_ssn)
            while captain is None:
                print()
                print("No player found with that id! Please Try again!")
                return
            team.captain_id = captain.ss_number
            self.logic_wrapper.create_team(team)
        else:
            print()
            print("Invalid input, please try again!")