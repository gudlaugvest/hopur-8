from model.game_model import Game_Model

class Game_UI:
    
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def menu_output(self):
        print()
        print("####################################\n")
        print("Registering Scores\n".rjust(23))
        
    
    
    def input_prompt(self):
        while True:
            self.menu_output()
            home_team_player_ssn = input("Enter Home Team Player SSN: ")