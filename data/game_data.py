import csv
from model.game_model import Game_Model

class Game_data:
    
    def __init__(self):
        self.file_name = "file/game.csv"
    
    def create_game(self, game):
        """Create Game and write into game.csv file"""
        i = len(self.get_all_games()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "home_team_player_ssn", "away_team_player_ssn", "score", "type_of_game", "match_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id" : i, "home_team_player_ssn": game.home_team_player_ssn, "away_team_player_ssn": game.away_team_player_ssn, "score": game.score, "type_of_game": game.type_of_game, "match_id": game.match_id})

    def get_all_games(self):
        """Return all Game attributes that are in game.csv file"""
        game_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                game_list.append(Game_Model(row["id"], row["home_team_player_ssn"], row["away_team_player_ssn"], row["score"], row["type_of_game"], row["match_id"]))
        return game_list

