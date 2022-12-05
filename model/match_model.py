class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        

    def __str__(self):
        return f"Home team: {self.home_team}, Away team: {self.away_team}"