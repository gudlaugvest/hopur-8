

class Player_logic:
    def __init__(self, data_connections):
        '''This function initializes the class'''
        self.data_wrapper = data_connections


    def create_player(self, player):
        '''this function creates a player'''
        self.data_wrapper.create_player(player)


    def get_all_players(self):
        return self.data_wrapper.get_all_players()
      

    def get_player_by_id(self, name):
        return self.data_wrapper.get_player_by_id(name)

    def get_player_by_name(self, name):
        return self.data_wrapper.get_player_by_name(name)

    def get_players_by_team_id(self, team_id):
        return self.data_wrapper.get_player_by_team_id(team_id)