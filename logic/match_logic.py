from data.data_wrapper import Data_Wrapper

class Match_Logic:


    def __init__(self, data_connections: Data_Wrapper()):
        self.data_wrapper = data_connections

    def create_match(self):
        return self.data_wrapper.create_match()

    def list_all_matches(self):
        return self.data_wrapper.list_all_matches()