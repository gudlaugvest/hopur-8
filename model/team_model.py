class Team():
    def __init__(self, team_name = "", captain = "", players = "", club = ""):
        self.team_name = team_name
        self.captain = captain
        self.players = players
        self.club = club

    def __str__(self):
        return f"{self.team_name}"





