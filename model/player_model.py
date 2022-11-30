class Player:
    def __init__(self, id="", name="", id_number="", home_address="", phone_number="", email_address="", team=""):
        self.id = id
        self.name = name
        self.id_number = id_number
        self.home_address = home_address
        self.phone_number = phone_number
        self. email_address = email_address
        self.team = team


    def __str__(self):
        return f"id: {self.id}, name: {self.name}, id_number: {self.id_number}, home_address: {self.home_address}, phone_number: {self.phone_number}, email_address: {self.email_address}, team: {self.team}"