from model.player_model import Player
from data.player_data import Player_Data


class Player_logic:
    def __init__(self, data_connections):
        '''This function initializes the class'''
        self.data_wrapper = data_connections


    def create_player(self, player):
        '''this function creates a player'''
        self.data_wrapper.create_player(player)


    def get_all_players(self):
        return self.data_wrapper.get_all_players()
      

    """def get_player_by_id(self, id):
        all_players = self.get_all_players()
        for player in all_players:
            if player.id_number == id:
                return player
"""

    def get_player_by_id(self, name):
        all_players = self.get_all_players()
        for player in all_players:
            if player.name == name:
                return player

    def get_list_of_player_and_teams(self):
        data_class = Player_Data()
        result = data_class.read_all_players()
        for elem in result:
            return (f"player: {elem.name}, team: {elem.team_name}")
