
class Game_Model:

    def __init__(self, id="", home_team_player_ssn="", away_team_player_ssn="", score="", type_of_game=""):
        self.id = id
        self.home_team_player_ssn = home_team_player_ssn
        self.away_team_player_ssn = away_team_player_ssn
        self.score = score
        self.type_of_game = type_of_game

    def __str__(self):
        return f"{self.home_team_player_ssn:<24} {self.score} {self.away_team_player_ssn:<24} {self.type_of_game:<24}"