from data.data_wrapper import Data_Wrapper
from model.team_model import Team


class Team_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections
        

    def team_info(self, team):
        self.data_wrapper.team_info(team)

    def get_captain(self, player):
        self.data_wrapper.get_captain(player)

        