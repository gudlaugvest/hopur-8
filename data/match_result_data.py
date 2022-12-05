import csv
from model.match_model import Match

class Match_Result_Data:

    def __init__(self):
        self.file_name = "file/match_results.csv"

    def create_match_result(self, match):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["home_team", "type_of_game", "away_team", "results"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"home_team": match.home_team, "type_of_game": match.type_of_game, "away_team": match.away_team, "results": match.results})

    def get_all_match_results(self):
        match_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_list.append(Match(row["home_team"], row["type_of_game"], row["away_team"], row["results"]))
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
    
    