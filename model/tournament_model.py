class Tournament:
    def __init__(self, id="", name="", number_of_rounds="", date=""):
        self.name = name
        self.number_of_rounds = number_of_rounds
        self.date = date
        self.id = id

    def __str__(self):
        return f"{self.id} {self.name} {self.number_of_rounds} {self.date}"
