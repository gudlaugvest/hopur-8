from data.player_data import Player_Data
from data.team_data import Team_Data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()
        self.team_data = Team_Data()


    def create_player(self, player):
        return self.player_data.create_player(player)

    def get_all_players(self):
        return self.player_data.get_all_players()


    def create_team(self):
        return self.team_data.create_team()

    def get_all_teams(self):
        return self.team_data.get_all_teams()