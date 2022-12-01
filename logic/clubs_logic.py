from data.clubs_data import Clubs_Data

class Clubs_Logic:

    def __init__(self, data_connections):
        self.data_wrapper = data_connections


    def create_club(self, club):
        return self.data_wrapper.create_club(club)

    def get_all_clubs(self):
        return self.data_wrapper.get_all_clubs()
