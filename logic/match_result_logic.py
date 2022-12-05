
from data.match_result_data import Match_Result_Data


class Match_Result_Logic:

    def __init__(self):
        self.match_result_data = Match_Result_Data()

    def get_all_match_results(self):
        return self.match_result_data.get_all_match_results()

    def get_all_matches(self):
        return self.match_result_data.get_all_match_results()

    def unplayed_matches(self, match_list, date):
        return self.match_result_data.unplayed_matches(match_list, date)
        
    def played_matches(self, match_list, date):
        return self.match_result_data.played_matches(match_list, date)
    
    
    def get_match_results(self, date):
        return self.match_result_data.get_match_results(date)
                

    def get_unplayed_match_results(self, date): 
        return self.match_result_data.get_unplayed_match_results(date)
        

    def get_match_result(self, home_team, type_of_game, away_team):
        return self.match_result_data.get_match_result(home_team, type_of_game, away_team)
        
    def create_match_result(self, home_team, type_of_game, away_team, results):
        return self.match_result_data.create_match_result(home_team, type_of_game, away_team, results)
        

    def new_method(self, home_team, type_of_game, away_team, results):
        return self.match_result_data.new_method(home_team, type_of_game, away_team, results)
        

    def update_match_result(self, home_team, type_of_game, away_team, results):
        return self.match_result_data.update_match_result(home_team, type_of_game, away_team, results)

    def delete_match_result(self, home_team, type_of_game, away_team):
        return self.match_result_data.delete_match_result(home_team, type_of_game, away_team)   