import csv
from model.match_model import Match

class Match_Data:

    def __init__(self):
        self.file_name = "file/matches.csv"  


    def create_match(self, match):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["home_team", "away_team", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"home_team": match.home_team, "away_team": match.away_team, "date": match.date})


    def get_all_matches(self):
        match_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_list.append(Match(row["home_team"], row["away_team"], row["date"]))
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
        