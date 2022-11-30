
from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_Logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)

    def create_player(self, player):
        """Takes in customer object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

        
    def create_team(self):
        return self.team_logic.create_team()

    def get_captain(self):
        return self.team_logic.get_captain()

