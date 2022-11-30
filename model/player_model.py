class Player:
    def __init__(self, name, id_number, home_address, phone_number, email_address, team):
        self.name = name
        self.id_number = id_number
        self.home_address = home_address
        self.phone_number = phone_number
        self. email_address = email_address
        self.team = team


    def __str__(self):
        return "name: {}, id_number: {}, home_address: {}, phone_number: {}, email_address: {}, team: {}".format(self.name, self.id_number, self.home_address, self.phone_number, self.email_address, self.team)