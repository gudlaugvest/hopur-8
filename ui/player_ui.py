from model.player_model import Player


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("####################################")
        print()
        print("Player".rjust(18))
        print()
        print("c. Continue To Input Player Info")
        print("b. Go Back To Organizer Menu")


    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "c":
            print()
            how_many = int(input("How many players?: "))
            if how_many < 4:
                print("Has to be at least 4 players\n")
                how_many = int(input("How many players?: "))
                print()
            else:
                for i in range(how_many):
                    print()
                    player = Player()
                    player.name = input("Enter Name: ")
                    player.ss_number = input("Enter Social Security Number: ")
                    #if len(player.id_number) >= 12:
                    #   print("id number is wrong")
                    #  return player.id_number 
                    player.home_address = input("Enter Home Address: ")
                    player.phone_number = input("Enter Phone Number: ")
                    player.email_address = input("Enter Email Address: ")
                    player.role = input("Enter Players Role(Captein/Player): ")
                    team_name = input("Enter Team Name: ")
                    team = self.logic_wrapper.get_team_by_name(team_name) 
                    print()          
                    
                    if team is None:
                        print("No team found with that name")
                        return
                    player.team_name = team.name
                    self.logic_wrapper.create_player(player)

        else:
            print()
            print("Invalid input, please try again!")