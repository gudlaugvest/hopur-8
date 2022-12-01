from data.clubs_data import Clubs_Data
from data.data_wrapper import Data_Wrapper

class Clubs_Logic:

    def __init__(self, data_connections : Data_Wrapper()):
        self.data_wrapper = data_connections


    def create_club(self, club):
        return self.data_wrapper.create_club(club)

    def get_all_clubs(self):
        return self.data_wrapper.get_all_clubs()
