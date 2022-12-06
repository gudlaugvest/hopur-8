class Player:
    def __init__(self, name ="", ss_number = "", home_address = "", phone_number = "", email_address = "",role = "", team_name = ""):
        self.name = name
        self.ss_number = ss_number
        self.home_address = home_address
        self.phone_number = phone_number
        self.email_address = email_address
        self.role = role
        self.team_name = team_name


    def __str__(self):
        return f"{self.name:<12} {self.role:<12} {self.team_name:<12}"