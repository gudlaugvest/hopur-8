from data.player_data import Player_Data
from data.team_data import Team_Data
from data.tournament_data import Tournament_Data
from data.clubs_data import Clubs_Data
from data.match_result_data import Match_Result_Data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()
        self.team_data = Team_Data()
        self.tournament_data = Tournament_Data()
        self.club_data = Clubs_Data()
        self.match_result_data = Match_Result_Data()


    def create_player(self, player):
        return self.player_data.create_player(player)

    def get_all_players(self):
        return self.player_data.read_all_players()

    def create_team(self, team):
        return self.team_data.create_team(team)

    def get_all_teams(self):
        return self.team_data.get_all_teams()

    def get_captain(self, team_id):
        return self.team_data.get_captain(team_id)

    def get_team_by_Id(self, id):
        return self.team_data.get_team_by_Id(id)

    def get_team_by_name(self, name):
        return self.team_data.get_team_by_name(name)

    def get_team_by_captain_id(self, captain_id):
        return self.team_data.get_team_by_captain_id(captain_id)

    def get_players_by_team_id(self, team_id):
        return self.team_data.get_players_by_team_id(team_id)

    def get_player_by_id(self, id):
        return self.player_data.get_player_by_id(id)

    def create_club(self, club):
        return self.club_data.create_club(club)
    
    def get_all_clubs(self):
        return self.club_data.get_all_clubs()
        
    def create_tournament(self, tournament):
        return self.tournament_data.create_tournament(tournament)

    def update_tournament(self, tournament):
        return self.tournament_data.update_tournament(tournament)    

    def get_all_tournaments(self):
        return self.tournament_data.get_all_tournaments()

    def create_match(self, match):
        return self.match_data.create_match(match)

    def get_all_matches(self):
        return self.match_data.get_all_matches()

    def create_match_result(self, match_result):
        return self.match_result_data.create_match_result(match_result)
    
    def get_all_match_results(self):
        return self.match_result_data.get_all_match_results()
    
    def unplayed_matches(self, date):
        return self.match_result_data.unplayed_matches(date)
    
    def played_matches(self, match_list, date):
        return self.match_result_data.played_matches(match_list, date)
    
      
    
    
    def create_match_result(self, match_result):
        return self.match_result_data.create_match_result(match_result)
    
    
    def update_match(self, match):
        return self.match_result_data.update_match(match)
    
    def delete_match_result(self, match_result):
        return self.match_result_data.delete_match_result(match_result)

    def get_match_by_id(self, id):
        return self.match_result_data.get_match_by_id(id)

    def get_team_name_by_team_id(self, id):
        return self.team_data.get_team_name_by_team_id(id)