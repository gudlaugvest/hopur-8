from model.player_model import Player


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Player Menu".rjust(18))
        print()
        print("1. Create Player")
        print("2. List all Players")
        print("b. Go Back")



    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                return "b"
            elif command == "q":
                return "q"
            elif command == "1":
                player = Player()
                player.name = str(input("Enter name of Player: "))
                player.id_number = str(input("Enter id number: "))
                player.home_address = input("Enter in home address: ")
                player.phone_number = input("Enter in phone number: ")
                player.email_address = input("Enter in email address: ")
                player.team = input("Enter in team name: ")
                self.logic_wrapper.create_player(player)
            elif command == "2":
                result = self.logic_wrapper.get_all_players()
                for element in result:
                    print("name: {}, id_number: {}, home_address: {}, phone_number: {}, email_address: {}, team: {}".format(element.name, element.id_number, element.home_address, element.phone_number, element.email_address, element.team))
            else:
                print("Invalid input, try again!")
