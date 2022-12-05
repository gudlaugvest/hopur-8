class Match_Result_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections

    def get_all_match_results(self):
        return self.data_wrapper.get_all_match_results()

    def get_all_matches(self):
        return self.data_wrapper.get_all_match_results()

    def unplayed_matches(self, match_list, date):
        return self.data_wrapper.unplayed_matches(match_list, date)
        
    def played_matches(self, match_list, date):
        return self.data_wrapper.played_matches(match_list, date)
    
    
    def get_match_results(self, date):
        return self.data_wrapper.get_match_results(date)
                

    def get_unplayed_match_results(self, date): 
        return self.data_wrapper.get_unplayed_match_results(date)
        

    def get_match_result(self, home_team, type_of_game, away_team):
        return self.data_wrapper.get_match_result(home_team, type_of_game, away_team)
        
    def create_match_result(self, home_team, type_of_game, away_team, results):
        return self.data_wrapper.create_match_result(home_team, type_of_game, away_team, results)
        

    def new_method(self, home_team, type_of_game, away_team, results):
        return self.data_wrapper.new_method(home_team, type_of_game, away_team, results)
        

    def update_match_result(self, home_team, type_of_game, away_team, results):
        return self.data_wrapper.update_match_result(home_team, type_of_game, away_team, results)

    def delete_match_result(self, home_team, type_of_game, away_team):
        return self.data_wrapper.delete_match_result(home_team, type_of_game, away_team)   