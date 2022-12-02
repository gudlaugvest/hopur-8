from model.captain_model import Captain

class Captain_Logic():    
    
    def __init__(self, data_connections):
        self.data_wrapper = data_connections

    def create_captain(self, captain: Captain):
        return self.data_wrapper.create_captain(captain)


    def get_captain(self):
        return self.data_wrapper.get_captain()
