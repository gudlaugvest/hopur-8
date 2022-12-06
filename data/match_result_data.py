import csv
from model.match_results_model import Match_Result_Model

class Match_Result_Data:

    def __init__(self):
        self.file_name = "file/matches.csv"

    def create_match_result(self, match):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["home_team", "type_of_game", "away_team", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"home_team": match.home_team, "type_of_game": match.type_of_game, "away_team": match.away_team,"date": match.date})

    def get_all_match_results(self):
        match_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_list.append(Match_Result_Model(row["home_team"], row["type_of_game"], row["away_team"], row["date"]))
        return match_list

    def unplayed_matches(self, match_list, date):
        unplayed_matches = []
        for match in match_list:
            if match > date:
                unplayed_matches.append(match)
        return unplayed_matches

    def played_matches(self, match_list, date):
        played_matches = []
        for match in match_list:
            if match < date:
                played_matches.append(match)
        return played_matches

    
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

    #def create_match_result(self, match):
    #    match_result = self.new_method(match)
    #    self.match_result_data.create_match_result(match_result)

   

    def update_match_result(self, home_team, type_of_game, away_team, results): 
        match_result = self.get_match_result(home_team, type_of_game, away_team) 
        match_result.results = results 
        self.match_result_data.update_match_result(match_result) 

    def delete_match_result(self, home_team, type_of_game, away_team):
        match_result = self.get_match_result(home_team, type_of_game, away_team)
        self.match_result_data.delete_match_result(match_result)
    
    