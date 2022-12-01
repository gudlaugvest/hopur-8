class Match:
    def __init__(self, home_team, home_team_score, away_team, away_team_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score

    def __str__(self):
        return f"Home team: {self.home_team} {self.home_team_score}, Away team: {self.away_team} {self.away_team_score}"