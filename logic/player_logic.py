from data.data_wrapper import Data_Wrapper
from data.player_data import Player_Data
from model.player_model import Player


class Player_logic:
    def __init__(self, data_connections: Data_Wrapper):
        
        self.data_wrapper = data_connections


    def create_player(self, player):
        self.data_wrapper.create_player(player)


    def get_all_players(self):
        return self.data_wrapper.get_all_players()

