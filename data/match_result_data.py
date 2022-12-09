import csv
from model.match_results_model import Match_Result_Model

class Match_Result_Data:

    def __init__(self):
        self.file_name = "file/matches.csv"

    def create_match_result(self, match):
        """Create Match and write into a csv file named match.csv"""
        i = len(self.get_all_match_results()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "home_team_id", "type_of_game", "away_team_id", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i, "home_team_id": match.home_team_id, "type_of_game": match.type_of_game, "away_team_id": match.away_team_id,"date": match.date})

    def get_all_match_results(self):
        """Return all Match attributes that are in match.csv file """
        match_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_list.append(Match_Result_Model(row["id"], row["home_team_id"], row["type_of_game"], row["away_team_id"], row["date"]))
        return match_list

    def unplayed_matches(self, date):
        """Loop though matches.csv file and return unplayed matches using the date and return said match"""
        unplayed_matches = []
        match_list = self.get_all_match_results()
        for match in match_list:
            if match.date > date:
                unplayed_matches.append(match)
        return unplayed_matches

    def played_matches(self, match_list, date):
        """Loop through matches.csv file and return played matches using the date and return said match"""
        played_matches = []
        for match in match_list:
            if match < date:
                played_matches.append(match)
        return played_matches



    def get_match_result(self, home_team_id, type_of_game, away_team_id):
        """Loop through matches.csv file and return match result"""
        for match_result in self.get_all_match_results():
            if match_result.home_team_id == home_team_id and match_result.type_of_game == type_of_game and match_result.away_team_id == away_team_id:
                return match_result
   

    def update_match(self, match):
        """Update date of match"""
        all_matches = self.get_all_match_results()
        for i in range(len(all_matches)):
            if match.id == all_matches[i].id:
                all_matches[i] = match
        
        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "home_team_id", "type_of_game", "away_team_id", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(all_matches)):
                writer.writerow({"id": all_matches[i].id, "home_team_id": all_matches[i].home_team_id, "type_of_game": all_matches[i].type_of_game, "away_team_id": all_matches[i].away_team_id,"date": all_matches[i].date})
            
    
    def get_match_by_id(self, id):
        """Loop through mathes.csv file and get match id"""
        all_matches = self.get_all_match_results()
        for match in all_matches:
            if match.id == id:
                return match