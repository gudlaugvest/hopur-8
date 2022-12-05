
class Tournament_Logic:

    def __init__(self, data_connections):
        '''This function initializes the class'''
        self.data_wrapper = data_connections



    def create_tournament(self, tournament):
        '''this function creates a tournament'''
        self.data_wrapper.create_tournament(tournament)


    def get_all_tournaments(self):
        '''This function gets all tournaments'''
        return self.data_wrapper.get_all_tournaments()
        


    def register_type_of_match(self):
        '''This function specifies what type of match'''
        pass


    def get_all_games_in_tournament(self, tournament):
        pass