from model.match_results_model import Match_Result_Model
from data.match_result_data import Match_Result_Data
from data.match_data import Match_Data

class Match_Result_Logic:

    def __init__(self):
        self.match_data = Match_Data()
        self.match_result_data = Match_Result_Data()

    def get_all_match_results(self):
        return self.match_result_data.get_all_match_results()

    def get_all_matches(self):
        return self.match_data.get_all_matches()

    def __str__(self):
        return f"{self.home_team} \t {self.type_of_game} \t {self.away_team} \t | {self.results}"