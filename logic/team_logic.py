from model.team_model import Team


class Team_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections
        

    def create_team(self, team):
        self.data_wrapper.create_team(team)


    def get_captain(self, team_id):
        teams = self.get_all_teams()
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
    
    
    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()
    

    def get_team_by_name(self, name):
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.name == name:
                return team