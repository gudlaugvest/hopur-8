class Player:
    def __init__(self, name="", ss_number="", home_address="", phone_number="", email_address="",role = "", team_name=""):
        self.name = name
        self.ss_number = ss_number
        self.home_address = home_address
        self.phone_number = phone_number
        self.email_address = email_address
        self.role = role
        self.team_name = team_name


    def __str__(self):
        return f"name: {self.name}, id_number: {self.ss_number}, home_address: {self.home_address}, phone_number: {self.phone_number}, email_address: {self.email_address}, team_id: {self.team_name}"