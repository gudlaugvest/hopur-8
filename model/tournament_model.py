class Tournament:
    def __init__(self, id="", name="", number_of_rounds="", start_date="", end_date=""):
        self.name = name
        self.number_of_rounds = number_of_rounds
        self.start_date = start_date
        self.end_date = end_date
        self.id = id

    def __str__(self):
        return f"{self.id} {self.name} {self.number_of_rounds} {self.start_date} {self.end_date}"
