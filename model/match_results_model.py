class Match_Result_Model:

    def __init__(self, id = "", home_team="", type_of_game="", away_team="", date=""):
        self.home_team = home_team
        self.type_of_game = type_of_game
        self.away_team = away_team
        self.date = date
        self.id = id

    def __str__(self):
        return f"{self.home_team:<12} {self.type_of_game:<12} {self.away_team:<12} | {self.date:<6}"
