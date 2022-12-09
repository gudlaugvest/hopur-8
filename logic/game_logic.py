class Game_Logic:

    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def create_game(self, game):
        return self.logic_wrapper.create_game(game)

    def get_all_games(self):
        all_games = self.logic_wrapper.get_all_games()
        for game in all_games:
            if game.home_team_player_ssn[0] == "[":
                game.home_team_player_ssn = game.home_team_player_ssn[1:-1].split(", ")
                game.away_team_player_ssn = game.away_team_player_ssn[1:-1].split(", ")
        return all_games

        # Þarf að hafa if setningu afþví það eru ekki allir leikmenn í lista MUNA