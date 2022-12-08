

class Team_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections
        

    def create_team(self, team):
        return self.data_wrapper.create_team(team)

    def get_team_by_Id(self, team_id):
        return self.data_wrapper.get_team_by_Id(team_id)
    
    def get_captain(self, team_id):
        the_team = self.get_team_by_Id(team_id)
        players = self.data_wrapper.get_all_players()
        for player in players:
            if player.ss_number == the_team.captain_id:
                return player
        return None





    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()


    def get_team_by_name(self, name):
        return self.data_wrapper.get_team_by_name(name)

    def get_team_by_captain_id(self, captain_id):
        return self.data_wrapper.get_team_by_captain_id(captain_id)