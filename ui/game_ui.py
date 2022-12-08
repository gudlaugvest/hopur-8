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
            game_counter = 0
            while game_counter != 4:
                home_team_player_ssn = input("Enter Home Team Player SSN: ")
                away_team_players_ssn = input("Enter Away Team Player SSN: ")
                score = input("Enter Score: ")
                type_of_game = input("Enter Type of Game: ")
                game = Game_Model(home_team_player_ssn, away_team_players_ssn, score, type_of_game)
                game_counter += 1
                self.logic_wrapper.create_game(game)