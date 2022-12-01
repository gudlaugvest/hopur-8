from data.data_wrapper import Data_Wrapper
from model.team_model import Team


class Team_Logic:

    def __init__(self, data_connections : Data_Wrapper()):
        self.data_wrapper = data_connections
        

    def create_team(self, team):
        self.data_wrapper.create_team(team)

    def get_captain(self, team_id):
        teams = self.data_wrapper.get_all_teams()
        correct_team = None
        for team in teams:
            if team.id == team_id:
                correct_team = team
                break
        players = self.data_wrapper.get_all_players()
        correct_player = None
        for player in players:
            if player.id == correct_team.team_captain:
                correct_player = player
                return correct_player
        return None