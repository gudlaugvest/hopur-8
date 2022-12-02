from model.player_model import Player


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Player".rjust(18))
        print()


    def input_prompt(self):
        self.menu_output()
        player = Player()
        player.name = input("Enter name of Player: ")
        player.id_number = input("Enter id number: ")
        player.home_address = input("Enter home address: ")
        player.phone_number = input("Enter phone number: ")
        player.email_address = input("Enter email address: ")
        team_name = input("Enter team name: ")
        team = self.logic_wrapper.get_team_by_name(team_name)
        if team is None:
            print("No team found with that name")
            return
        player.team_id = team.id
        self.logic_wrapper.create_player(player)
        print()