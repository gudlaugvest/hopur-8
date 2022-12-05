
from data.match_result_data import Match_Result_Data

class Match_Result_Logic:

    def __init__(self):
        self.match_result_data = Match_Result_Data()

    def get_all_match_results(self):
        return self.match_result_data.get_all_match_results()

    def get_all_matches(self):
        return self.match_data.get_all_matches()

    