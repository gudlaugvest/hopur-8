class Match_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections

    def get_all_match_results(self):
        return self.data_wrapper.get_all_match_results()

    def unplayed_matches(self, date):
        return self.data_wrapper.unplayed_matches(date)
        
    def played_matches(self, match_list, date):
        return self.data_wrapper.played_matches(match_list, date)
        
    def create_match_result(self, match):
        return self.data_wrapper.create_match_result(match)
        
    def update_match(self, match):
        return self.data_wrapper.update_match(match)

    def delete_match_result(self, home_team, type_of_game, away_team):
        return self.data_wrapper.delete_match_result(home_team, type_of_game, away_team)

    def get_match_by_id(self, match_id):
        return self.data_wrapper.get_match_by_id(match_id)