from data.player_data import Player_Data
from data.team_data import Team_Data
from data.tournament_data import Tournament_Data
from data.clubs_data import Clubs_Data
from data.match_data import Match_Data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()
        self.team_data = Team_Data()
        self.tournament_data = Tournament_Data()
        self.club_data = Clubs_Data()
        self.match_data = Match_Data()


    def create_player(self, player):
        return self.player_data.create_player(player)


    def get_all_players(self):
        return self.player_data.get_all_players()


    def create_team(self, team):
        return self.team_data.create_team(team)

    def get_all_teams(self):
        return self.team_data.get_all_teams()

    def create_club(self, club):
        return self.club_data.create_club(club)
    
    def get_all_clubs(self):
        return self.club_data.get_all_clubs()

        
    def create_tournament(self, tournament):
        return self.tournament_data.create_tournament(tournament)

    def get_all_tournaments(self):
        return self.tournament_data.get_all_tournaments()


    def create_match(self, match):
        return self.match_data.create_match(match)
        

    def get_all_matches(self):
        return self.match_data.get_all_matches()