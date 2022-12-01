class Tournament:
    def __init__(self, organizer_name="", tournament_name="", number_rounds="", date=""):
        self.organizer_name = organizer_name
        self.tournament_name = tournament_name
        self.number_rounds = number_rounds
        self.date = date

    def __str__(self):
        return f"{self.organizer_name} {self.tournament_name} {self.number_rounds} {self.date}"
