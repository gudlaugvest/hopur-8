
from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_Logic
from logic.tournament_logic import Tournament_Logic
from logic.clubs_logic import Clubs_Logic
from logic.match_logic import Match_Logic
from logic.game_logic import Game_Logic


class Logic_Wrapper:
    '''This function takes all the class logics'''
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.tournament_logic = Tournament_Logic(self.data_wrapper)
        self.clubs_logic = Clubs_Logic(self.data_wrapper)
        self.match_result = Match_Logic(self.data_wrapper)
        self.game_logic = Game_Logic(self.data_wrapper)

    def create_player(self, player):
        """Takes in customer object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()
  
    def create_team(self, team):
        return self.team_logic.create_team(team)

    def get_all_teams(self):
        return self.team_logic.get_all_teams()

    def get_captain(self, team_id):
        return self.team_logic.get_captain(team_id)
    
    def get_player_by_id(self, id):
        return self.player_logic.get_player_by_id(id)

    def get_team_by_captain_id(self, captain_id):
        return self.team_logic.get_team_by_captain_id(captain_id)

    def get_all_tournaments(self):
        '''This function gets all tournaments'''
        return self.data_wrapper.get_all_tournaments()    

    def create_tournament(self, tournament):
        return self.tournament_logic.create_tournament(tournament)

    def update_tournament(self, tournament):
        return self.tournament_logic.update_tournament(tournament)    

    def register_team_to_match(self):
        return self.tournament_logic.register_team_to_match()        

    def register_type_of_match(self):
        return self.tournament_logic.register_type_of_match()
        
    def display_final_match(self):
        return self.tournament_logic.display_final_match()

    def create_club(self, club):
        return self.clubs_logic.create_club(club)

    def get_all_clubs(self):
        return self.clubs_logic.get_all_clubs()
       
    def get_team_by_name(self, name):
        return self.team_logic.get_team_by_name(name)

    def get_club_by_name(self, name):
        return self.clubs_logic.get_club_by_name(name)

    def unplayed_matches(self, match_list, date):
        return self.match_result.unplayed_matches(match_list, date)
        
    def played_matches(self, match_list, date):
        return self.match_result.played_matches(match_list, date)
    
    def get_all_match_results(self):
        return self.match_result.get_all_match_results() 
             
    def create_match_result(self, match):
        return self.match_result.create_match_result(match)

    def update_match(self, match):
        return self.match_result.update_match(match)

    def delete_match_result(self, home_team, type_of_game, away_team):
        return self.match_result.delete_match_result(home_team, type_of_game, away_team)        

    def unplayed_matches(self, date):
        return self.match_result.unplayed_matches(date)

    def get_players_from_team_id(self, team_id):
        return self.player_logic.get_players_from_team_id(team_id)

    def get_match_by_id(self, match_id):
        return self.match_result.get_match_by_id(match_id)

    def get_team_name_by_team_id(self, team_id):
        return self.team_logic.get_team_name_by_team_id(team_id)

    def create_game(self, game):
        return self.game_logic.create_game(game)
    
    def get_all_games(self):
        return self.game_logic.get_all_games()

    def get_club_by_name(self, name):
        return self.data_wrapper.get_club_by_name(name)

    def get_team_by_Id(self, id):
        return self.data_wrapper.get_team_by_Id(id)

    def update_player(self, p):
        """Update player attributes in player.csv"""
        return self.data_wrapper.update_player(p)

