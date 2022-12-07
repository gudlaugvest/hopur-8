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
            while how_many < 4:
                print()
                print("Players for each team has to be at least 4! Please try again!\n")
                how_many = int(input("How many players?: "))
                print()
            else:
                for i in range(how_many):
                    print()
                    player = Player()
                    player.name = input("Enter Name: ")
                    player.ss_number = input("Enter Social Security Number(0000000000): ")
                    try:
                        if len(player.ss_number) != 10:
                            raise ValueError()
                    
                    player.home_address = input("Enter Home Address: ")
                    player.phone_number = input("Enter phone number: ")
                    try:
                        if len(player.phone_number) != 7:
                            raise ValueError("Not a valid phone number, try again")  
                    except ValueError as err:
                        print(ValueError, err)
                        player.phone_number = input("Enter phone number: ")      
                    player.email_address = input("Enter Email Address: ")
                    player.role = input("Enter Players Role(Captain/Player): ")
                    try:
                        if player.role == "Player".lower() or "Captain".lower():
                            raise ValueError("Not a valid role, try again")
                    except ValueError as err:
                        print(ValueError, err)
                        player.role = input("Enter Players Role(Captain/Player): ")


                    
        else:
            print()
            print("Invalid input, please try again!")

"""while len(player.ss_number) != 10:
                        print("Invalid ss number, try again")
                        player.ss_number = input("Enter Social Security Number(0000000000): ")"""

'''team_name = input("Enter Team Name: ")
                    team_name = team_name.lower()
                    team = self.logic_wrapper.get_team_by_name(team_name) 
                    while team is None:
                        print()
                        print("No team found with that name")
                        team_name = input("Enter Team Name: ")
                        team_name = team_name.lower()
                        team = self.logic_wrapper.get_team_by_name(team_name)  
                    print()          
                    player.team_name = team.name
                    self.logic_wrapper.create_player(player)'''                        