class Tournament:
    def __init__(self, id="", tournament_name="", number_rounds="", date=""):
        self.tournament_name = tournament_name
        self.number_rounds = number_rounds
        self.date = date
        self.id = id

    def __str__(self):
        return f"{self.id} {self.tournament_name} {self.number_rounds} {self.date}"
