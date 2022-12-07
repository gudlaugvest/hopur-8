class Captain:
    def __init__(self, id = "", name="", club="", captain_id = ""):
        self.captain_id = captain_id
        self.id = id
        self.name = name
        self.club = club



    def __str__(self):
        return f"Id: {self.id}: Captain: {self.captain_id}"   
        