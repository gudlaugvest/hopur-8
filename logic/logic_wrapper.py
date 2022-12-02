
from data.data_wrapper import Data_Wrapper
from logic.player_logic import Player_logic
from logic.team_logic import Team_Logic
from logic.tournament_logic import Tournament_Logic
from logic.clubs_logic import Clubs_Logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.tournament_logic = Tournament_Logic(self.data_wrapper)
        self.clubs_logic = Clubs_Logic(self.data_wrapper)

    def create_player(self, player):
        """Takes in customer object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()
   
    def create_team(self, team):
        return self.team_logic.create_team(team)

    def get_captain(self):
        return self.team_logic.get_captain()
    
    def get_player_by_id(self, id):
        return self.player_logic.get_player_by_id(id)

    
    
    
    
    def type_of_tournament(self):
        return self.tournament_logic.type_of_tournament()


    def create_tournament(self):
        return self.tournament_logic.create_tournament()

        

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