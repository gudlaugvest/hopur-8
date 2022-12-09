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
                player = Player()
                #Fá lista af öllum klúbbum og prenta út
                all_clubs = self.logic_wrapper.get_all_clubs()
                print("Name of clubs:\n".rjust(10))
                for club in all_clubs:
                    print("Club Name:{:<10}\n".format(club.name))
                    
                team.club = input("Enter Club name: ")
                #club = self.logic_wrapper.get_club_by_name(team.club)
                #while club is None:
                    #print("No club found with that name! Please try again!")
                    #return
                #team.club == club.name
                team.name = input("Enter Team Name: ")
                print()
                print("Choose a captain for this Team: ")
                print()
                player.name = input("Enter Captain name: ")
                while True:
                    try:
                        player.ss_number = input("Enter Captain SSN: ")
                        if len(player.ss_number) == 10:
                            break
                        else:
                            print("Invalid ss number, please try again!")
                    except:
                        ValueError        

                player.home_address = input("Enter Captain home address: ")
                while True:
                    try:
                        player.phone_number = input("Enter Captain phone number: ")
                        if len(player.phone_number) == 7:
                            break
                        else: 
                            print("Invalid phone number, try again!")
                    except:
                        ValueError        
                player.email_address = input("Enter Captain email address: ")
                player.role = "Captain"
                
                captain_ssn = input("Verify Captain with captain id: ")
                captain = self.logic_wrapper.get_player_by_id(captain_ssn)
                while captain is None:
                    print()
                    print("No player found with that id! Please Try again!")
                    return
                team.captain_id = captain.ss_number
                player.team_id = team.id
                self.logic_wrapper.create_team(team)
                allteams = self.logic_wrapper.get_all_teams()
                newest_team = allteams[-1]
                player.team_id = newest_team.id
                self.logic_wrapper.create_player(player)
            else:
                print()
                print("Invalid input, please try again!")