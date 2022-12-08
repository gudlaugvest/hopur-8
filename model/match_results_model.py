class Match_Result_Model:

    def __init__(self, id = "", home_team_id="", type_of_game="", away_team_id="", date=""):
        self.home_team_id = home_team_id
        self.type_of_game = type_of_game
        self.away_team_id = away_team_id
        self.date = date
        self.id = id

    def __str__(self):
        return f"{self.home_team_id:<12} {self.type_of_game:<12} {self.away_team_id:<12} | {self.date:<6}"
