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

    def unplayed_matches(self, date):
        return self.match_data.unplayed_matches(self.get_all_matches(), date)

    def played_matches(self, date):
        return self.match_data.played_matches(self.get_all_matches(), date)

    def get_match_results(self, date):
        match_results = []
        for match in self.played_matches(date):
            for match_result in self.get_all_match_results():
                if match == match_result:
                    match_results.append(match_result)
        return match_results

    def get_unplayed_match_results(self, date):
        unplayed_match_results = []
        for match in self.unplayed_matches(date):
            for match_result in self.get_all_match_results():
                if match == match_result:
                    unplayed_match_results.append(match_result)
        return unplayed_match_results

    def get_match_result(self, home_team, type_of_game, away_team):
        for match_result in self.get_all_match_results():
            if match_result.home_team == home_team and match_result.type_of_game == type_of_game and match_result.away_team == away_team:
                return match_result

    def create_match_result(self, home_team, type_of_game, away_team, results):
        match_result = self.new_method(home_team, type_of_game, away_team, results)
        self.match_result_data.create_match_result(match_result)

    def new_method(self, home_team, type_of_game, away_team, results):
        match_result = Match_Result_Model(home_team, type_of_game, away_team, results)
        return match_result

    def update_match_result(self, home_team, type_of_game, away_team, results):
        match_result = self.get_match_result(home_team, type_of_game, away_team)
        match_result.results = results
        self.match_result_data.update_match_result(match_result)

    def delete_match_result(self, home_team, type_of_game, away_team):
        match_result = self.get_match_result(home_team, type_of_game, away_team)
        self.match_result_data.delete_match_result(match_result)

    def __str__(self):
        return f"{self.home_team} \t {self.type_of_game} \t {self.away_team} \t | {self.results}"