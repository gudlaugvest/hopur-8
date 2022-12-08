class Team():
    def __init__(self, id="", name = "", club = "", captain_id=""):
        self.id = id
        self.name = name
        self.club = club
        self.captain_id = captain_id

    def __str__(self):
        return f"Name: {self.name}"