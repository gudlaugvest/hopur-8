from data.player_data import Player_Data
from data.team_data import Team_Data
from data.tournament_data import Tournament_Data
from data.clubs_data import Clubs_Data
from data.match_data import Match_Data
from data.game_data import Game_data


class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()
        self.team_data = Team_Data()
        self.tournament_data = Tournament_Data()
        self.club_data = Clubs_Data()
        self.match_result_data = Match_Data()
        self.game_data = Game_data()


    def create_player(self, player):
        """Create Player and write into a csv file named player.csv"""
        return self.player_data.create_player(player)

    def get_all_players(self):
        """Return all Player attributes that are in player.csv file """
        return self.player_data.read_all_players()

    def create_team(self, team):
        """Create Team and write into csv file named team.csv"""
        return self.team_data.create_team(team)

    def get_all_teams(self):
        """Return all Team attributes that are in team.csv file"""
        return self.team_data.get_all_teams()

    def get_captain(self, team_id):
        """Get captain ssn number from player.csv file and return that player if captain is not found return None"""
        return self.team_data.get_captain(team_id)

    def get_team_by_Id(self, id):
        '''Gets team information from their id'''
        return self.team_data.get_team_by_Id(id)

    def get_team_by_name(self, name):
        return self.team_data.get_team_by_name(name)

    def get_team_by_captain_id(self, captain_id):
        '''Gets information about the team that contains the captains id'''
        return self.team_data.get_team_by_captain_id(captain_id)

    def get_players_by_team_id(self, team_id):
        '''Gets all players with the same team id'''
        return self.team_data.get_players_by_team_id(team_id)

    def get_player_by_id(self, id):
        return self.player_data.get_player_by_id(id)

    def create_club(self, club):
        '''Creates a club and writes it into the csv file'''
        return self.club_data.create_club(club)
    
    def get_all_clubs(self):
        '''Gets all clubs from the csv file'''
        return self.club_data.get_all_clubs()
        
    def create_tournament(self, tournament):
        '''Creates a tournament and writes it into the csv file'''
        return self.tournament_data.create_tournament(tournament)

    def update_tournament(self, tournament):
        return self.tournament_data.update_tournament(tournament)    

    def get_all_tournaments(self):
        '''Gets all tournaments from the csv file'''
        return self.tournament_data.get_all_tournaments()


    def create_match_result(self, match_result):
        '''Creates a match and writes it into the csv file'''
        return self.match_result_data.create_match_result(match_result)
    
    def get_all_match_results(self):
        '''Gets all matches from the csv file'''
        return self.match_result_data.get_all_match_results()
    
    # def unplayed_matches(self, date):
    #     '''Gets all matches that are not played yet'''
    #     return self.match_result_data.unplayed_matches(date)
    
    # def played_matches(self, match_list, date):
    #     '''Gets all matches that are played'''
    #     return self.match_result_data.played_matches(match_list, date)
    
    
    
    def update_match(self, match):
        '''Updates a match and writes it into the csv file'''
        return self.match_result_data.update_match(match)

    
    def unplayed_matches(self, date):
        return self.match_result_data.unplayed_matches(date)

    def get_match_by_id(self, id):
        '''Gets a match by its id'''
        return self.match_result_data.get_match_by_id(id)

    def get_team_name_by_team_id(self, id):
        '''Gets a team name by its id'''
        return self.team_data.get_team_name_by_team_id(id)

    def create_game(self, game):
        '''Creates a game and writes it into the csv file'''
        return self.game_data.create_game(game)
    
    def get_all_games(self):
        '''Gets all games from the csv file'''
        return self.game_data.get_all_games()

    def get_club_by_name(self, name):
        '''Gets a club by its name'''
        return self.get_club_by_name(name)

    