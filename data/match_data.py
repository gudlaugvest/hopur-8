import csv
from model.matches_model import Match

class Match_Data:

    def __init__(self):
        self.file_name = "data/matches.csv"  


    def create_match(self, match):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["home_team", "away_team"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"home_team": match.home_team, "away_team": match.away_team,})


    def get_all_matches(self):
        match_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_list.append(Match(row["home_team"], row["away_team"]))
        return match_list
