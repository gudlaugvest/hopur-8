class Team():
    def __init__(self, team_name = "", captain = "", players = "", club = "", player_id=""):
        self.team_name = team_name
        self.captain = captain
        self.players = players
        self.club = club
        self.player_id = player_id

    def __str__(self):
        return f"{self.team_name}"
    