class Tournament:
    def __init__(self, id="", name="", matches="", start_date="", end_date=""):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.id = id
        self.matches = matches

    def __str__(self):
        return f"{self.id} {self.name} {self.number_of_rounds} {self.start_date} {self.end_date} {self.matches}"
