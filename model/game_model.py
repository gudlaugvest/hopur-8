
class Game_Model:

    def __init__(self, id="", home_team_player_ssn="", away_team_player_ssn="", score="", type_of_game="", match_id=""):
        self.id = id
        self.home_team_player_ssn = home_team_player_ssn
        self.away_team_player_ssn = away_team_player_ssn
        self.score = score
        self.type_of_game = type_of_game
        self.match_id = match_id


    def __str__(self):
        homestr = str(self.home_team_player_ssn)
        homestr = homestr.replace("[", "")
        homestr = homestr.replace("'", "")
        homestr = homestr.replace("\"", "")
        homestr = homestr.replace("]", "")
        awaystr = str(self.away_team_player_ssn)
        awaystr = awaystr.replace("[", "")
        awaystr = awaystr.replace("'", "")
        awaystr = awaystr.replace("\"", "")
        awaystr = awaystr.replace("]", "")
        scorestr = str(self.score)
        scorestr = scorestr.replace("[", "")
        scorestr = scorestr.replace("'", "")
        scorestr = scorestr.replace("]", "")
        
        return f"{homestr:<48} {scorestr:<24}  {awaystr:<48} {self.type_of_game:<24} {self.match_id:<24}"