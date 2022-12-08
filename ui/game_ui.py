from model.game_model import Game_Model


class Game_UI:
    
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def menu_output(self):
        print()
        print("####################################\n")
        print("Registering Scores\n".rjust(23))
        
    
    
    def input_prompt(self):
        self.menu_output()
        game = Game_Model()
        while True:
            game_counter = 0
            while game_counter != 4:
                print("The games are played best out of 3 where the \nhighest possible score is 3-0 or 0-3.\n")
                #print()
                print("Registering results for 501 games\n")
                game.home_team_player_ssn = input("Enter Home Team Player SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player SSN: ")
                
                game.type_of_game = input("Enter Type of Game: ")
                while game.type_of_game != '501':
                    print("Þarft að byrja að skrá 501 leikina fyrst!")
                    game.type_of_game = input("Enter Type of Game: ")
                
                
                game.score = input("Enter Score (0-0): ").split('-')
                print(game.score)
                home_team_score = int(game.score[0])
                away_team_score = int(game.score[1])
                print(type(home_team_score))
                while home_team_score > 3 or away_team_score > 3:
                    print("Invalid Scores please try again!")
                    score = input("Enter Score (0-0): ").split('-')
                    home_team_score = int(game.score[0])
                    away_team_score = int(game.score[1])
                
                game_counter += 1
            
                #self.logic_wrapper.create_game(game)
            
            counter = 0
            while counter != 1:
                print("Registering results for 301 games\n")
                game.home_team_player_ssn = input("Enter Home Team Player1 SSN: ")
                game.home_team_player_ssn = input("Enter Home Team Player2 SSN: ")
                
                game.away_team_player_ssn = input("Enter Away Team Player1 SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player2 SSN: ")

                type_of_game = input("Enter Type of Game: ")
                while type_of_game != '301':
                    print("Þarft að byrja að skrá 301 leikina!")
                    type_of_game = input("Enter Type of Game: ")
                
                game.score = input("Enter Score (0-0): ").split('-')
                home_team_score = int(game.score[0])
                away_team_score = int(game.score[1])
                while home_team_score > 3 or away_team_score > 3:
                    print("Invalid Scores please try again!")
                    game.score = input("Enter Score (0-0): ").split('-')
                    home_team_score = int(game.score[0])
                    away_team_score = int(game.score[1])
                
                counter += 1
                
                #self.logic_wrapper.create_game(game)
            
            counter = 0
            while counter != 1:
                print("Registering results for cricket games\n")
                game.home_team_player_ssn = input("Enter Home Team Player SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player SSN: ")

                type_of_game = input("Enter Type of Game: ").lower()
                while type_of_game != 'cricket':
                    print("Þarft að byrja að skrá cricket leikina!")
                    type_of_game = input("Enter Type of Game: ").lower()
                
                game.score = input("Enter Score (0-0): ").split('-')
                home_team_score = int(game.score[0])
                away_team_score = int(game.score[1])
                while home_team_score > 3 or away_team_score > 3:
                    print("Invalid Scores please try again!")
                    game.score = input("Enter Score (0-0): ").split('-')
                    home_team_score = int(game.score[0])
                    away_team_score = int(game.score[1])    
                
                counter += 1
                
                #self.logic_wrapper.create_game(game)
            self.logic_wrapper.create_game(game)