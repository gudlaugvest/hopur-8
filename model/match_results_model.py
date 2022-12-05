class Match_Result_Model:

    def __init__(self, id = "", home_team="", type_of_game="", away_team="", results=""):
        self.home_team = home_team
        self.type_of_game = type_of_game
        self.away_team = away_team
        self.results = results
        self.id = id

    def __str__(self):
        return f"{self.home_team} \t {self.type_of_game} \t {self.away_team} \t | {self.results}"