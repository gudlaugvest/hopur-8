from model.game_model import Game_Model


class Game_UI:
    
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def menu_output(self):
        """Print out header"""
        print()
        print("####################################\n")
        print("Registering Scores\n".rjust(23))
        
    
    
    def input_prompt(self): # DEBUG og finna afh þetta er skritið
        self.menu_output()
        game = Game_Model()
        while True:
            print("The games are played best out of 3 where the \nhighest possible score is 3-0 or 0-3.\n")
            
            print("Registering results for 501 games\n")
            game_counter = 0
            while game_counter != 4:
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
                    game.score = input("Enter Score (0-0): ").split('-')
                    game.home_team_score = int(game.score[0])
                    game.away_team_score = int(game.score[1])
                
                game_counter += 1
            
                #self.logic_wrapper.create_game(game)
            
            game_counter = 0
            print("Registering results for 301 games\n")
            while game_counter != 1:
                game.home_team_player_ssn = input("Enter Home Team Player1 SSN: ")
                game.home_team_player_ssn = input("Enter Home Team Player2 SSN: ")
                
                game.away_team_player_ssn = input("Enter Away Team Player1 SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player2 SSN: ")

                game.type_of_game = input("Enter Type of Game: ")
                while game.type_of_game != '301':
                    print("Þarft að byrja að skrá 301 leikina!")
                    game.type_of_game = input("Enter Type of Game: ")
                
                game.score = input("Enter Score (0-0): ").split('-')
                game.home_team_score = int(game.score[0])
                game.away_team_score = int(game.score[1])
                while game.home_team_score > 3 or game.away_team_score > 3:
                    print("Invalid Scores please try again!")
                    game.score = input("Enter Score (0-0): ").split('-')
                    game.home_team_score = int(game.score[0])
                    game.away_team_score = int(game.score[1])
                
                game_counter += 1
            
            
                
                #self.logic_wrapper.create_game(game)
            
            game_counter = 0
            print("Registering results for cricket games\n")
            while game_counter != 1:
                game.home_team_player_ssn = input("Enter Home Team Player SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player SSN: ")

                game.type_of_game = input("Type of game: ").lower()
                while game.type_of_game != 'cricket':
                    print("Þarft að byrja að skrá cricket leikina!")
                    game.type_of_game = input("Enter Type of Game: ").lower()
                
                game.score = input("Enter Score (0-0): ").split('-')
                game.home_team_score = int(game.score[0])
                game.away_team_score = int(game.score[1])
                while game.home_team_score > 3 or game.away_team_score > 3:
                    print("Invalid Scores please try again!")
                    game.score = input("Enter Score (0-0): ").split('-')
                    game.home_team_score = int(game.score[0])
                    game.away_team_score = int(game.score[1])    
                
                game_counter += 1
                
                #self.logic_wrapper.create_game(game)
            game_counter = 0
            print("Registering results for last 501 game\n")
            while game_counter != 1:
                game.home_team_player_ssn = input("Enter Home Team Player 1 SSN: ")
                game.home_team_player_ssn = input("Enter Home Team Player 2 SSN: ")
                game.home_team_player_ssn = input("Enter Home Team Player 3 SSN: ")
                game.home_team_player_ssn = input("Enter Home Team Player 4 SSN: ")
                
                game.away_team_player_ssn = input("Enter Away Team Player 1 SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player 2 SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player 3 SSN: ")
                game.away_team_player_ssn = input("Enter Away Team Player 4 SSN: ")


                game.type_of_game = input("Enter type of game: ")
                while game.type_of_game != '501':
                    print("Invalid type of game!\nGame must be 301")
                    game.type_of_game = input("Enter type of game: ")
                
                game.score = input("Enter Score (0-0): ").split('-')
                game.home_team_score = int(game.score[0])
                game.away_team_score = int(game.score[1])
                while game.home_team_score > 3 or game.away_team_score > 3:
                    print("Invalid Scores please try again!")
                    game.score = input("Enter Score (0-0): ").split('-')
                    game.home_team_score = int(game.score[0])
                    game.away_team_score = int(game.score[1])

                game_counter += 1        
            
            self.logic_wrapper.create_game(game)
            return
            # Vandamálið er að í staðinn fyrir að það bætist við spilari og leikur og þannig að þá er forritið
            # að yfirskrifa hvert gildi í hverju skrefi þannig aðeins síðasti home team player og away team player eru skrifaðir
            # sama gildir með type of game og score