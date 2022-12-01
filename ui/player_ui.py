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

    def add_another_player(self):
        add_player = input("Do you want to add another player (yes/no)?: ")
        add_player.lower()


    def input_prompt(self):
        self.menu_output()
        player = Player()
        player.name = input("Enter name of Player: ")
        player.id_number = input("Enter id number: ")
        player.home_address = input("Enter home address: ")
        player.phone_number = input("Enter phone number: ")
        player.email_address = input("Enter email address: ")
        self.logic_wrapper.create_player(player)
        self.add_another_player()