
from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic(self.data_wrapper)

    def create_player(self, player):
        """Takes in customer object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

        