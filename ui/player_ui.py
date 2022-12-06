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
        print("c. Continue to input Player info")
        print("b. Go Back to Organizer Menu")


    def validate_team(self):
        try_again = input("Enter do you want to try again (y/n)? ")
        try_again.lower()



    def input_prompt(self):
        self.menu_output()
        print()
        command = input("Enter command: ")
        if command == "b":
            return "b"
        elif command == "c":
            print()
            while True:
                player = Player()
                player.name = input("Enter name of Player: ")
                player.id_number = input("Enter id number: ")
                #if len(player.id_number) >= 12:
                #   print("id number is wrong")
                #  return player.id_number 
                player.home_address = input("Enter home address: ")
                player.phone_number = input("Enter phone number: ")
                player.email_address = input("Enter email address: ")
                team_name = input("Enter team name: ")
                team = self.logic_wrapper.get_team_by_name(team_name)           
                
                if team is None:
                    print("No team found with that name")
                    if self.validate_team() == "n":
                        return
                player.team_id = team.id
                self.logic_wrapper.create_player(player)

        else:
            print()
            print("Invalid input, please try again!")